"""compose-casserole API — health + redis ping."""
import os
from flask import Flask, jsonify
import redis

app = Flask(__name__)
r = redis.Redis(host=os.environ.get("REDIS_HOST", "localhost"), port=6379, decode_responses=True)

@app.get("/health")
def health():
    try:
        r.ping()
        return jsonify({"status": "ok", "redis": True}), 200
    except Exception as e:
        return jsonify({"status": "degraded", "redis": False, "error": str(e)}), 503

@app.get("/counter")
def counter():
    n = r.incr("casserole_hits")
    return jsonify({"hits": n, "msg": "one more ladle"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5005)))
