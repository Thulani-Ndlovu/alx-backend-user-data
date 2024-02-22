#!/usr/bin/env python3
'''Flask App'''
from flask import Flask, jsonify


@app.route("/", methods=["GET"], strict_slashes=False)
def index() -> str:
    '''homepage'''
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")