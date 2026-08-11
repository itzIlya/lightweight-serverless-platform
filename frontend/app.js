const keys = {
  backendUrl: "serverless.frontend.backendUrl",
  userserviceUrl: "serverless.frontend.userserviceUrl",
  access: "serverless.frontend.access",
  refresh: "serverless.frontend.refresh",
  user: "serverless.frontend.user",
};

const state = {
  backendUrl: localStorage.getItem(keys.backendUrl) || "http://localhost:8000",
  userserviceUrl: localStorage.getItem(keys.userserviceUrl) || "http://localhost:8100",
  access: localStorage.getItem(keys.access) || "",
  refresh: localStorage.getItem(keys.refresh) || "",
  user: readStoredJson(keys.user, null),
  functions: [],
  selectedFunction: null,
  buildStatus: null,
  currentInvocation: null,
  invocationReadToken: "",
  buildTimer: null,
  invocationTimer: null,
  lastBuildNoticeState: "",
};

const el = {};

document.addEventListener("DOMContentLoaded", () => {
  bindElements();
  bindEvents();
  renderAuthState();
  showRoute(location.hash || "#home");
  if (state.refresh && !state.access) {
    refreshAccessToken().then(loadMe).then(loadFunctions).catch(clearSession);
  } else if (state.access) {
    loadMe().then(loadFunctions).catch(() => {});
  }
});

window.addEventListener("hashchange", () => showRoute(location.hash || "#home"));

function bindElements() {
  for (const id of [
    "sessionSummary",
    "headerLoginButton",
    "headerSignupButton",
    "heroLoginButton",
    "heroSignupButton",
    "logoutButton",
    "loginForm",
    "signupForm",
    "contactForm",
    "homeView",
    "aboutView",
    "contactView",
    "authView",
    "workspaceView",
    "siteNotice",
    "functionsPanel",
    "editorPanel",
    "refreshFunctionsButton",
    "addFunctionButton",
    "emptyAddFunctionButton",
    "emptyFunctions",
    "functionListWrap",
    "functionsTableBody",
    "backToFunctionsButton",
    "buildStateLabel",
    "refreshBuildButton",
    "buildSummaryPanel",
    "buildOutcomeLabel",
    "buildCanInvokeLabel",
    "buildImageLabel",
    "buildMessageText",
    "invokeGuidePanel",
    "invokeAuthHint",
    "copyInvokeUrlButton",
    "invokeUrlText",
    "sampleInputBox",
    "sampleOutputTitle",
    "sampleOutputBox",
    "samplePollBox",
    "sampleOutputsListBox",
    "sampleOutputDownloadBox",
    "sampleZipDownloadBox",
    "editorTitle",
    "editorForm",
    "codeLineNumbers",
    "codeHighlight",
    "buildButton",
    "buildDetailsPanel",
    "toggleBuildDetailsButton",
    "buildStatusBox",
    "managePanel",
    "loadTokensButton",
    "createTokenForm",
    "copyRawTokenButton",
    "rawTokenBox",
    "tokensTableBody",
    "invokeForm",
    "invokeModeHint",
    "submitInvocationButton",
    "loadHistoryButton",
    "historyTableBody",
    "invocationStatusBox",
    "resultStatus",
    "resultExitCode",
    "resultBox",
    "stdoutBox",
    "stderrBox",
    "downloadInvocationButton",
    "refreshInvocationButton",
    "apiOutputBox",
  ]) {
    el[id] = document.getElementById(id);
  }
}

function bindEvents() {
  el.headerLoginButton.addEventListener("click", () => showAuth("login"));
  el.headerSignupButton.addEventListener("click", () => showAuth("signup"));
  el.heroLoginButton.addEventListener("click", () => showAuth("login"));
  el.heroSignupButton.addEventListener("click", () => showAuth("signup"));
  el.logoutButton.addEventListener("click", () => withButton(el.logoutButton, logout));
  el.loginForm.addEventListener("submit", (event) => withForm(event, login));
  el.signupForm.addEventListener("submit", (event) => withForm(event, signup));
  el.contactForm.addEventListener("submit", onContactDraft);
  el.refreshFunctionsButton.addEventListener("click", () => withButton(el.refreshFunctionsButton, loadFunctions));
  el.addFunctionButton.addEventListener("click", openNewFunctionEditor);
  el.emptyAddFunctionButton.addEventListener("click", openNewFunctionEditor);
  el.backToFunctionsButton.addEventListener("click", () => {
    location.hash = "#functions";
  });
  el.editorForm.addEventListener("submit", (event) => withForm(event, buildFromEditor, el.buildButton));
  el.editorForm.elements.invoke_access.addEventListener("change", renderInvokeGuide);
  el.refreshBuildButton.addEventListener("click", () => withButton(el.refreshBuildButton, () => refreshBuild(false)));
  el.copyInvokeUrlButton.addEventListener("click", () => withButton(el.copyInvokeUrlButton, copyInvokeUrl));
  el.toggleBuildDetailsButton.addEventListener("click", toggleBuildDetails);
  editorField("code").addEventListener("input", renderCodeEditor);
  editorField("code").addEventListener("scroll", syncCodeEditorScroll);
  editorField("code").addEventListener("keydown", onCodeEditorKeydown);
  el.loadTokensButton.addEventListener("click", () => withButton(el.loadTokensButton, loadTokens));
  el.createTokenForm.addEventListener("submit", (event) => withForm(event, createToken));
  el.copyRawTokenButton.addEventListener("click", () => withButton(el.copyRawTokenButton, copyRawToken));
  el.invokeForm.addEventListener("submit", (event) => withForm(event, invokeFunction));
  el.invokeForm.elements.invoke_mode.forEach((radio) => {
    radio.addEventListener("change", renderInvocationMode);
  });
  el.invokeForm.elements.input_files.addEventListener("change", renderInvocationMode);
  el.loadHistoryButton.addEventListener("click", () => withButton(el.loadHistoryButton, loadInvocationHistory));
  el.downloadInvocationButton.addEventListener("click", () => withButton(el.downloadInvocationButton, downloadCurrentInvocation));
  el.refreshInvocationButton.addEventListener("click", () => withButton(el.refreshInvocationButton, () => refreshInvocation(false)));
}

