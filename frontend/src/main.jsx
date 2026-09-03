import React, { useEffect, useMemo, useRef, useState } from "react";
import { createRoot } from "react-dom/client";
import "./styles.css";

const STORAGE = {
  access: "serverless.react.access",
  refresh: "serverless.react.refresh",
  backend: "serverless.react.backend",
  userservice: "serverless.react.userservice",
};
const serviceUrl = (port) => {
  if (typeof window === "undefined") return `http://localhost:${port}`;
  if (!window.location.port || ["80", "443"].includes(window.location.port)) {
    return window.location.origin;
  }
  return `${window.location.protocol}//${window.location.hostname}:${port}`;
};
const BACKEND = localStorage.getItem(STORAGE.backend) || serviceUrl(8000);
const USERSERVICE = localStorage.getItem(STORAGE.userservice) || serviceUrl(8100);
const PYTHON_STARTER = `def main(event, context):\n    name = event.get("name", "world")\n    print(f"hello, {name}")\n    return {"message": f"hello, {name}"}\n`;
const EMPTY_DRAFT = {
  name: "", description: "", invoke_access: "private", handler: "handler.main",
  code: PYTHON_STARTER, requirements: "", config: "{}", inputTypes: [], inputMaxFiles: 1,
  inputMaxSize: 10, inputMaxTotal: 10, outputs: "", outputMaxFiles: 5, outputMaxSize: 10, outputMaxTotal: 10,
  timeoutSeconds: 60,
};

function App() {
  const [access, setAccess] = useState(localStorage.getItem(STORAGE.access) || "");
  const [refresh, setRefresh] = useState(localStorage.getItem(STORAGE.refresh) || "");
  const [user, setUser] = useState(null);
  const [screen, setScreen] = useState("landing");
  const [functions, setFunctions] = useState([]);
  const [selected, setSelected] = useState(null);
  const [build, setBuild] = useState(null);
  const [notice, setNotice] = useState(null);
  const [busy, setBusy] = useState(false);

  const session = { access, refresh, setAccess, setRefresh, setUser, setScreen };
  const api = useApi(session, (message, kind = "error") => setNotice({ message, kind }));

  useEffect(() => { restoreSession(); }, []);
  useEffect(() => {
    if (screen === "dashboard" && access) loadFunctions();
  }, [screen, access]);
  useEffect(() => {
    if (!build?.poll_after_seconds || build.is_terminal) return undefined;
    const id = window.setTimeout(() => refreshBuild(), build.poll_after_seconds * 1000);
    return () => window.clearTimeout(id);
  }, [build]);

  async function restoreSession() {
    if (!access && !refresh) return;
    try {
      const me = await api.userservice("/api/auth/me/");
      setUser(me); setScreen("dashboard");
    } catch { logout(false); }
  }
  async function loadFunctions() {
    try { setFunctions(await api.backend("/api/functions/")); }
    catch (error) { setNotice({ message: error.message, kind: "error" }); }
  }
  async function openFunction(fn) {
    setSelected(fn); setBuild(null); setScreen("function");
    try {
      const [detail, status] = await Promise.all([
        api.backend(`/api/functions/${fn.id}/`), api.backend(`/api/functions/${fn.id}/build-status/`),
      ]);
      setSelected(detail); setBuild(status);
    } catch (error) { setNotice({ message: error.message, kind: "error" }); }
  }
  async function refreshBuild() {
    if (!selected) return;
    try { setBuild(await api.backend(`/api/functions/${selected.id}/build-status/`)); }
    catch (error) { setNotice({ message: error.message, kind: "error" }); }
  }
  function logout(callApi = true) {
    if (callApi && access) api.userservice("/api/auth/logout/", { method: "POST", auth: false }).catch(() => {});
    localStorage.removeItem(STORAGE.access); localStorage.removeItem(STORAGE.refresh);
    setAccess(""); setRefresh(""); setUser(null); setSelected(null); setScreen("landing");
  }
  const nav = <Header user={user} screen={screen} onHome={() => setScreen("landing")} onWorkspace={() => setScreen(access ? "dashboard" : "auth")} onGuide={() => setScreen("tutorial")} onLogin={() => setScreen("auth")} onLogout={logout} />;

  return <>
    {nav}
    {notice && <Toast notice={notice} onClose={() => setNotice(null)} />}
    {screen === "landing" && <Landing onStart={() => setScreen(access ? "dashboard" : "auth")} onGuide={() => setScreen("tutorial")} />}
    {screen === "tutorial" && <Tutorial onStart={() => setScreen(access ? "dashboard" : "auth")} />}
    {screen === "auth" && <Auth api={api} session={session} onDone={(newUser) => { setUser(newUser); setScreen("dashboard"); }} />}
    {screen === "dashboard" && <Dashboard functions={functions} onRefresh={loadFunctions} onNew={() => { setSelected(null); setBuild(null); setScreen("wizard"); }} onOpen={openFunction} />}
    {screen === "wizard" && <FunctionWizard api={api} existing={selected} onCancel={() => setScreen(selected ? "function" : "dashboard")} onSaved={async (fn, summary) => { setSelected(fn); setBuild(summary); await loadFunctions(); setNotice({ message: "Build queued. We will keep the status current here.", kind: "success" }); setScreen("function"); }} />}
    {screen === "function" && selected && <FunctionHub api={api} fn={selected} build={build} onEdit={() => setScreen("wizard")} onRefresh={refreshBuild} onBack={() => setScreen("dashboard")} onNotice={setNotice} />}
  </>;
}

function Header({ user, screen, onHome, onWorkspace, onGuide, onLogin, onLogout }) {
  return <header className="topbar"><button className="wordmark" onClick={onHome}>Fleeting Circus<span>.</span></button><nav><button onClick={onHome}>Home</button><button onClick={onWorkspace}>Workspace</button><button onClick={onGuide}>How it works</button></nav><div className="account">{user ? <><span>{user.username}</span><button className="button quiet" onClick={onLogout}>Log out</button></> : <button className="button" onClick={onLogin}>{screen === "auth" ? "Sign in" : "Get started"}</button>}</div></header>;
}
function Landing({ onStart, onGuide }) {
  return <main className="landing"><section className="hero"><div className="hero-copy"><p className="eyebrow">A joyful home for tiny Python services</p><h1>Ship a function into the clouds.</h1><p className="lede">Paste your Python handler, choose how people can call it, build once, then invoke it from the workspace or your own apps.</p><div className="hero-actions"><button className="button primary" onClick={onStart}>Start building <span>→</span></button><button className="button quiet" onClick={onGuide}>Learn the platform</button></div></div><figure className="hero-art"><img src="/fleeting-circus-hero.png" alt="A colorful circus tent floating through soft clouds" /><figcaption>Functions, builds, tokens and results in one light workspace.</figcaption></figure></section><section id="guide" className="flow-strip"><FlowCard number="01" title="Shape it" text="Name the function, paste code, and declare the files it can use."/><FlowCard number="02" title="Build it" text="Install dependencies once and prepare a callable version."/><FlowCard number="03" title="Run it" text="Send JSON or files, follow the result, download artifacts."/></section></main>;
}
function FlowCard({ number, title, text }) { return <article className="flow-card"><span>{number}</span><h2>{title}</h2><p>{text}</p></article>; }

