
from flask import Flask, redirect, request
from datetime import datetime

app = Flask(__name__)

DESTINATION = "https://www.instagram.com/"

@app.route("/test")
def test():
    ip = request.remote_addr
    forwarded = request.headers.get("X-Forwarded-For", "Not provided")

    print("\n========== VISITOR ==========")
    print("Time:", datetime.now().isoformat())
    print("Connection IP:", ip)
    print("Forwarded IP header:", forwarded)
    print("User-Agent:", request.headers.get("User-Agent"))
    print("=============================\n", flush=True)

    return redirect(DESTINATION, code=302)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