function showRoute(hash) {
  const route = String(hash || "#home").replace("#", "");
  for (const view of [el.homeView, el.aboutView, el.contactView, el.authView, el.workspaceView]) {
    view.classList.remove("is-active");
  }

  if (!state.user) {
    if (route === "about") el.aboutView.classList.add("is-active");
    else if (route === "contact") el.contactView.classList.add("is-active");
    else if (route === "auth") el.authView.classList.add("is-active");
    else el.homeView.classList.add("is-active");
    return;
  }

  el.workspaceView.classList.add("is-active");
  if (route === "editor") showWorkspacePanel("editor");
  else showWorkspacePanel("functions");
}

function showWorkspacePanel(name) {
  el.functionsPanel.classList.toggle("is-active", name === "functions");
  el.editorPanel.classList.toggle("is-active", name === "editor");
}

function showAuth(mode) {
  location.hash = "#auth";
  requestAnimationFrame(() => {
    if (mode === "signup") el.signupForm.scrollIntoView({ block: "center" });
    else el.loginForm.scrollIntoView({ block: "center" });
  });
}

async function login(event) {
  event.preventDefault();
  const form = new FormData(event.currentTarget);
  const response = await api(state.userserviceUrl, "/api/auth/token/", {
    method: "POST",
    auth: false,
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      username: form.get("username"),
      password: form.get("password"),
    }),
  });
  setSession(response);
  await loadFunctions();
  notify("Logged in. Your functions are ready.");
  location.hash = "#functions";
}

async function signup(event) {
  event.preventDefault();
  const form = new FormData(event.currentTarget);
  const response = await api(state.userserviceUrl, "/api/auth/register/", {
    method: "POST",
    auth: false,
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      first_name: form.get("first_name") || "",
      last_name: form.get("last_name") || "",
      username: form.get("username"),
      email: form.get("email") || "",
      password: form.get("password"),
    }),
  });
  setSession(response);
  await loadFunctions();
  notify("Account created. Your functions are ready.");
  location.hash = "#functions";
}

async function logout() {
  try {
    await api(state.userserviceUrl, "/api/auth/logout/", { method: "POST", auth: false });
  } finally {
    clearSession();
    notify("");
    location.hash = "#home";
  }
}

async function loadMe() {
  const user = await api(state.userserviceUrl, "/api/auth/me/");
  state.user = user;
  localStorage.setItem(keys.user, JSON.stringify(user));
  renderAuthState();
}

function setSession(response) {
  state.user = response.user || null;
  state.access = response.access || "";
  state.refresh = response.refresh || "";
  localStorage.setItem(keys.user, JSON.stringify(state.user));
  localStorage.setItem(keys.access, state.access);
  localStorage.setItem(keys.refresh, state.refresh);
  renderAuthState();
  showOutput(response);
}

function clearSession() {
  state.user = null;
  state.access = "";
  state.refresh = "";
  state.functions = [];
  state.selectedFunction = null;
  state.buildStatus = null;
  state.currentInvocation = null;
  state.lastBuildNoticeState = "";
  localStorage.removeItem(keys.user);
  localStorage.removeItem(keys.access);
  localStorage.removeItem(keys.refresh);
  renderAuthState();
  renderFunctions();
  renderBuild();
  renderInvocation(null);
}

function renderAuthState() {
  document.body.classList.toggle("is-authenticated", Boolean(state.user));
  el.sessionSummary.textContent = state.user ? `${state.user.username} / ${state.user.role}` : "Signed out";
}

async function loadFunctions() {
  const response = await api(state.backendUrl, "/api/functions/");
  state.functions = Array.isArray(response) ? response : [];
  if (state.selectedFunction?.id) {
    state.selectedFunction = state.functions.find((item) => item.id === state.selectedFunction.id) || state.selectedFunction;
  }
  renderFunctions();
  renderBuild();
  showOutput(response);
}

function renderFunctions() {
  const hasFunctions = state.functions.length > 0;
  el.emptyFunctions.hidden = hasFunctions;
  el.functionListWrap.hidden = !hasFunctions;
  el.functionsTableBody.innerHTML = "";
  for (const fn of state.functions) {
    const row = document.createElement("tr");
    row.innerHTML = `
      <td>${escapeHtml(fn.name)}</td>
      <td>${escapeHtml(fn.invoke_access)}</td>
      <td>${escapeHtml(fn.build_status)}</td>
      <td>${escapeHtml(fn.active_version?.version || "")}</td>
      <td>${escapeHtml(formatDate(fn.updated_at))}</td>
      <td><button type="button">Edit</button></td>
    `;
    row.querySelector("button").addEventListener("click", () => openExistingFunctionEditor(fn.id));
    el.functionsTableBody.appendChild(row);
  }
}

function openNewFunctionEditor() {
  state.selectedFunction = null;
  state.buildStatus = null;
  state.currentInvocation = null;
  state.lastBuildNoticeState = "";
  resetEditorForm();
  renderBuild();
  renderInvokeGuide();
  renderInvocationMode();
  renderTokens([]);
  renderRawToken("");
  renderHistory([]);
  renderInvocation(null);
  el.managePanel.hidden = true;
  el.buildDetailsPanel.hidden = true;
  el.editorTitle.textContent = "New Function";
  notify("New function editor opened.");
  location.hash = "#editor";
}

function openExistingFunctionEditor(functionId) {
  const fn = state.functions.find((item) => String(item.id) === String(functionId));
  if (!fn) return;
  state.selectedFunction = fn;
  state.buildStatus = null;
  state.currentInvocation = null;
  resetEditorForm();
  loadFunctionIntoEditor(fn);
  renderBuild();
  renderInvokeGuide();
  renderInvocationMode();
  renderInvocation(null);
  el.managePanel.hidden = false;
  el.buildDetailsPanel.hidden = false;
  renderRawToken("");
  loadTokens().catch(() => {});
  loadInvocationHistory().catch(() => {});
  refreshBuild(false).catch(() => {});
  notify(`Editing ${fn.name}.`);
  location.hash = "#editor";
}