const TUTORIAL_TOPICS = [
  {
    id: "platform",
    label: "Understand the platform",
    mission: "Scout",
    title: "What is this platform?",
    summary: "Learn what you can do here before writing code.",
    steps: [
      "This platform turns a Python function into an HTTP API.",
      "You paste your code, list your dependencies, choose who can call it, and press build.",
      "After the build succeeds, you can run the function from the dashboard or from an external app.",
      "A request sends JSON and, for async calls, optional input files.",
      "A response gives back the value your function returned and links to any files it produced.",
    ],
    checkpoint: "Think of it as: Python function in, callable API out.",
  },
  {
    id: "function",
    label: "Write a function",
    mission: "Builder",
    title: "What is a function?",
    summary: "A function is a Python handler plus a contract.",
    steps: [
      "The handler is usually handler.main.",
      "The platform imports handler.py, finds main, then calls main(event, context).",
      "event is the JSON object from the request.",
      "context is platform metadata that can grow later.",
      "The function should return JSON-serializable data.",
    ],
    code: `def main(event, context):\n    name = event.get("name", "world")\n    return {"message": f"hello, {name}"}`,
    checkpoint: "The smallest useful function accepts event, context and returns a JSON object.",
  },
  {
    id: "dependencies",
    label: "Add dependencies",
    mission: "Loadout",
    title: "How do dependencies work?",
    summary: "Dependencies are declared in requirements.txt during build.",
    steps: [
      "Paste packages into requirements.txt exactly like a normal Python project.",
      "The platform installs those packages when you press build.",
      "Changing dependencies means editing the function and building again.",
      "Heavy dependencies make builds slower, so keep the list as small as you can.",
      "The function does not install packages during invocation.",
    ],
    code: `numpy==2.2.0\npillow==11.0.0`,
    checkpoint: "Runtime should be fast because dependency work belongs to build time.",
  },
  {
    id: "sync",
    label: "Use sync calls",
    mission: "Sprint",
    title: "Synchronous invocation",
    summary: "Use sync when the caller wants a quick JSON result immediately.",
    steps: [
      "The caller sends JSON to /invoke-sync/.",
      "The platform waits for the function for a short amount of time.",
      "If the function finishes in time, the same HTTP response contains the returned JSON.",
      "Sync calls do not accept input files.",
      "Sync calls are only available when the function declares no output files.",
    ],
    code: `POST http://localhost:8000/api/functions/76/invoke-sync/?response_mode=simple\nContent-Type: application/json\n\n{\n  "event": { "name": "Ada" }\n}\n\n200 OK\n{\n  "status": "succeeded",\n  "result": { "message": "hello, Ada" },\n  "output_files": []\n}`,
    checkpoint: "Use sync for quick JSON-only work, like validation, scoring, formatting, or small calculations.",
  },
  {
    id: "async",
    label: "Use async calls",
    mission: "Expedition",
    title: "Asynchronous invocation",
    summary: "Use async when the function may take longer or needs files.",
    steps: [
      "The caller sends JSON, and optionally files, to /invoke/.",
      "The first response confirms that the invocation was accepted.",
      "The caller polls the invocation URL to see whether it finished.",
      "When it is finished, the caller can read the result and download the invocation ZIP.",
      "Async is the right mode for images, PDFs, generated reports, or slower processing.",
    ],
    code: `POST http://localhost:8000/api/functions/76/invoke/?response_mode=simple\nContent-Type: application/json\nX-Function-Token: fn_your_full_token_here\n\n{\n  "event": { "name": "Ada" }\n}\n\n202 Accepted\n{\n  "id": 123,\n  "status": "queued",\n  "poll_after_seconds": 1,\n  "read_token": "inv_read_token_here"\n}\n\nGET http://localhost:8000/api/invocations/123/?response_mode=simple\nX-Invocation-Read-Token: inv_read_token_here\n\n200 OK\n{\n  "status": "succeeded",\n  "result": { "message": "hello, Ada" },\n  "output_files": [\n    { "path": "report.txt", "download_url": "/api/invocations/123/outputs/7/download/" }\n  ]\n}`,
    checkpoint: "Use async when the caller should receive an invocation id first and collect the result later.",
  },
  {
    id: "capabilities",
    label: "Manage functions",
    mission: "Control",
    title: "What can you do with functions?",
    summary: "A function is not just code. It has lifecycle, access and history.",
    steps: [
      "Create a function and choose private, token or public access.",
      "Edit code, requirements and file contracts, then queue a new build.",
      "Watch build status until the active version is ready.",
      "Create, rotate and revoke invocation tokens for token-protected functions.",
      "Run test invocations and review invocation history.",
      "Download an invocation ZIP while it is still retained.",
    ],
    checkpoint: "The frontend should guide the owner from create to build to invoke without needing raw API knowledge.",
  },
  {
    id: "apis",
    label: "Use the APIs",
    mission: "Integrate",
    title: "What APIs exist?",
    summary: "These are the core frontend-facing and caller-facing routes.",
    steps: [
      "Auth lives in userservice: register, login, refresh, logout and me.",
      "Function management lives in backend: create functions, replace source, build, status and tokens.",
      "Invocation APIs start work: async invoke and sync invoke.",
      "Result APIs read work: invocation detail, output listing and invocation ZIP download.",
      "The dashboard uses the same public user-facing APIs that external clients can use.",
    ],
    code: `POST /api/functions/{id}/invoke/\nPOST /api/functions/{id}/invoke-sync/\nGET  /api/invocations/{id}/?response_mode=simple\nGET  /api/invocations/{id}/download/`,
    checkpoint: "Frontend users should see friendly flows, but integration users need these URLs.",
  },
  {
    id: "request",
    label: "See a request",
    mission: "Launch",
    title: "What does a request look like?",
    summary: "A caller sends JSON, optional auth, and sometimes files.",
    steps: [
      "Public functions need no auth header.",
      "Token functions use X-Function-Token with the full fn_ token.",
      "Private functions use Authorization: Bearer with the owner JWT.",
      "JSON-only calls use application/json.",
      "File calls use multipart form data with event and input_files.",
    ],
    code: `POST http://localhost:8000/api/functions/76/invoke-sync/?response_mode=simple\nContent-Type: application/json\n\n{\n  "event": { "name": "Ada" }\n}`,
    checkpoint: "The response mode can be simple for callers and advanced for dashboard diagnostics.",
  },
];

function Tutorial({ onStart }) {
  const [active, setActive] = useState(TUTORIAL_TOPICS[0].id);
  const topic = TUTORIAL_TOPICS.find((item) => item.id === active) || TUTORIAL_TOPICS[0];
  const done = TUTORIAL_TOPICS.findIndex((item) => item.id === active) + 1;
  return <main className="tutorial-page"><section className="tutorial-hero"><div><p className="eyebrow">How it works</p><h1>Choose your next lesson.</h1><p className="lede">Pick the mission that matches what you are trying to understand. Each page gives you the practical model, the platform behavior, and a checkpoint before you move on.</p></div><div className="tutorial-score"><span>Progress</span><strong>{done}/{TUTORIAL_TOPICS.length}</strong><p>{Math.round((done / TUTORIAL_TOPICS.length) * 100)}% mapped</p></div></section><section className="tutorial-layout"><nav className="mission-map">{TUTORIAL_TOPICS.map((item, index) => <button key={item.id} className={item.id === active ? "active" : ""} onClick={() => setActive(item.id)}><span>{String(index + 1).padStart(2, "0")}</span><strong>{item.label}</strong><small>{item.mission}</small></button>)}</nav><article className="lesson-card"><p className="mission">Mission {topic.mission} <span>{topic.label}</span></p><h2>{topic.title}</h2><p className="hint">{topic.summary}</p><ol className="lesson-steps">{topic.steps.map((step) => <li key={step}>{step}</li>)}</ol>{topic.code && <pre>{topic.code}</pre>}<section className="checkpoint"><span>Checkpoint</span><p>{topic.checkpoint}</p></section><div className="wizard-actions"><button className="button quiet" onClick={() => setActive(TUTORIAL_TOPICS[Math.max(0, done - 2)].id)} disabled={done === 1}>Previous</button>{done < TUTORIAL_TOPICS.length ? <button className="button primary" onClick={() => setActive(TUTORIAL_TOPICS[done].id)}>Next mission →</button> : <button className="button primary" onClick={onStart}>Open workspace →</button>}</div></article></section></main>;
}

function Auth({ api, session, onDone }) {
  const [mode, setMode] = useState("login"); const [form, setForm] = useState({ username: "", password: "", first_name: "", last_name: "", email: "" }); const [error, setError] = useState(""); const [busy, setBusy] = useState(false);
  const set = (key) => (e) => setForm({ ...form, [key]: e.target.value });
  async function submit(e) { e.preventDefault(); setBusy(true); setError(""); try { const endpoint = mode === "login" ? "/api/auth/token/" : "/api/auth/register/"; const body = mode === "login" ? { username: form.username, password: form.password } : form; const response = await api.userservice(endpoint, { method: "POST", auth: false, headers: { "Content-Type": "application/json" }, body: JSON.stringify(body) }); localStorage.setItem(STORAGE.access, response.access); localStorage.setItem(STORAGE.refresh, response.refresh); session.setAccess(response.access); session.setRefresh(response.refresh); onDone(response.user); } catch (err) { setError(err.message); } finally { setBusy(false); } }
  return <main className="auth-page"><form className="auth-card" onSubmit={submit}><p className="eyebrow">{mode === "login" ? "Welcome back" : "First, your account"}</p><h1>{mode === "login" ? "Sign in to your workspace." : "Create your workspace."}</h1>{mode === "register" && <div className="two"><Field label="First name" value={form.first_name} onChange={set("first_name")} /><Field label="Last name" value={form.last_name} onChange={set("last_name")} /></div>}<Field label="Username" value={form.username} onChange={set("username")} required />{mode === "register" && <Field label="Email" type="email" value={form.email} onChange={set("email")} />}<Field label="Password" type="password" value={form.password} onChange={set("password")} required />{error && <p className="form-error">{error}</p>}<button className="button primary full" disabled={busy}>{busy ? "Working…" : mode === "login" ? "Sign in" : "Create account"}</button><button type="button" className="text-button" onClick={() => setMode(mode === "login" ? "register" : "login")}>{mode === "login" ? "Need an account? Sign up" : "Already have an account? Sign in"}</button></form></main>;
}
function Dashboard({ functions, onRefresh, onNew, onOpen }) { return <main className="workspace"><section className="page-heading"><div><p className="eyebrow">Your workspace</p><h1>Functions</h1><p>Each function has its own source, build, endpoint, tokens, and invocation history.</p></div><button className="button primary" onClick={onNew}>New function <span>+</span></button></section>{functions.length ? <section className="function-grid">{functions.map((fn) => <button className="function-card" key={fn.id} onClick={() => onOpen(fn)}><div><span className="dot" data-status={fn.build_status} /><span className="mono">{fn.slug || fn.name}</span></div><h2>{fn.name}</h2><p>{fn.description || "No description yet."}</p><footer><Status value={fn.build_status || "not built"} /><span>Open →</span></footer></button>)}</section> : <section className="empty"><span className="empty-mark">+</span><h2>Your first function starts here.</h2><p>The guided builder will take you from function idea to a buildable endpoint.</p><button className="button primary" onClick={onNew}>Create function</button></section>}<button className="refresh-link" onClick={onRefresh}>Refresh workspace</button></main>; }

