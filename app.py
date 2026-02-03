from flask import Flask, send_from_directory, render_template
import os

app = Flask(__name__, static_folder='.', template_folder='.')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/<path:path>")
def static_proxy(path):
    # Route to serve static files like CSS, JS, and Data from the root folder
    return send_from_directory(app.static_folder, path)

if __name__ == "__main__":
    # Use the port assigned by Render, or default to 10000 for local testing
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