function resetEditorForm() {
  el.editorForm.reset();
  editorField("name").value = "";
  editorField("description").value = "";
  editorField("invoke_access").value = "private";
  editorField("handler").value = "handler.main";
  editorField("code").value = `def main(event, context):
    print("hello from stdout")
    return {"echo": event}`;
  editorField("requirements").value = "";
  editorField("config").value = "{}";
  editorField("declared_output_files").value = "";
  editorField("invocation_input_max_files").value = 1;
  editorField("invocation_input_max_size_mb").value = 10;
  editorField("invocation_input_max_total_size_mb").value = 10;
  editorField("invocation_output_max_files").value = 5;
  editorField("invocation_output_max_file_size_mb").value = 10;
  editorField("invocation_output_max_total_size_mb").value = 10;
  renderCodeEditor();
}

function loadFunctionIntoEditor(fn) {
  el.editorTitle.textContent = fn.name;
  editorField("name").value = fn.name || "";
  editorField("description").value = fn.description || "";
  editorField("invoke_access").value = fn.invoke_access || "private";
  if (fn.active_version) loadVersionIntoEditor(fn.active_version);
  renderCodeEditor();
}

function loadVersionIntoEditor(version) {
  editorField("handler").value = version.handler || "handler.main";
  editorField("config").value = JSON.stringify(version.config || {}, null, 2);
  editorField("invocation_input_max_files").value = version.invocation_input_max_files ?? 1;
  editorField("invocation_input_max_size_mb").value = version.invocation_input_max_size_mb ?? 10;
  editorField("invocation_input_max_total_size_mb").value = version.invocation_input_max_total_size_mb ?? 10;
  editorField("invocation_output_max_files").value = version.invocation_output_max_files ?? 5;
  editorField("invocation_output_max_file_size_mb").value = version.invocation_output_max_file_size_mb ?? 10;
  editorField("invocation_output_max_total_size_mb").value = version.invocation_output_max_total_size_mb ?? 10;
  editorField("declared_output_files").value = (version.declared_output_files || []).join("\n");
  const inputTypes = new Set(version.invocation_input_mime_types || []);
  el.editorForm.querySelectorAll('input[name="input_type"]').forEach((box) => {
    box.checked = inputTypes.has(box.value);
  });
}

function editorField(name) {
  return el.editorForm.elements[name];
}

function renderCodeEditor() {
  const textarea = editorField("code");
  const value = textarea.value || "";
  const lineCount = Math.max(1, value.split("\n").length);
  el.codeLineNumbers.textContent = Array.from({ length: lineCount }, (_, index) => index + 1).join("\n");
  el.codeHighlight.innerHTML = highlightPython(value) + "\n";
  syncCodeEditorScroll();
}

function syncCodeEditorScroll() {
  const textarea = editorField("code");
  el.codeHighlight.scrollTop = textarea.scrollTop;
  el.codeHighlight.scrollLeft = textarea.scrollLeft;
  el.codeLineNumbers.scrollTop = textarea.scrollTop;
}

function onCodeEditorKeydown(event) {
  if (event.key !== "Tab") return;
  event.preventDefault();
  const textarea = event.currentTarget;
  const start = textarea.selectionStart;
  const end = textarea.selectionEnd;
  textarea.value = `${textarea.value.slice(0, start)}    ${textarea.value.slice(end)}`;
  textarea.selectionStart = textarea.selectionEnd = start + 4;
  renderCodeEditor();
}

function highlightPython(source) {
  const tokenPattern = /("""[\s\S]*?"""|'''[\s\S]*?'''|"(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*'|#[^\n]*|@[A-Za-z_][\w.]*|\b(?:False|None|True|and|as|assert|async|await|break|class|continue|def|del|elif|else|except|finally|for|from|global|if|import|in|is|lambda|nonlocal|not|or|pass|raise|return|try|while|with|yield)\b|\b(?:print|len|range|dict|list|set|tuple|str|int|float|bool|open|enumerate|zip|map|filter|sum|min|max|Exception|ValueError)\b|\b\d+(?:\.\d+)?\b)/g;
  let output = "";
  let cursor = 0;
  for (const match of source.matchAll(tokenPattern)) {
    const token = match[0];
    output += escapeHtml(source.slice(cursor, match.index));
    let className = "syntax-number";
    if (token.startsWith("#")) className = "syntax-comment";
    else if (token.startsWith("\"") || token.startsWith("'")) className = "syntax-string";
    else if (token.startsWith("@")) className = "syntax-decorator";
    else if (/^(print|len|range|dict|list|set|tuple|str|int|float|bool|open|enumerate|zip|map|filter|sum|min|max|Exception|ValueError)$/.test(token)) className = "syntax-builtin";
    else if (!/^\d/.test(token)) className = "syntax-keyword";
    output += `<span class="${className}">${escapeHtml(token)}</span>`;
    cursor = match.index + token.length;
  }
  output += escapeHtml(source.slice(cursor));
  return output;
}

async function buildFromEditor(event) {
  event.preventDefault();
  const form = new FormData(event.currentTarget);
  setBuildButtonState(true);
  try {
    let fn = state.selectedFunction;
    const metadata = {
      name: form.get("name"),
      description: form.get("description") || "",
      invoke_access: form.get("invoke_access"),
    };
    if (!fn) {
      fn = await api(state.backendUrl, "/api/functions/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(metadata),
      });
    } else {
      fn = await api(state.backendUrl, `/api/functions/${fn.id}/`, {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(metadata),
      });
    }
    state.selectedFunction = fn;
    loadFunctionIntoEditor(fn);

    const config = parseJson(form.get("config") || "{}", "Config JSON");
    const zip = buildSourceZip({
      "handler.py": String(form.get("code") || ""),
      "requirements.txt": String(form.get("requirements") || ""),
      "config.json": JSON.stringify(config, null, 2),
    });
    const body = new FormData();
    body.append("source_bundle", new File([zip], "function.zip", { type: "application/zip" }));
    body.append("runtime", "python3.13");
    body.append("handler", form.get("handler") || "handler.main");
    body.append("config", JSON.stringify(config));
    body.append("invocation_input_mime_types", JSON.stringify(selectedInputTypes(form)));
    body.append("declared_output_files", JSON.stringify(outputFileNames(form.get("declared_output_files") || "")));
    for (const key of [
      "invocation_input_max_files",
      "invocation_input_max_size_mb",
      "invocation_input_max_total_size_mb",
      "invocation_output_max_files",
      "invocation_output_max_file_size_mb",
      "invocation_output_max_total_size_mb",
    ]) {
      body.append(key, form.get(key));
    }

    const response = await api(state.backendUrl, fn.links?.source || `/api/functions/${fn.id}/source/`, {
      method: "POST",
      body,
    });
    state.buildStatus = response;
    el.managePanel.hidden = false;
    el.buildDetailsPanel.hidden = false;
    renderBuild();
    scheduleBuildPoll(response);
    await loadFunctions().catch(() => {});
    notify("Your function has been queued for a build.");
    showOutput(response);
  } finally {
    setBuildButtonState(false);
  }
}

