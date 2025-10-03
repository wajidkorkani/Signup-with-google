# Signup-with-google

A minimal Flask example that demonstrates signing in with Google using Flask-Dance.

This app starts a small web server with a "Login with Google" button and shows the
authenticated user's name, email, and profile picture after successful OAuth.

## What this repo contains

- `app.py` - the Flask application using `flask-dance` to authenticate via Google.

## Prerequisites

- Python 3.8+
- A Google Cloud project with OAuth 2.0 credentials (see steps below)

## Installation

1. Create and activate a virtual environment (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

## Create Google OAuth credentials

1. Go to https://console.cloud.google.com/apis/credentials and create a new OAuth 2.0 Client ID.
2. Choose "Web application" and set an authorized redirect URI for local development:

```
http://localhost:5000/login/google/authorized
```

3. Note the Client ID and Client Secret.

## Configuration

Open `app.py` and replace the placeholders at the top with your credentials:

```py
client_id = "YourGoogleClientID"
client_secret = "YourGoogleClientSecret"
```

Alternative (recommended for production): don't store secrets in source. Instead set environment variables and update `app.py` to read them from `os.environ`. Example:

```py
client_id = os.environ.get('GOOGLE_CLIENT_ID')
client_secret = os.environ.get('GOOGLE_CLIENT_SECRET')
```

Then set them in PowerShell before running:

```powershell
$env:GOOGLE_CLIENT_ID = 'your-client-id'
$env:GOOGLE_CLIENT_SECRET = 'your-client-secret'
```

Also change the `app.secret_key` in `app.py` to a secure value for production.

> Note: The app sets `OAUTHLIB_INSECURE_TRANSPORT=1` to allow HTTP during local development. Do not use this in production.

## Run the app

Start the Flask app (PowerShell):

```powershell
python app.py
```

Open http://localhost:5000 in your browser and click "Login with Google".

## How it works (quick)

- The app registers a Flask-Dance Google blueprint at `/login`.
- If the user is not authorized, they're redirected to Google's consent screen.
- After consent, the app requests `/oauth2/v2/userinfo` and displays the user's name, email, and picture.

## Dependencies

See `requirements.txt` for the Python dependencies used by this project.

## Troubleshooting

- If the redirect fails, double-check the authorized redirect URI in the Google Cloud Console.
- If you see issues with credentials, confirm the Client ID/Secret are correct and that they belong to the same Google Cloud project that has the Google+ / People API (userinfo endpoint) enabled.

## License

This example is provided as-is for learning purposes.
# Signup-with-google