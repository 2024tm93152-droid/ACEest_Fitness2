from flask import Flask, jsonify, request, abort

def create_app(config=None):
    app = Flask(__name__)
    if config:
        app.config.update(config)

    members = [
        {"id": 1, "name": "Alice", "plan": "Premium"},
        {"id": 2, "name": "Bob", "plan": "Basic"},
    ]
    plans = [
        {"id": "basic", "duration_weeks": 4, "price": 20},
        {"id": "premium", "duration_weeks": 12, "price": 50},
    ]

    @app.route("/", methods=["GET"])
    def home():
        return jsonify({"service": "ACEest Fitness", "version": "v1.0", "status": "ok"})

    @app.route("/members", methods=["GET"])
    def get_members():
        return jsonify({"members": members})

    @app.route("/members/<int:member_id>", methods=["GET"])
    def get_member(member_id):
        for m in members:
            if m["id"] == member_id:
                return jsonify(m)
        abort(404)

    @app.route("/members", methods=["POST"])
    def add_member():
        body = request.get_json()
        if not body or "name" not in body or "plan" not in body:
            abort(400)
        new_id = max([m["id"] for m in members]) + 1 if members else 1
        m = {"id": new_id, "name": body["name"], "plan": body["plan"]}
        members.append(m)
        return jsonify(m), 201

    @app.route("/plans", methods=["GET"])
    def get_plans():
        return jsonify({"plans": plans})

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)
