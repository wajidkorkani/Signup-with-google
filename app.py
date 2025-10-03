import os
from flask import Flask, redirect, url_for, render_template as render
from flask_dance.contrib.google import make_google_blueprint, google

# Allow HTTP for local dev
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask(__name__)
app.secret_key = "supersekrit"   # change in production

# 🔑 Replace with your Google credentials
client_id = "YourGoogleClientID"
client_secret = "YourGoogleClientSecret"

google_bp = make_google_blueprint(
    client_id=client_id,
    client_secret=client_secret,
    scope=[
        "openid",
        "https://www.googleapis.com/auth/userinfo.profile",
        "https://www.googleapis.com/auth/userinfo.email",
    ],
    redirect_to="google_login"
)
app.register_blueprint(google_bp, url_prefix="/login")


@app.route("/")
def index():
    return render("login.html")


@app.route("/google_login")
def google_login():
    if not google.authorized:
        return redirect(url_for("google.login"))
    
    # Fetch user info
    resp = google.get("/oauth2/v2/userinfo")
    if not resp.ok:
        return f"Error: {resp.text}"
    
    user_info = resp.json()
    return render("home.html", name=user_info["name"], email=user_info["email"], picture=user_info["picture"])


if __name__ == "__main__":
    app.run(debug=True)