function FunctionWizard({ api, existing, onCancel, onSaved }) {
  const [step, setStep] = useState(0); const [draft, setDraft] = useState(() => draftFromFunction(existing)); const [busy, setBusy] = useState(false); const [sourceLoading, setSourceLoading] = useState(Boolean(existing)); const [error, setError] = useState("");
  const steps = ["Function", "Code", "Contract", "Build"];
  const update = (key, value) => setDraft((old) => ({ ...old, [key]: value }));
  useEffect(() => { let alive = true; async function loadSource() { if (!existing) { setSourceLoading(false); return; } setSourceLoading(true); try { const source = await api.backend(existing.links?.source || `/api/functions/${existing.id}/source/`); if (!alive) return; const config = source.config || {}; setDraft((old) => ({ ...old, code: source.code ?? old.code, requirements: source.requirements ?? old.requirements, handler: source.handler || old.handler, config: JSON.stringify(config, null, 2), timeoutSeconds: Number(config.timeout_seconds || old.timeoutSeconds || 60) })); } catch { if (alive) setError("Could not load the current source. Paste the full replacement before building."); } finally { if (alive) setSourceLoading(false); } } loadSource(); return () => { alive = false; }; }, [existing?.id]);
  function validStep() { if (step === 0) return draft.name.trim() ? "" : "Give the function a name before continuing."; if (step === 1) return draft.code.trim() ? "" : "Paste a Python handler before continuing."; if (step === 2) { try { JSON.parse(draft.config || "{}"); } catch { return "Config JSON must be valid JSON."; } const timeout = Number(draft.timeoutSeconds); if (!Number.isInteger(timeout) || timeout < 1 || timeout > 300) return "Execution timeout must be a whole number from 1 to 300 seconds."; return ""; } return ""; }
  function next() { const message = validStep(); if (message) setError(message); else { setError(""); setStep(Math.min(3, step + 1)); } }
  async function buildFunction() { const message = validStep(); if (message) { setError(message); return; } setBusy(true); setError(""); try { const metadata = { name: draft.name.trim(), description: draft.description.trim(), invoke_access: draft.invoke_access }; const fn = existing ? await api.backend(`/api/functions/${existing.id}/`, { method: "PATCH", headers: jsonHeaders(), body: JSON.stringify(metadata) }) : await api.backend("/api/functions/", { method: "POST", headers: jsonHeaders(), body: JSON.stringify(metadata) }); const config = withRuntimeConfig(JSON.parse(draft.config || "{}"), draft); const files = { "handler.py": draft.code, "requirements.txt": draft.requirements, "config.json": JSON.stringify(config, null, 2) }; const body = new FormData(); body.append("source_bundle", new File([buildZip(files)], "function.zip", { type: "application/zip" })); body.append("runtime", "python3.13"); body.append("handler", draft.handler || "handler.main"); body.append("config", JSON.stringify(config)); body.append("invocation_input_mime_types", JSON.stringify(draft.inputTypes)); body.append("declared_output_files", JSON.stringify(lines(draft.outputs))); [["invocation_input_max_files", draft.inputMaxFiles], ["invocation_input_max_size_mb", draft.inputMaxSize], ["invocation_input_max_total_size_mb", draft.inputMaxTotal], ["invocation_output_max_files", draft.outputMaxFiles], ["invocation_output_max_file_size_mb", draft.outputMaxSize], ["invocation_output_max_total_size_mb", draft.outputMaxTotal]].forEach(([key, value]) => body.append(key, String(value))); const summary = await api.backend(fn.links?.source || `/api/functions/${fn.id}/source/`, { method: "POST", body }); onSaved(fn, summary); } catch (err) { setError(err.message); } finally { setBusy(false); } }
  return <main className="workspace wizard"><button className="back-link" onClick={onCancel}>← Back to functions</button><section className="wizard-header"><div><p className="eyebrow">{existing ? "Update function" : "New function"}</p><h1>{existing ? existing.name : "Build something small."}</h1><p>One focused decision at a time. Nothing is sent until the final build step.</p></div><div className="progress-label">Step {step + 1} of {steps.length}</div></section><ol className="stepper">{steps.map((title, index) => <li key={title} className={index === step ? "current" : index < step ? "done" : ""}><button onClick={() => index <= step && setStep(index)}><span>{index < step ? "✓" : index + 1}</span>{title}</button></li>)}</ol><section className="wizard-card">{sourceLoading && <p className="loading-inline">Loading current source…</p>}{step === 0 && <Basics draft={draft} update={update} />}{step === 1 && <CodeStep draft={draft} update={update} isReplacement={Boolean(existing)} sourceLoading={sourceLoading} />}{step === 2 && <ContractStep draft={draft} update={update} />}{step === 3 && <Review draft={draft} />}{error && <p className="form-error">{error}</p>}<div className="wizard-actions"><button className="button quiet" onClick={step === 0 ? onCancel : () => setStep(step - 1)}>{step === 0 ? "Cancel" : "Back"}</button>{step < 3 ? <button className="button primary" disabled={sourceLoading} onClick={next}>Continue →</button> : <button className="button primary" disabled={busy || sourceLoading} onClick={buildFunction}>{busy ? "Queueing build…" : "Queue build →"}</button>}</div></section></main>;
}
function Basics({ draft, update }) { return <div className="step-content"><p className="mission">Mission 01 <span>Function identity</span></p><h2>What are you making?</h2><p className="hint">A good name and access rule make this endpoint easy to identify later.</p><div className="two"><Field label="Function name" value={draft.name} onChange={(e) => update("name", e.target.value)} placeholder="image-resizer" required /><Field label="Handler" value={draft.handler} onChange={(e) => update("handler", e.target.value)} placeholder="handler.main" /></div><Field label="Description" value={draft.description} onChange={(e) => update("description", e.target.value)} placeholder="What should this function do?"/><fieldset><legend>Who can invoke it?</legend><div className="choice-grid">{[["private", "Private", "Only your workspace JWT can invoke it."], ["token", "Token", "People with a function token can invoke it."], ["public", "Public", "Anyone can invoke its public endpoint."]].map(([value, title, text]) => <label className={draft.invoke_access === value ? "choice selected" : "choice"} key={value}><input type="radio" checked={draft.invoke_access === value} onChange={() => update("invoke_access", value)} /><strong>{title}</strong><span>{text}</span></label>)}</div></fieldset></div>; }
function CodeStep({ draft, update, isReplacement, sourceLoading }) { const numbers = useMemo(() => Array.from({ length: Math.max(1, draft.code.split("\n").length) }, (_, i) => i + 1).join("\n"), [draft.code]); return <div className="step-content"><p className="mission">Mission 02 <span>Function code</span></p><h2>{isReplacement ? "Edit the current handler." : "Give it a handler."}</h2><p className="hint">{isReplacement ? "The editor loads the current handler.py and requirements.txt. Building will replace the current source with what is shown here." : "The platform packages these as handler.py and requirements.txt."}</p><div className="editor-grid"><label className="editor-field"><span>handler.py</span><div className="code-editor"><pre>{numbers}</pre><textarea spellCheck="false" disabled={sourceLoading} value={draft.code} onChange={(e) => update("code", e.target.value)} /></div></label><label className="editor-field"><span>requirements.txt <small>Optional</small></span><textarea className="requirements" spellCheck="false" disabled={sourceLoading} value={draft.requirements} placeholder="numpy\npillow" onChange={(e) => update("requirements", e.target.value)} /></label></div></div>; }
function ContractStep({ draft, update }) { const toggle = (type) => update("inputTypes", draft.inputTypes.includes(type) ? draft.inputTypes.filter((item) => item !== type) : [...draft.inputTypes, type]); return <div className="step-content contract-step"><p className="mission">Mission 03 <span>Input, output and runtime contract</span></p><h2>Set the boundaries.</h2><p className="hint">Tell callers what the function can receive, what it can publish, and how long the user code may run.</p><div className="contract-stack"><section className="contract-panel runtime-panel"><header><div><h3>Execution timeout</h3><p>This timer starts when your function code begins running. Queueing, scheduling, network delay, input upload and result download do not count.</p></div><span>Runtime</span></header><NumberField label="Timeout seconds" value={draft.timeoutSeconds} min={1} max={300} onChange={(v) => update("timeoutSeconds", v)} /><p className="field-note">Allowed range: 1 to 300 seconds. The worker stops the function if it exceeds this value.</p></section><section className="contract-panel"><header><div><h3>Input files</h3><p>Optional files sent with an asynchronous invocation.</p></div><span>Async only</span></header><div className="check-grid contract-checks">{[["image/png", "PNG"], ["image/jpeg", "JPEG"], ["application/pdf", "PDF"], ["text/plain", "Text"], ["application/json", "JSON"]].map(([value, label]) => <label key={value}><input type="checkbox" checked={draft.inputTypes.includes(value)} onChange={() => toggle(value)} /> {label}</label>)}</div><Limits prefix="input" draft={draft} update={update} /></section><section className="contract-panel"><header><div><h3>Output files</h3><p>One expected filename per line. Other files will not be published.</p></div><span>Optional</span></header><label className="output-list-field"><span>Expected output files</span><textarea value={draft.outputs} placeholder="report.txt\npreview.png" onChange={(e) => update("outputs", e.target.value)} /></label><Limits prefix="output" draft={draft} update={update} /></section></div><label className="config-field">Advanced Config JSON<small>Optional values for context.config. The timeout field above is saved here as timeout_seconds.</small><textarea value={draft.config} onChange={(e) => update("config", e.target.value)} /></label></div>; }
function Limits({ prefix, draft, update }) { const capital = prefix === "input" ? "Input" : "Output"; return <div className="limits"><NumberField label="Max files" value={draft[`${prefix}MaxFiles`]} onChange={(v) => update(`${prefix}MaxFiles`, v)} /><NumberField label="Max file MB" value={draft[`${prefix}MaxSize`]} onChange={(v) => update(`${prefix}MaxSize`, v)} /><NumberField label="Max total MB" value={draft[`${prefix}MaxTotal`]} onChange={(v) => update(`${prefix}MaxTotal`, v)} /></div>; }
function Review({ draft }) { return <div className="step-content"><p className="mission">Mission 04 <span>Review and build</span></p><h2>Ready to queue a build?</h2><p className="hint">The source is kept, then the platform prepares a callable version. You can keep using the current built version while an update is building.</p><dl className="review"><div><dt>Name</dt><dd>{draft.name}</dd></div><div><dt>Access</dt><dd>{draft.invoke_access}</dd></div><div><dt>Handler</dt><dd>{draft.handler}</dd></div><div><dt>Execution timeout</dt><dd>{draft.timeoutSeconds} seconds of function runtime</dd></div><div><dt>Dependencies</dt><dd>{draft.requirements ? `${draft.requirements.split("\n").filter(Boolean).length} package(s)` : "None"}</dd></div><div><dt>Input types</dt><dd>{draft.inputTypes.length ? draft.inputTypes.join(", ") : "JSON only"}</dd></div><div><dt>Output files</dt><dd>{lines(draft.outputs).length ? lines(draft.outputs).join(", ") : "No files"}</dd></div></dl></div>; }

