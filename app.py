from flask import Flask, render_template, request
import os
import subprocess
import threading
import socket

app = Flask(__name__)

BASE_DIR = "/storage/shared"


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except:
        ip = "127.0.0.1"

    s.close()
    return ip


def start_copyparty(folder, port):
    subprocess.Popen([
        "copyparty",
        "-p",
        str(port),
        "-v",
        f"{folder}::r"
    ])


@app.route("/")
def home():

    folders = []

    for item in sorted(os.listdir(BASE_DIR)):
        full = os.path.join(BASE_DIR, item)

        if os.path.isdir(full):
            folders.append(full)

    return render_template(
        "index.html",
        folders=folders,
        ip=get_ip()
    )


@app.route("/start", methods=["POST"])
def start():

    folder = request.form["folder"]
    port = request.form["port"]

    threading.Thread(
        target=start_copyparty,
        args=(folder, port),
        daemon=True
    ).start()

    return render_template(
        "success.html",
        folder=folder,
        port=port,
        ip=get_ip()
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )
