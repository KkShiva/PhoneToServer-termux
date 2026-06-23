from flask import Flask, send_from_directory, request, jsonify
import subprocess, re

app = Flask(__name__, static_folder="static")
proc = None

def get_ip():
    try:
        out = subprocess.check_output(["ifconfig"], text=True)
        ips = re.findall(r"inet (\\d+\\.\\d+\\.\\d+\\.\\d+)", out)
        for ip in ips:
            if not ip.startswith("127."):
                return ip
    except:
        pass
    return "127.0.0.1"

@app.route("/")
def root():
    return send_from_directory("static","index.html")

@app.route("/api/info")
def info():
    return {"ip": get_ip()}

@app.route("/api/start", methods=["POST"])
def start():
    global proc
    data=request.json
    port=data.get("port","8080")
    folder=data.get("folder","~/storage/shared")
    proc=subprocess.Popen(["copyparty","-p",str(port),"-v",f"{folder}::r"])
    return jsonify(ok=True)

@app.route("/api/stop", methods=["POST"])
def stop():
    global proc
    if proc:
        proc.terminate()
        proc=None
    return jsonify(ok=True)

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000)