function FunctionHub({ api, fn, build, onEdit, onRefresh, onBack, onNotice }) {
  const [tab, setTab] = useState("overview"); const [tokens, setTokens] = useState([]); const [history, setHistory] = useState([]);
  useEffect(() => { if (tab === "access") loadTokens(); if (tab === "runs") loadHistory(); }, [tab, fn.id]);
  async function loadTokens() { try { setTokens(await api.backend(fn.links?.tokens || `/api/functions/${fn.id}/tokens/`)); } catch (e) { onNotice({ message: e.message, kind: "error" }); } }
  async function loadHistory() { try { setHistory(await api.backend(fn.links?.invocations || `/api/functions/${fn.id}/invocations/?limit=50`)); } catch (e) { onNotice({ message: e.message, kind: "error" }); } }
  return <main className="workspace"><button className="back-link" onClick={onBack}>← All functions</button><section className="function-title"><div><div className="label-row"><Status value={build?.frontend_state || fn.build_status || "not built"} /><span className="mono">{fn.slug}</span></div><h1>{fn.name}</h1><p>{fn.description || "No description yet."}</p></div><div className="title-actions"><button className="button quiet" onClick={onEdit}>Edit function</button><button className="button" onClick={onRefresh}>Refresh status</button></div></section><BuildBanner build={build} onRefresh={onRefresh} /><nav className="tabs">{[["overview", "Overview"], ["run", "Run"], ["runs", "Invocation history"], ["access", "Access tokens"], ["guide", "API guide"]].map(([value, label]) => <button className={tab === value ? "active" : ""} onClick={() => setTab(value)} key={value}>{label}</button>)}</nav>{tab === "overview" && <Overview fn={fn} build={build} onRun={() => setTab("run")} />}{tab === "run" && <RunWizard api={api} fn={fn} build={build} onNotice={onNotice} />}{tab === "runs" && <History api={api} fn={fn} history={history} reload={loadHistory} />}{tab === "access" && <Tokens api={api} fn={fn} tokens={tokens} reload={loadTokens} onNotice={onNotice} />}{tab === "guide" && <ApiGuide fn={fn} build={build} />}</main>;
}
function BuildBanner({ build, onRefresh }) { const state = build?.frontend_state || "not_built"; const ready = build?.can_invoke; return <section className="build-banner" data-state={state}><div><p>Build status</p><h2>{state.replaceAll("_", " ")}</h2><span>{ready ? "This endpoint is ready to run." : state === "failed" ? "The last build failed. Edit the code and queue another build." : "The platform is preparing this function."}</span></div><button className="button quiet" onClick={onRefresh}>Refresh</button></section>; }
function Overview({ fn, build, onRun }) { return <section className="overview"><article className="endpoint-card"><p className="eyebrow">Live endpoint</p><h2>{build?.can_invoke ? "Ready when you are." : "Build this function first."}</h2><p>{build?.can_invoke ? "Use the guided runner for a test invocation, or copy the endpoint from the API guide." : "A successful build prepares the callable version behind this function. Callers use the API URL shown in the guide."}</p><button className="button primary" disabled={!build?.can_invoke} onClick={onRun}>Run a test →</button></article><article className="summary-card"><span>Access</span><strong>{fn.invoke_access}</strong><span>Output files</span><strong>{build?.active_version?.declared_output_files?.length || 0}</strong><span>Active version</span><strong>{build?.active_version?.version || "None"}</strong></article></section>; }
function RunWizard({ api, fn, build, onNotice }) {
  const [step, setStep] = useState(0); const [mode, setMode] = useState("async"); const [event, setEvent] = useState("{\n  \"name\": \"Ada\"\n}"); const [files, setFiles] = useState([]); const [result, setResult] = useState(null); const [busy, setBusy] = useState(false); const [error, setError] = useState(""); const poll = useRef(null);
  useEffect(() => () => window.clearTimeout(poll.current), []);
  const version = build?.active_version || build?.latest_version || {};
  const outputFiles = version.declared_output_files || [];
  const syncAllowed = !outputFiles.length;
  async function invoke() { let parsed; try { parsed = JSON.parse(event || "{}"); } catch { setError("Event JSON must be valid JSON."); return; } if (mode === "sync" && !syncAllowed) { setError("Sync invocation is available only when the function declares no output files."); return; } setBusy(true); setError(""); try { let body; const headers = {}; if (files.length) { body = new FormData(); body.append("event", JSON.stringify(parsed)); files.forEach((file) => body.append("input_files", file)); } else { headers["Content-Type"] = "application/json"; body = JSON.stringify({ event: parsed }); } const endpoint = mode === "sync" ? fn.links?.invoke_sync || `/api/functions/${fn.id}/invoke-sync/` : fn.links?.invoke || `/api/functions/${fn.id}/invoke/`; const response = await api.backend(`${endpoint}${endpoint.includes("?") ? "&" : "?"}response_mode=advanced`, { method: "POST", headers, body }); setResult(response); setStep(2); onNotice({ message: response.is_terminal ? "Invocation completed." : "Invocation queued. We are following its result.", kind: "success" }); if (!response.is_terminal) follow(response); } catch (err) { setError(err.message); } finally { setBusy(false); } }
  async function follow(current) { window.clearTimeout(poll.current); if (current.is_terminal) return; const delay = (current.poll_after_seconds || 1) * 1000; poll.current = window.setTimeout(async () => { try { const next = await api.backend(`${current.links?.self || `/api/invocations/${current.id}/`}?response_mode=advanced`); setResult(next); follow(next); } catch (err) { setError(err.message); } }, delay); }
  return <section className="run-panel"><header><p className="eyebrow">Guided invocation</p><h2>Run {fn.name}</h2><p>Start with the payload, then the platform will show the function result or the status to follow.</p></header><ol className="run-steps"><li className={step === 0 ? "current" : ""}><span>1</span> Choose</li><li className={step === 1 ? "current" : ""}><span>2</span> Configure</li><li className={step === 2 ? "current" : ""}><span>3</span> Result</li></ol>{step === 0 && <div className="step-content"><h3>How should this run?</h3><div className="choice-grid"><label className={mode === "async" ? "choice selected" : "choice"}><input type="radio" checked={mode === "async"} onChange={() => setMode("async")} /><strong>Async</strong><span>Queue work, then follow a complete result. Required for files and output artifacts.</span></label><label className={!syncAllowed ? "choice disabled" : mode === "sync" ? "choice selected" : "choice"}><input type="radio" disabled={!syncAllowed} checked={mode === "sync"} onChange={() => setMode("sync")} /><strong>Sync</strong><span>Wait briefly for a JSON-only function result. No input or output files.</span></label></div><div className="wizard-actions"><span/><button className="button primary" onClick={() => setStep(1)}>Continue →</button></div></div>}{step === 1 && <div className="step-content"><h3>What should the function receive?</h3><label className="config-field">Event JSON<textarea value={event} onChange={(e) => setEvent(e.target.value)} /></label>{mode === "async" && <label className="file-input">Attach input files <small>{version.invocation_input_max_files || 0} file(s), up to {version.invocation_input_max_total_size_mb || 0} MB total</small><input type="file" multiple onChange={(e) => setFiles(Array.from(e.target.files || []))} /></label>}{files.length > 0 && <p className="file-list">{files.map((file) => file.name).join(", ")}</p>}{error && <p className="form-error">{error}</p>}<div className="wizard-actions"><button className="button quiet" onClick={() => setStep(0)}>Back</button><button className="button primary" disabled={busy} onClick={invoke}>{busy ? "Sending…" : mode === "sync" ? "Run now →" : "Queue invocation →"}</button></div></div>}{step === 2 && <InvocationResult api={api} result={result} error={error} onBack={() => { setResult(null); setStep(1); }} />}</section>;
}
function InvocationResult({ api, result, error, onBack }) { async function download() { try { await api.download(result.links?.download || `/api/invocations/${result.id}/download/`, `invocation-${result.id}.zip`); } catch (e) { alert(e.message); } } if (error) return <div className="step-content"><p className="form-error">{error}</p><button className="button quiet" onClick={onBack}>Back</button></div>; if (!result) return <div className="loading">Preparing invocation…</div>; return <div className="step-content result"><Status value={result.status || result.frontend_state} /><h3>{result.is_terminal ? "The function has finished." : "The function is running."}</h3>{result.is_terminal ? <><dl className="review"><div><dt>Exit code</dt><dd>{result.exit_code ?? "—"}</dd></div><div><dt>Duration</dt><dd>{result.duration_ms ?? "—"} ms</dd></div><div><dt>Output files</dt><dd>{result.output_files?.length || 0}</dd></div></dl><label>Returned JSON<pre>{JSON.stringify(result.result || {}, null, 2)}</pre></label><div className="wizard-actions"><button className="button quiet" onClick={onBack}>Run again</button><button className="button" disabled={!result.can_download} onClick={download}>Download invocation ZIP</button></div></> : <><p>The result screen refreshes automatically. You can leave this tab; the invocation will continue.</p><pre>{JSON.stringify({ id: result.id, status: result.status, poll_after_seconds: result.poll_after_seconds }, null, 2)}</pre></>}</div>; }
function History({ api, fn, history, reload }) { const [current, setCurrent] = useState(null); async function open(item) { setCurrent(await api.backend(`${item.links?.self || `/api/invocations/${item.id}/`}?response_mode=advanced`)); } async function download(item) { await api.download(item.links?.download || `/api/invocations/${item.id}/download/`, `invocation-${item.id}.zip`); } return <section className="history"><header className="section-head"><div><p className="eyebrow">Previous runs</p><h2>Invocation history</h2></div><button className="button quiet" onClick={reload}>Refresh</button></header>{history.length ? <div className="history-list">{history.map((item) => <article key={item.id}><Status value={item.status}/><div><strong>{item.invocation_token_name || item.invocation_auth_type || "owner"}</strong><span>{formatDate(item.queued_at || item.started_at)}</span></div><span>{item.duration_ms ? `${item.duration_ms} ms` : "—"}</span><button className="text-button" onClick={() => open(item)}>View</button><button className="text-button" disabled={!item.can_download} onClick={() => download(item)}>ZIP</button></article>)}</div> : <div className="empty compact"><h2>No runs yet.</h2><p>Use the Run tab to send the first invocation.</p></div>}{current && <section className="result-detail"><h3>Invocation {current.id}</h3><InvocationResult api={api} result={current} onBack={() => setCurrent(null)} /></section>}</section>; }
function Tokens({ api, fn, tokens, reload, onNotice }) { const [name, setName] = useState(""); const [secret, setSecret] = useState(""); async function create(e) { e.preventDefault(); try { const response = await api.backend(fn.links?.tokens || `/api/functions/${fn.id}/tokens/`, { method: "POST", headers: jsonHeaders(), body: JSON.stringify({ name: name || "default" }) }); setSecret(response.raw_token); setName(""); await reload(); onNotice({ message: "Copy the token now. It will not be shown again.", kind: "success" }); } catch (err) { onNotice({ message: err.message, kind: "error" }); } } async function action(token, path) { try { const response = await api.backend(`/api/functions/${fn.id}/tokens/${token.id}/${path}/`, { method: "POST", headers: jsonHeaders(), body: "{}" }); if (response.raw_token) setSecret(response.raw_token); await reload(); } catch (err) { onNotice({ message: err.message, kind: "error" }); } } return <section className="tokens"><header><p className="eyebrow">Invocation access</p><h2>Function tokens</h2><p>Use these only for functions with token access. They are separate from your sign-in JWT.</p></header><form className="token-create" onSubmit={create}><Field label="Token name" value={name} onChange={(e) => setName(e.target.value)} placeholder="production-client"/><button className="button primary">Create token</button></form>{secret && <section className="secret"><div><span>Copy this token now</span><code>{secret}</code></div><button className="button" onClick={() => navigator.clipboard.writeText(secret)}>Copy</button></section>}<div className="history-list">{tokens.map((token) => <article key={token.id}><Status value={token.is_active ? "active" : "revoked"}/><div><strong>{token.name}</strong><span className="mono">{token.prefix}…</span></div><span>{token.last_used_at ? `Used ${formatDate(token.last_used_at)}` : "Not used"}</span>{token.is_active ? <><button className="text-button" onClick={() => action(token, "rotate")}>Rotate</button><button className="text-button danger" onClick={() => action(token, "revoke")}>Revoke</button></> : <span/>}</article>)}</div></section>; }
function ApiGuide({ fn, build }) { const endpoint = `${BACKEND}${fn.links?.invoke || `/api/functions/${fn.id}/invoke/`}`; const sync = `${BACKEND}${fn.links?.invoke_sync || `/api/functions/${fn.id}/invoke-sync/`}`; const access = fn.invoke_access; const auth = access === "public" ? "No authentication header required." : access === "token" ? "X-Function-Token: fn_<the-full-token>" : "Authorization: Bearer <your-userservice-JWT>"; return <section className="api-guide"><p className="eyebrow">Integration guide</p><h2>Call this function outside the dashboard.</h2><p>The image reference is internal. These API routes are the public interface for this function.</p><ol className="guide-steps"><li><h3>Use this authorization</h3><pre>{auth}</pre></li><li><h3>Invoke it</h3><pre>{`POST ${endpoint}\nContent-Type: application/json\n${auth}\n\n{\n  "event": { "name": "Ada" }\n}`}</pre></li>{!build?.active_version?.declared_output_files?.length && <li><h3>For a fast JSON-only call, use synchronous mode</h3><pre>{`POST ${sync}\nContent-Type: application/json\n${auth}\n\n{\n  "event": { "name": "Ada" }\n}`}</pre></li>}<li><h3>Follow an async result</h3><pre>{`GET ${BACKEND}/api/invocations/<id>/?response_mode=simple\n${auth}`}</pre></li><li><h3>Download all inputs, outputs, and logs</h3><pre>{`GET ${BACKEND}/api/invocations/<id>/download/\n${auth}`}</pre></li></ol></section>; }

