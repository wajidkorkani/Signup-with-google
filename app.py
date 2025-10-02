from flask import Flask, redirect, url_for
from flask_dance.contrib.google import make_google_blueprint, google

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Replace with your credentials from Google Cloud Console
app.config["GOOGLE_OAUTH_CLIENT_ID"] = "YOUR_GOOGLE_CLIENT_ID"
app.config["GOOGLE_OAUTH_CLIENT_SECRET"] = "YOUR_GOOGLE_CLIENT_SECRET"

google_bp = make_google_blueprint(
    client_id=app.config["GOOGLE_OAUTH_CLIENT_ID"],
    client_secret=app.config["GOOGLE_OAUTH_CLIENT_SECRET"],
    scope=["profile", "email"],
    redirect_to="google_login"
)
app.register_blueprint(google_bp, url_prefix="/login")


@app.route("/")
def index():
    if not google.authorized:
        return '<a href="/login/google">Sign in with Google</a>'
    resp = google.get("/oauth2/v2/userinfo")
    user_info = resp.json()
    return f"Hello, {user_info['name']}! Your email is {user_info['email']}."


@app.route("/google_login")
def google_login():
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
