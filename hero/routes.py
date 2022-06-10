from crypt import methods
import json
from .hero import Hero
from .data.hero import HERO
from flask import Blueprint, request

hero_routes = Blueprint("hero", __name__)
hero_data = Hero()
hero_data.data = HERO

@hero_routes.route("/", methods=["GET"])
def hero():
  return hero_data.data

@hero_routes.route("/", methods=["PUT"])
def update_hero():
  hero_data.data = request.get_json()
  return hero_data.data