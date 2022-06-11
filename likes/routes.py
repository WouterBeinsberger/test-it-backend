from .likes import Likes
from data.likes import LIKES
from flask import Blueprint, request

likes_routes = Blueprint("likes", __name__)
likes_data = Likes()
likes_data.data = LIKES

@likes_routes.route("/", methods=["GET"])
def likes():
  return likes_data.data

@likes_routes.route("/", methods=["PUT"])
def update_likes():
  likes_data.data = request.get_json()
  return likes_data.data