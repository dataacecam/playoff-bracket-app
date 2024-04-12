import os
from . import create_app
from .models import Participant
from flask import jsonify, render_template

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

@app.route("/participant/list", methods=["GET"])
def get_participants():
    participants = Participant.query.all()
    return jsonify([participant.to_json() for participant in participants])

@app.route("/participant/<int:isbn>", methods=["GET"])
def get_participant(isbn):
    participant = Participant.query.get(isbn)
    if participant is None:
        abort(404)
    return jsonify(participant.to_json())