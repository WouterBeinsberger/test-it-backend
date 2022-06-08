from about_us.routes import about_us_routes
from hero.routes import hero_routes
from flask import Flask

app = Flask(__name__)

app.register_blueprint(hero_routes, url_prefix="/hero")
app.register_blueprint(about_us_routes, url_prefix="/about-us")

if __name__ == "__main__":
  app.run()