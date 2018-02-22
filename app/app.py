"""
TODO: DOC
"""
import controllers
import config

app = Flask(__name__)
"""
The top level application, handles routing and blueprint configuration.
"""

# Routing for each of the blueprints

app.register_blueprint(controllers.css.bp, url_prefix="/css")
app.register_blueprint(controllers.nosql.bp, url_prefix="/nosql")
app.register_blueprint(controllers.xss.bp, url_prefix="/xss")

# Configuration of the flask instance variables
config.redis_config.configure(app)