function Field({ label, value, onChange, type = "text", placeholder = "", required = false }) { return <label className="field"><span>{label}</span><input type={type} value={value} onChange={onChange} placeholder={placeholder} required={required} /></label>; }
function NumberField({ label, value, onChange, min = 0, max }) { return <label className="field"><span>{label}</span><input type="number" min={min} max={max} value={value} onChange={(e) => onChange(Number(e.target.value))} /></label>; }
function Status({ value }) { const clean = String(value || "unknown").replaceAll("_", " "); return <span className="status" data-status={clean}>{clean}</span>; }
function Toast({ notice, onClose }) { return <aside className={`toast ${notice.kind}`}><span>{notice.kind === "success" ? "✓" : "!"}</span><p>{notice.message}</p><button onClick={onClose}>×</button></aside>; }

function useApi(session, onError) { async function request(base, path, options = {}) { const auth = options.auth !== false; const retry = options.retry !== false; const headers = new Headers(options.headers || {}); if (auth && session.access && !headers.has("Authorization")) headers.set("Authorization", `Bearer ${session.access}`); let response = await fetch(url(base, path), { ...options, headers }); if (response.status === 401 && auth && retry && session.refresh) { const refreshed = await request(USERSERVICE, "/api/auth/token/refresh/", { method: "POST", auth: false, retry: false, headers: jsonHeaders(), body: JSON.stringify({ refresh: session.refresh }) }); session.setAccess(refreshed.access); session.setRefresh(refreshed.refresh || session.refresh); localStorage.setItem(STORAGE.access, refreshed.access); localStorage.setItem(STORAGE.refresh, refreshed.refresh || session.refresh); headers.set("Authorization", `Bearer ${refreshed.access}`); response = await fetch(url(base, path), { ...options, headers }); } if (!response.ok) throw new Error(await responseMessage(response)); if (response.status === 204) return null; return response.headers.get("content-type")?.includes("application/json") ? response.json() : response.text(); }
  return { backend: (path, options) => request(BACKEND, path, options), userservice: (path, options) => request(USERSERVICE, path, options), download: async (path, fallback) => { const headers = new Headers(); if (session.access) headers.set("Authorization", `Bearer ${session.access}`); const response = await fetch(url(BACKEND, path), { headers }); if (!response.ok) throw new Error(await responseMessage(response)); const objectUrl = URL.createObjectURL(await response.blob()); const link = document.createElement("a"); link.href = objectUrl; link.download = fallback; link.click(); URL.revokeObjectURL(objectUrl); } };
}
function draftFromFunction(fn) { const version = fn?.active_version || fn?.latest_version || {}; const config = version.config || {}; return fn ? { ...EMPTY_DRAFT, code: "", name: fn.name || "", description: fn.description || "", invoke_access: fn.invoke_access || "private", handler: version.handler || "handler.main", config: JSON.stringify(config, null, 2), timeoutSeconds: Number(config.timeout_seconds || 60), inputTypes: version.invocation_input_mime_types || [], outputs: (version.declared_output_files || []).join("\n"), inputMaxFiles: version.invocation_input_max_files || 1, inputMaxSize: version.invocation_input_max_size_mb || 10, inputMaxTotal: version.invocation_input_max_total_size_mb || 10, outputMaxFiles: version.invocation_output_max_files || 5, outputMaxSize: version.invocation_output_max_file_size_mb || 10, outputMaxTotal: version.invocation_output_max_total_size_mb || 10 } : { ...EMPTY_DRAFT }; }
function url(base, path) { return path.startsWith("http") ? path : `${base.replace(/\/$/, "")}/${path.replace(/^\//, "")}`; }
function jsonHeaders() { return { "Content-Type": "application/json" }; }
async function responseMessage(response) { try { const body = await response.json(); return typeof body === "object" ? body.detail || Object.entries(body).map(([key, value]) => `${key}: ${Array.isArray(value) ? value.join(", ") : value}`).join("\n") : String(body); } catch { return `${response.status} ${response.statusText}`; } }
function lines(value) { return String(value || "").split("\n").map((item) => item.trim()).filter(Boolean); }
function withRuntimeConfig(config, draft) { return { ...config, timeout_seconds: Number(draft.timeoutSeconds) }; }
function formatDate(value) { return value ? new Intl.DateTimeFormat(undefined, { dateStyle: "medium", timeStyle: "short" }).format(new Date(value)) : "—"; }

