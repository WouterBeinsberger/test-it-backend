from .contact import Contact
from data.contact import CONTACT
from flask import Blueprint, request

contact_routes = Blueprint("contact", __name__)
contact_data = Contact()
contact_data.data = CONTACT

@contact_routes.route("/", methods=["GET"])
def contact():
  return contact_data.data

@contact_routes.route("/", methods=["PUT"])
def update_contact():
  contact_data.data = request.get_json()
  return contact_data.data