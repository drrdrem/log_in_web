# run.py

from web import app
from datetime import timedelta


if __name__ == "__main__":
    app.permanent_session_lifetime = timedelta(minutes=10)
    app.run(host="0.0.0.0", port=int("5000"))