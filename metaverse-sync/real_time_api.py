from flask import Flask, request, jsonify

app = Flask(__name__)
updates = []

@app.route('/api/updates', methods=['POST'])
def github_update():
    payload = request.json
    updates.append(payload)
    print("Update received:", payload)
    return jsonify({"status": "dispatched"}), 200

@app.route('/api/pull_updates')
def pull_updates():
    return jsonify({"updates": updates})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3080)