async function refreshBuild(auto) {
  if (!state.selectedFunction) {
    notify("Save and build the function first.");
    return;
  }
  const response = await api(state.backendUrl, state.selectedFunction.links?.build_status || `/api/functions/${state.selectedFunction.id}/build-status/`);
  state.buildStatus = response;
  renderBuild();
  renderInvokeGuide();
  if (auto) scheduleBuildPoll(response);
  showOutput(response);
}

function renderBuild() {
  const summary = buildSummary();
  el.buildStateLabel.textContent = summary.stateLabel;
  el.buildOutcomeLabel.textContent = summary.outcome;
  el.buildCanInvokeLabel.textContent = summary.canInvoke ? "Yes" : "No";
  el.buildImageLabel.textContent = summary.imageRef || "None";
  el.buildMessageText.textContent = summary.message;
  el.buildStatusBox.textContent = state.buildStatus ? JSON.stringify(state.buildStatus, null, 2) : "No build status loaded.";
  el.buildSummaryPanel.dataset.state = summary.stateLabel;
  maybeNotifyBuildTerminal(summary);
  renderInvokeGuide(summary);
}

function renderInvokeGuide(summary = buildSummary()) {
  const fn = state.selectedFunction;
  const access = editorField("invoke_access")?.value || fn?.invoke_access || "private";
  const url = fn ? urlFor(state.backendUrl, fn.links?.invoke || `/api/functions/${fn.id}/invoke/`) : "";
  el.invokeUrlText.textContent = url || "No function selected.";
  el.copyInvokeUrlButton.disabled = !url;
  el.invokeAuthHint.textContent = invokeAuthHint(access, summary.canInvoke, Boolean(fn));
  el.sampleOutputTitle.textContent = selectedInvokeMode() === "sync"
    ? "Direct Sync Response"
    : "Initial Queue Response";
  el.sampleInputBox.textContent = JSON.stringify(sampleInvokeRequest(access), null, 2);
  el.sampleOutputBox.textContent = JSON.stringify(sampleInvokeResponse(), null, 2);
  el.samplePollBox.textContent = JSON.stringify(samplePollRequest(access), null, 2);
  el.sampleOutputsListBox.textContent = JSON.stringify(sampleOutputsListRequest(access), null, 2);
  el.sampleOutputDownloadBox.textContent = JSON.stringify(sampleOutputDownloadRequest(access), null, 2);
  el.sampleZipDownloadBox.textContent = JSON.stringify(sampleZipDownloadRequest(access), null, 2);
}

function invokeAuthHint(access, canInvoke, hasFunction) {
  if (!hasFunction) return "Create or open a function first. The image tag is internal and is not the invoke URL.";
  const prefix = canInvoke
    ? "This function has a built image and can be invoked."
    : "The URL is stable, but invocation will work after a successful build.";
  if (access === "public") return `${prefix} Public functions do not need JWT or a function token.`;
  if (access === "token") return `${prefix} Token functions require X-Function-Token from the token manager.`;
  return `${prefix} Private functions require the owner's Bearer JWT.`;
}

function sampleInvokeRequest(access) {
  const mode = selectedInvokeMode();
  const path = mode === "sync"
    ? state.selectedFunction?.links?.invoke_sync || `/api/functions/${state.selectedFunction?.id || "{function_id}"}/invoke-sync/`
    : state.selectedFunction?.links?.invoke || `/api/functions/${state.selectedFunction?.id || "{function_id}"}/invoke/`;
  const headers = { "Content-Type": "application/json" };
  if (access === "private") headers.Authorization = "Bearer <userservice-access-jwt>";
  if (access === "token") headers["X-Function-Token"] = "fn_<raw-function-token>";
  return {
    method: "POST",
    url: state.selectedFunction
      ? urlFor(state.backendUrl, path)
      : urlFor(state.backendUrl, path),
    invocation_type: mode === "sync" ? "sync" : "async",
    headers,
    body: {
      event: {
        message: "hello",
        value: 42,
      },
    },
  };
}

function sampleInvokeResponse() {
  if (selectedInvokeMode() === "sync") {
    return {
      id: 123,
      request_id: "8a5a0c5b-7b91-4a1d-9b8b-3a122e86a000",
      status: "succeeded",
      exit_code: 0,
      result: { echo: { message: "hello", value: 42 } },
      stdout: "hello from stdout\n",
      stderr: "",
      read_token: "inv_<read-token-returned-once>",
      links: {
        self: "/api/invocations/123/",
        download: "/api/invocations/123/download/",
      },
      timeout_fallback: {
        status_code: 202,
        detail: "Invocation is still running. Continue polling.",
      },
    };
  }
  return {
    id: 123,
    request_id: "8a5a0c5b-7b91-4a1d-9b8b-3a122e86a000",
    status: "queued",
    poll_after_seconds: 1,
    read_token: "inv_<read-token-returned-once>",
    links: {
      self: "/api/invocations/123/",
      download: "/api/invocations/123/download/",
    },
    terminal_result_shape: {
      status: "succeeded",
      exit_code: 0,
      result: { echo: { message: "hello", value: 42 } },
      stdout: "hello from stdout\n",
      stderr: "",
      can_download: true,
    },
  };
}

function selectedInvokeMode() {
  return el.invokeForm?.elements.invoke_mode?.value || "async";
}

