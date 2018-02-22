"""
Routing and configuration of backend resource connectors are found within this
module. The application `app` instance is defined here, along with the routing
for controllers.
"""
from flask import Flask

import controllers
import config

app = Flask(__name__)
"""
The top level application, handles routing and blueprint configuration storage.
"""

# Routing for each of the blueprints
app.register_blueprint(controllers.pages.bp, url_prefix="/")
app.register_blueprint(controllers.css.bp, url_prefix="/css")
app.register_blueprint(controllers.nosql.bp, url_prefix="/nosql")
app.register_blueprint(controllers.xss.bp, url_prefix="/xss")

# Configuration of the flask instance variables
config.redis_config.configure(app)