function buildZip(files) { const encoder = new TextEncoder(); const entries = Object.entries(files).map(([name, text]) => { const data = encoder.encode(String(text ?? "")); return { nameBytes: encoder.encode(name), data, crc: crc32(data) }; }); const local = []; const central = []; let offset = 0; const date = new Date(); const dosTime = (date.getHours() << 11) | (date.getMinutes() << 5) | Math.floor(date.getSeconds() / 2); const dosDate = ((Math.max(1980, date.getFullYear()) - 1980) << 9) | ((date.getMonth() + 1) << 5) | date.getDate(); for (const entry of entries) { const part = bytes(30); write32(part, 0, 0x04034b50); write16(part, 4, 20); write16(part, 10, dosTime); write16(part, 12, dosDate); write32(part, 14, entry.crc); write32(part, 18, entry.data.length); write32(part, 22, entry.data.length); write16(part, 26, entry.nameBytes.length); local.push(part, entry.nameBytes, entry.data); const center = bytes(46); write32(center, 0, 0x02014b50); write16(center, 4, 20); write16(center, 6, 20); write16(center, 12, dosTime); write16(center, 14, dosDate); write32(center, 16, entry.crc); write32(center, 20, entry.data.length); write32(center, 24, entry.data.length); write16(center, 28, entry.nameBytes.length); write32(center, 42, offset); central.push(center, entry.nameBytes); offset += part.length + entry.nameBytes.length + entry.data.length; } const centralSize = central.reduce((total, part) => total + part.length, 0); const end = bytes(22); write32(end, 0, 0x06054b50); write16(end, 8, entries.length); write16(end, 10, entries.length); write32(end, 12, centralSize); write32(end, 16, offset); return new Blob([...local, ...central, end], { type: "application/zip" }); }
function bytes(size) { return new Uint8Array(size); } function write16(buffer, offset, value) { new DataView(buffer.buffer).setUint16(offset, value, true); } function write32(buffer, offset, value) { new DataView(buffer.buffer).setUint32(offset, value >>> 0, true); }
const CRC = (() => { const table = new Uint32Array(256); for (let n = 0; n < 256; n += 1) { let c = n; for (let k = 0; k < 8; k += 1) c = c & 1 ? 0xedb88320 ^ (c >>> 1) : c >>> 1; table[n] = c >>> 0; } return table; })(); function crc32(data) { let crc = 0xffffffff; for (const byte of data) crc = CRC[(crc ^ byte) & 255] ^ (crc >>> 8); return (crc ^ 0xffffffff) >>> 0; }

createRoot(document.getElementById("root")).render(<App />);