function syncInvocationEligibility() {
  const version = state.selectedFunction?.active_version || state.buildStatus?.active_version || null;
  const declaredOutputs = version?.declared_output_files || [];
  const files = el.invokeForm?.elements.input_files?.files || [];
  if (!state.selectedFunction) return { ok: false, reason: "Select or build a function before invoking." };
  if (declaredOutputs.length > 0) {
    return {
      ok: false,
      reason: "Sync is disabled because this function declares output files. Use async so outputs can be published and downloaded.",
    };
  }
  if (files.length > 0) {
    return {
      ok: false,
      reason: "Sync is disabled while input files are attached. Use async for file inputs.",
    };
  }
  return {
    ok: true,
    reason: "Sync will wait briefly and return result, stdout, stderr, and exit status directly.",
  };
}

function renderInvocationMode() {
  if (!el.invokeForm) return;
  const mode = selectedInvokeMode();
  const sync = syncInvocationEligibility();
  if (mode === "sync" && !sync.ok) {
    el.invokeModeHint.textContent = sync.reason;
    el.submitInvocationButton.textContent = "Sync Unavailable";
    el.submitInvocationButton.disabled = true;
  } else if (mode === "sync") {
    el.invokeModeHint.textContent = sync.reason;
    el.submitInvocationButton.textContent = "Invoke Sync";
    el.submitInvocationButton.disabled = false;
  } else {
    el.invokeModeHint.textContent = "Async queues the invocation immediately. Use it for file inputs, declared output files, and longer-running functions.";
    el.submitInvocationButton.textContent = "Invoke Async";
    el.submitInvocationButton.disabled = false;
  }
  renderInvokeGuide();
}

function sampleResultHeaders(access) {
  const headers = {};
  if (access === "private") headers.Authorization = "Bearer <userservice-access-jwt>";
  else headers["X-Invocation-Read-Token"] = "inv_<read-token-returned-once>";
  return headers;
}

function sampleInvocationId() {
  return state.currentInvocation?.id || 123;
}

function samplePollRequest(access) {
  const invocationId = sampleInvocationId();
  return {
    method: "GET",
    url: urlFor(state.backendUrl, `/api/invocations/${invocationId}/`),
    headers: sampleResultHeaders(access),
    response_when_done: {
      id: invocationId,
      status: "succeeded",
      exit_code: 0,
      result: { echo: { message: "hello", value: 42 } },
      stdout: "hello from stdout\n",
      stderr: "",
      outputs_available: true,
      can_download: true,
      links: {
        outputs: `/api/invocations/${invocationId}/outputs/`,
        download: `/api/invocations/${invocationId}/download/`,
      },
    },
  };
}

function sampleOutputsListRequest(access) {
  const invocationId = sampleInvocationId();
  return {
    method: "GET",
    url: urlFor(state.backendUrl, `/api/invocations/${invocationId}/outputs/`),
    headers: sampleResultHeaders(access),
    response: [
      {
        id: 456,
        original_path: "report.txt",
        safe_name: "report.txt",
        content_type: "text/plain",
        size_bytes: 128,
        position: 0,
        links: {
          download: `/api/invocations/${invocationId}/outputs/456/download/`,
        },
      },
    ],
  };
}

function sampleOutputDownloadRequest(access) {
  const invocationId = sampleInvocationId();
  return {
    method: "GET",
    url: urlFor(state.backendUrl, `/api/invocations/${invocationId}/outputs/456/download/`),
    headers: sampleResultHeaders(access),
    response: "Binary/file response for one declared output file.",
  };
}

function sampleZipDownloadRequest(access) {
  const invocationId = sampleInvocationId();
  return {
    method: "GET",
    url: urlFor(state.backendUrl, `/api/invocations/${invocationId}/download/`),
    headers: sampleResultHeaders(access),
    response: "ZIP file containing manifest.json, inputs, outputs, stdout, and stderr.",
  };
}

async function copyInvokeUrl() {
  const url = state.selectedFunction
    ? urlFor(state.backendUrl, state.selectedFunction.links?.invoke || `/api/functions/${state.selectedFunction.id}/invoke/`)
    : "";
  if (!url) throw new Error("No invoke URL is available yet.");
  await copyText(url);
  notify("Invoke URL copied.");
}

async function copyText(value) {
  if (navigator.clipboard?.writeText) {
    await navigator.clipboard.writeText(value);
  } else {
    const input = document.createElement("textarea");
    input.value = value;
    document.body.appendChild(input);
    input.select();
    document.execCommand("copy");
    input.remove();
  }
}

function buildSummary() {
  const build = state.buildStatus;
  const selected = state.selectedFunction;
  const latestVersion = build?.active_version || build?.latest_version || selected?.active_version || null;
  const latestAttempt = build?.latest_attempt || selected?.pending_build?.attempt || null;
  const stateLabel = build?.frontend_state || build?.state || selected?.build_status || "not_built";
  const imageRef = latestVersion?.image_ref || selected?.active_image_ref || "";
  const canInvoke = Boolean(build?.can_invoke || (selected?.active_version && selected?.build_status === "built"));

  if (stateLabel === "built") {
    return {
      stateLabel,
      imageRef,
      canInvoke,
      outcome: "Build succeeded",
      message: canInvoke
        ? "The function image was built successfully and this function can now be invoked."
        : "The build is marked built, but the function is not invokable yet. Refresh status once more.",
    };
  }
  if (stateLabel === "failed") {
    return {
      stateLabel,
      imageRef,
      canInvoke: false,
      outcome: "Build failed",
      message: latestAttempt?.log || latestVersion?.build_log || "The build failed. Open Build Details for the backend response.",
    };
  }
  if (stateLabel === "cancelled") {
    return {
      stateLabel,
      imageRef,
      canInvoke: false,
      outcome: "Build cancelled",
      message: latestAttempt?.log || "The build was cancelled before it produced an invokable image.",
    };
  }
  if (["queued", "pending"].includes(stateLabel)) {
    return {
      stateLabel,
      imageRef,
      canInvoke,
      outcome: "Build queued",
      message: "The build job is waiting for a worker. Refresh status or wait for automatic polling.",
    };
  }
  if (["building", "cancelling"].includes(stateLabel)) {
    return {
      stateLabel,
      imageRef,
      canInvoke,
      outcome: stateLabel === "building" ? "Build running" : "Cancelling build",
      message: stateLabel === "building"
        ? "A worker is building the function image now."
        : "Cancellation was requested and the worker is being asked to stop.",
    };
  }
  return {
    stateLabel,
    imageRef,
    canInvoke,
    outcome: "Not built yet",
    message: "Build a function to see whether it succeeds or fails.",
  };
}

function maybeNotifyBuildTerminal(summary) {
  if (!["built", "failed", "cancelled"].includes(summary.stateLabel)) return;
  const key = `${state.selectedFunction?.id || "new"}:${summary.stateLabel}:${summary.imageRef}`;
  if (state.lastBuildNoticeState === key) return;
  state.lastBuildNoticeState = key;
  if (summary.stateLabel === "built") notify("Build succeeded. The function can be invoked.");
  else if (summary.stateLabel === "failed") notify("Build failed. Check the build message and details.");
  else notify("Build cancelled.");
}

function toggleBuildDetails() {
  const box = el.buildStatusBox;
  const nextHidden = !box.hidden;
  box.hidden = nextHidden;
  el.toggleBuildDetailsButton.textContent = nextHidden ? "Show Details" : "Hide Details";
}

function scheduleBuildPoll(response) {
  clearTimeout(state.buildTimer);
  if (!response?.poll_after_seconds || response.is_terminal) return;
  state.buildTimer = setTimeout(() => refreshBuild(true).catch(showError), response.poll_after_seconds * 1000);
}

async function createToken(event) {
  event.preventDefault();
  requireFunction();
  const form = new FormData(event.currentTarget);
  const payload = { name: form.get("name") || "default" };
  if (form.get("expires_at")) payload.expires_at = new Date(form.get("expires_at")).toISOString();
  const response = await api(state.backendUrl, state.selectedFunction.links?.tokens || `/api/functions/${state.selectedFunction.id}/tokens/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
  renderRawToken(response.raw_token || "");
  await loadTokens();
  notify("Invocation token created. Copy the full token now; the table only keeps its prefix.");
  showOutput(response);
}

async function loadTokens() {
  requireFunction();
  const response = await api(state.backendUrl, state.selectedFunction.links?.tokens || `/api/functions/${state.selectedFunction.id}/tokens/`);
  renderTokens(response);
  showOutput(response);
}

function renderTokens(tokens) {
  el.tokensTableBody.innerHTML = "";
  for (const token of tokens || []) {
    const row = document.createElement("tr");
    row.innerHTML = `
      <td><input data-field="name" value="${escapeAttribute(token.name)}" /></td>
      <td>${escapeHtml(token.prefix)}</td>
      <td><input data-field="active" type="checkbox" ${token.is_active ? "checked" : ""} /></td>
      <td>${escapeHtml(formatDate(token.last_used_at))}</td>
      <td>
        <div class="table-actions">
          <button type="button" data-action="save">Save</button>
          <button type="button" data-action="rotate">Rotate</button>
          <button type="button" data-action="revoke">Revoke</button>
        </div>
      </td>
    `;
    row.querySelector('[data-action="save"]').addEventListener("click", () => updateToken(token.id, row).catch(showError));
    row.querySelector('[data-action="rotate"]').addEventListener("click", () => rotateToken(token.id).catch(showError));
    row.querySelector('[data-action="revoke"]').addEventListener("click", () => revokeToken(token.id).catch(showError));
    el.tokensTableBody.appendChild(row);
  }
}

function renderRawToken(rawToken) {
  el.rawTokenBox.textContent = rawToken || "Create or rotate a token to reveal the full fn_ token here.";
  el.copyRawTokenButton.disabled = !rawToken;
}

async function copyRawToken() {
  const token = el.rawTokenBox.textContent.trim();
  if (!token || !token.startsWith("fn_")) throw new Error("No full function token is visible.");
  await copyText(token);
  notify("Full invocation token copied.");
}

async function updateToken(tokenId, row) {
  const response = await api(state.backendUrl, `/api/functions/${state.selectedFunction.id}/tokens/${tokenId}/`, {
    method: "PATCH",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      name: row.querySelector('[data-field="name"]').value,
      is_active: row.querySelector('[data-field="active"]').checked,
    }),
  });
  await loadTokens();
  notify("Invocation token updated.");
  showOutput(response);
}

async function rotateToken(tokenId) {
  const response = await api(state.backendUrl, `/api/functions/${state.selectedFunction.id}/tokens/${tokenId}/rotate/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({}),
  });
  renderRawToken(response.raw_token || "");
  await loadTokens();
  notify("Invocation token rotated. Copy the new full token now; the old token no longer works.");
  showOutput(response);
}

async function revokeToken(tokenId) {
  const response = await api(state.backendUrl, `/api/functions/${state.selectedFunction.id}/tokens/${tokenId}/revoke/`, {
    method: "POST",
  });
  await loadTokens();
  notify("Invocation token revoked.");
  showOutput(response);
}

async function invokeFunction(event) {
  event.preventDefault();
  requireFunction();
  const form = new FormData(event.currentTarget);
  const mode = form.get("invoke_mode") || "async";
  const sync = syncInvocationEligibility();
  if (mode === "sync" && !sync.ok) throw new Error(sync.reason);
  const eventJson = parseJson(form.get("event") || "{}", "Event JSON");
  const files = form.getAll("input_files").filter((file) => file && file.name);
  let body;
  let headers = {};
  if (files.length) {
    body = new FormData();
    body.append("event", JSON.stringify(eventJson));
    for (const file of files) body.append("input_files", file);
  } else {
    body = JSON.stringify({ event: eventJson });
    headers = { "Content-Type": "application/json" };
  }
  const endpoint = mode === "sync"
    ? state.selectedFunction.links?.invoke_sync || `/api/functions/${state.selectedFunction.id}/invoke-sync/`
    : state.selectedFunction.links?.invoke || `/api/functions/${state.selectedFunction.id}/invoke/`;
  const response = await api(state.backendUrl, endpoint, {
    method: "POST",
    headers,
    body,
  });
  state.currentInvocation = response;
  state.invocationReadToken = response.read_token || "";
  renderInvocation(response);
  if (mode === "async" || response.status === "running" || !response.is_terminal) {
    scheduleInvocationPoll(response);
  }
  await loadInvocationHistory().catch(() => {});
  notify(mode === "sync" && response.is_terminal
    ? "Sync invocation completed."
    : mode === "sync"
      ? "Sync wait expired. The invocation is still running asynchronously."
      : "Invocation queued.");
  showOutput(response);
  renderInvocationMode();
}

