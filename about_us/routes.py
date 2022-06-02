from .data.about_us import ABOUT_US
from flask import Blueprint, jsonify

about_us = Blueprint("about_us", __name__)

@about_us.route("/", methods=["GET"])
def about():
  return jsonify(ABOUT_US)