from crypt import methods
from .services import Services
from data.services import SERVICES
from flask import Blueprint, request

services_routes = Blueprint("services", __name__)
services_data = Services()
services_data.data = SERVICES

@services_routes.route("/", methods=["GET"])
def services():
  return services_data.data

@services_routes.route("/", methods=["PUT"])
def update_services():
  services_data.data = request.get_json()
  return services_data.data