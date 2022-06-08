from flask import Flask
from about_us.routes import about_us
from hero.routes import hero_routes

app = Flask(__name__)

app.register_blueprint(hero_routes, url_prefix="/hero")
app.register_blueprint(about_us, url_prefix="/about-us")

if __name__ == "__main__":
  app.run()