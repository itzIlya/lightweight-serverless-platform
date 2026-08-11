# Serverless Platform Frontend

This is the local prototype frontend for the platform.

Run it from the project root:

```powershell
python -m http.server 5173 -d frontend
```

Then open:

```text
http://localhost:5173
```

Default service URLs:

```text
userservice: http://localhost:8100
backend:     http://localhost:8000
```

Implemented user flow:

```text
landing page
login/sign up
my functions list
add new function
function editor
enter function name
paste handler.py code
paste requirements.txt
choose public/private/token access
choose input MIME types and limits
declare expected output filenames and limits
press Build
see an in-page queued notification
see build status at the top of the editor
refresh or auto-poll build status
invoke with JSON event and optional files
poll invocation status
view result/stdout/stderr/exit code
download invocation ZIP
create/update/rotate/revoke invocation tokens
view invocation history, including token metadata when a function token was used
```

The editor creates an uncompressed ZIP in the browser containing:

```text
handler.py
requirements.txt
config.json
```

The backend still validates and builds the uploaded ZIP. The frontend does not
replace backend validation.

Prototype auth storage:

```text
access JWT:  localStorage
refresh JWT: localStorage
```

This is intentionally simple for the local prototype. Production should move to
a safer refresh-token strategy.
