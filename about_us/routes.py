from .data.about_us import ABOUT_US
from flask import Blueprint, request
from .about import About

about_us_routes = Blueprint("about_us", __name__)
about_data = About()
about_data.data = ABOUT_US

@about_us_routes.route("/", methods=["GET"])
def about():
  return about_data.data

@about_us_routes.route("/", methods=["PUT"])
def update_about():
  about_data.data  = request.get_json()
  return about_data.data