async function refreshInvocation(auto) {
  if (!state.currentInvocation) throw new Error("No invocation selected.");
  const response = await api(state.backendUrl, state.currentInvocation.links?.self || `/api/invocations/${state.currentInvocation.id}/`, {
    headers: readTokenHeaders(),
  });
  state.currentInvocation = response;
  renderInvocation(response);
  if (auto) scheduleInvocationPoll(response);
  showOutput(response);
}

function scheduleInvocationPoll(response) {
  clearTimeout(state.invocationTimer);
  if (!response?.poll_after_seconds || response.is_terminal) return;
  state.invocationTimer = setTimeout(() => refreshInvocation(true).catch(showError), response.poll_after_seconds * 1000);
}

function renderInvocation(invocation) {
  el.invocationStatusBox.textContent = invocation ? JSON.stringify(invocation, null, 2) : "No invocation loaded.";
  el.resultStatus.value = invocation?.status || "";
  el.resultExitCode.value = invocation?.exit_code ?? "";
  el.resultBox.textContent = JSON.stringify(invocation?.result || {}, null, 2);
  el.stdoutBox.textContent = invocation?.stdout || "";
  el.stderrBox.textContent = invocation?.stderr || "";
  el.downloadInvocationButton.disabled = !invocation?.can_download;
}

async function loadInvocationHistory() {
  requireFunction();
  const response = await api(state.backendUrl, state.selectedFunction.links?.invocations || `/api/functions/${state.selectedFunction.id}/invocations/?limit=50`);
  renderHistory(response);
  showOutput(response);
}

function renderHistory(invocations) {
  el.historyTableBody.innerHTML = "";
  for (const invocation of invocations || []) {
    const row = document.createElement("tr");
    const tokenLabel = invocation.invocation_token_name
      ? `${invocation.invocation_token_name} / ${invocation.invocation_token_prefix || ""}`
      : "";
    row.innerHTML = `
      <td>${escapeHtml(invocation.status)}</td>
      <td>${escapeHtml(invocation.invocation_auth_type || "")}</td>
      <td>${escapeHtml(tokenLabel)}</td>
      <td>${escapeHtml(formatDate(invocation.started_at || invocation.queued_at))}</td>
      <td>
        <div class="table-actions">
          <button type="button" data-action="open">Open</button>
          <button type="button" data-action="zip">ZIP</button>
        </div>
      </td>
    `;
    row.querySelector('[data-action="open"]').addEventListener("click", () => {
      state.currentInvocation = invocation;
      renderInvocation(invocation);
      notify("Invocation loaded.");
    });
    row.querySelector('[data-action="zip"]').addEventListener("click", () => {
      state.currentInvocation = invocation;
      downloadCurrentInvocation().catch(showError);
    });
    el.historyTableBody.appendChild(row);
  }
}

async function downloadCurrentInvocation() {
  if (!state.currentInvocation) throw new Error("No invocation selected.");
  await downloadFile(
    state.backendUrl,
    state.currentInvocation.links?.download || `/api/invocations/${state.currentInvocation.id}/download/`,
    `invocation-${state.currentInvocation.request_id || state.currentInvocation.id}.zip`,
    readTokenHeaders(),
  );
}

function onContactDraft(event) {
  event.preventDefault();
  notify("Contact draft saved on this page.");
}

async function api(base, path, options = {}) {
  const auth = options.auth !== false;
  const retry = options.retry !== false;
  const headers = new Headers(options.headers || {});
  if (auth && state.access && !headers.has("Authorization")) {
    headers.set("Authorization", `Bearer ${state.access}`);
  }
  const response = await fetch(urlFor(base, path), { ...options, headers });
  if (response.status === 401 && auth && retry && state.refresh) {
    await refreshAccessToken();
    return api(base, path, { ...options, retry: false });
  }
  if (!response.ok) throw await responseError(response);
  if (response.status === 204) return null;
  const contentType = response.headers.get("content-type") || "";
  if (contentType.includes("application/json")) return response.json();
  return response.text();
}

async function refreshAccessToken() {
  const response = await api(state.userserviceUrl, "/api/auth/token/refresh/", {
    method: "POST",
    auth: false,
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ refresh: state.refresh }),
  });
  state.access = response.access || "";
  state.refresh = response.refresh || state.refresh;
  localStorage.setItem(keys.access, state.access);
  localStorage.setItem(keys.refresh, state.refresh);
  renderAuthState();
  return response;
}

async function downloadFile(base, path, fallbackName, extraHeaders = {}) {
  const headers = new Headers(extraHeaders);
  if (state.access && !headers.has("Authorization")) {
    headers.set("Authorization", `Bearer ${state.access}`);
  }
  let response = await fetch(urlFor(base, path), { headers });
  if (response.status === 401 && state.refresh) {
    await refreshAccessToken();
    headers.set("Authorization", `Bearer ${state.access}`);
    response = await fetch(urlFor(base, path), { headers });
  }
  if (!response.ok) throw await responseError(response);
  const blob = await response.blob();
  const objectUrl = URL.createObjectURL(blob);
  const link = document.createElement("a");
  link.href = objectUrl;
  link.download = filenameFromDisposition(response.headers.get("content-disposition")) || fallbackName;
  document.body.appendChild(link);
  link.click();
  link.remove();
  URL.revokeObjectURL(objectUrl);
}

function setBuildButtonState(isBusy) {
  el.buildButton.disabled = isBusy;
  el.buildButton.textContent = isBusy ? "Building..." : "Build Function";
  el.buildButton.setAttribute("aria-busy", String(isBusy));
}

async function withForm(event, handler, button = event.submitter) {
  event.preventDefault();
  await withButton(button, () => handler(event));
}

