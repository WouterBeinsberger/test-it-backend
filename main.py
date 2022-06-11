from about_us.routes import about_us_routes
from hero.routes import hero_routes
from services.routes import services_routes
from likes.routes import likes_routes
from contact.routes import contact_routes

from flask import Flask

app = Flask(__name__)

app.register_blueprint(hero_routes, url_prefix="/hero")
app.register_blueprint(about_us_routes, url_prefix="/about-us")
app.register_blueprint(services_routes, url_prefix="/services")
app.register_blueprint(likes_routes, url_prefix="/likes")
app.register_blueprint(contact_routes, url_prefix="/contact")

if __name__ == "__main__":
  app.run()