async function withButton(button, action) {
  const originalText = button?.textContent;
  if (button) {
    button.disabled = true;
    button.textContent = "Working...";
    button.setAttribute("aria-busy", "true");
  }
  try {
    return await action();
  } catch (error) {
    showError(error);
    notify("Something went wrong. Check the latest API response.");
  } finally {
    if (button) {
      button.disabled = false;
      button.textContent = originalText;
      button.setAttribute("aria-busy", "false");
    }
  }
}

function notify(message) {
  el.siteNotice.textContent = message || "";
  el.siteNotice.classList.toggle("is-visible", Boolean(message));
}

function showOutput(value) {
  el.apiOutputBox.textContent = typeof value === "string" ? value : JSON.stringify(value, null, 2);
}

function showError(error) {
  el.apiOutputBox.textContent = error?.message || String(error);
}

function selectedInputTypes(form) {
  const selected = form.getAll("input_type").filter(Boolean);
  const custom = String(form.get("custom_input_types") || "")
    .split(",")
    .map((item) => item.trim().toLowerCase())
    .filter(Boolean);
  return [...new Set([...selected, ...custom])];
}

function outputFileNames(value) {
  return String(value || "")
    .split(/\r?\n|,/)
    .map((item) => item.trim())
    .filter(Boolean);
}

function parseJson(value, label) {
  try {
    return JSON.parse(value);
  } catch {
    throw new Error(`${label} is not valid JSON.`);
  }
}

function requireFunction() {
  if (!state.selectedFunction) throw new Error("Build or select a function first.");
}

function readTokenHeaders() {
  if (state.access || !state.invocationReadToken) return {};
  return { "X-Invocation-Read-Token": state.invocationReadToken };
}

function urlFor(base, path) {
  if (/^https?:\/\//i.test(path)) return path;
  return `${String(base).replace(/\/+$/, "")}${path.startsWith("/") ? path : `/${path}`}`;
}

async function responseError(response) {
  const contentType = response.headers.get("content-type") || "";
  const body = contentType.includes("application/json")
    ? JSON.stringify(await response.json(), null, 2)
    : await response.text();
  return new Error(`${response.status} ${response.statusText}\n${body}`);
}

function readStoredJson(key, fallback) {
  try {
    return JSON.parse(localStorage.getItem(key) || "");
  } catch {
    return fallback;
  }
}

function formatDate(value) {
  if (!value) return "";
  const date = new Date(value);
  if (Number.isNaN(date.getTime())) return "";
  return date.toLocaleString();
}

function filenameFromDisposition(value) {
  const match = /filename="?([^"]+)"?/i.exec(value || "");
  return match ? match[1] : "";
}

function escapeHtml(value) {
  return String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

function escapeAttribute(value) {
  return escapeHtml(value).replaceAll("`", "&#096;");
}

function buildSourceZip(files) {
  const encoder = new TextEncoder();
  const entries = Object.entries(files).map(([name, text]) => {
    const data = encoder.encode(String(text ?? ""));
    return { name, nameBytes: encoder.encode(name), data, crc: crc32(data) };
  });
  const localParts = [];
  const centralParts = [];
  let offset = 0;
  const { dosDate, dosTime } = dosDateTime(new Date());

  for (const entry of entries) {
    const local = header(30);
    write32(local, 0, 0x04034b50);
    write16(local, 4, 20);
    write16(local, 6, 0);
    write16(local, 8, 0);
    write16(local, 10, dosTime);
    write16(local, 12, dosDate);
    write32(local, 14, entry.crc);
    write32(local, 18, entry.data.length);
    write32(local, 22, entry.data.length);
    write16(local, 26, entry.nameBytes.length);
    write16(local, 28, 0);
    localParts.push(local, entry.nameBytes, entry.data);

    const central = header(46);
    write32(central, 0, 0x02014b50);
    write16(central, 4, 20);
    write16(central, 6, 20);
    write16(central, 8, 0);
    write16(central, 10, 0);
    write16(central, 12, dosTime);
    write16(central, 14, dosDate);
    write32(central, 16, entry.crc);
    write32(central, 20, entry.data.length);
    write32(central, 24, entry.data.length);
    write16(central, 28, entry.nameBytes.length);
    write16(central, 30, 0);
    write16(central, 32, 0);
    write16(central, 34, 0);
    write16(central, 36, 0);
    write32(central, 38, 0);
    write32(central, 42, offset);
    centralParts.push(central, entry.nameBytes);
    offset += local.length + entry.nameBytes.length + entry.data.length;
  }

  const centralSize = centralParts.reduce((sum, part) => sum + part.length, 0);
  const end = header(22);
  write32(end, 0, 0x06054b50);
  write16(end, 8, entries.length);
  write16(end, 10, entries.length);
  write32(end, 12, centralSize);
  write32(end, 16, offset);
  write16(end, 20, 0);
  return new Blob([...localParts, ...centralParts, end], { type: "application/zip" });
}

function header(size) {
  return new Uint8Array(size);
}

function write16(buffer, offset, value) {
  new DataView(buffer.buffer).setUint16(offset, value, true);
}

function write32(buffer, offset, value) {
  new DataView(buffer.buffer).setUint32(offset, value >>> 0, true);
}

function dosDateTime(date) {
  const year = Math.max(1980, date.getFullYear());
  return {
    dosTime: (date.getHours() << 11) | (date.getMinutes() << 5) | Math.floor(date.getSeconds() / 2),
    dosDate: ((year - 1980) << 9) | ((date.getMonth() + 1) << 5) | date.getDate(),
  };
}

const crcTable = (() => {
  const table = new Uint32Array(256);
  for (let n = 0; n < 256; n += 1) {
    let c = n;
    for (let k = 0; k < 8; k += 1) {
      c = c & 1 ? 0xedb88320 ^ (c >>> 1) : c >>> 1;
    }
    table[n] = c >>> 0;
  }
  return table;
})();

function crc32(bytes) {
  let crc = 0xffffffff;
  for (const byte of bytes) {
    crc = crcTable[(crc ^ byte) & 0xff] ^ (crc >>> 8);
  }
  return (crc ^ 0xffffffff) >>> 0;
}
