"""
Controller for the XSS endpoint. Handles the endpoints:

    /
    /reflective/<code>
    /stored/<code>

"""
from flask import Blueprint, # For hooking into routing in app.py
                  render_template, # Render response templates
                  redirect, url_for, # Handles redirection and routing
                  request # Access to request query/body values

from jinja2 import TemplateNotFound


DEFAULT_REFLECTIVE = "Take a peek into the mirror. What do you see?"
DEFAULT_STORED = "Is it your reflection? Or something more?"


bp = Blueprint('xss', __name__,
                template_folder='../templates/xss')

@bp.route("/", methods=["GET"])
def index():
    """
    Render the index template, and allow for reflective or stored XSS.
    Reflective XSS is facilitated through the `flask.request` variable, which
    exposes query parameters sent with the request. Stored XSS is pulled from
    redis, unless it isn't set, in which case it defaults to `DEFAULT_STORED`.
    """
    return render_template(
        "index.jinja",
        stored_xss=bp.config.redis.get("STORED_XSS"),
        reflective_xss=request.args.get("reflective_xss", DEFAULT_REFLECTIVE)
    )

@bp.route("/reflective/<code:str>", methods=["GET"])
def reflective(code=DEFAULT_REFLECTIVE):
    """
    Redirect to the index page with the `reflective_xss` parameter set.
    """
    return redirect(
        url_for("index", reflective_xss=code)
    )

@bp.route("/stored/<code:str>", methods=["GET"])
def stored(code=DEFAULT_STORED):
    """
    Set the `STORED_XSS` key in Redis, then redirect to the index page. No
    query parameter is required, since this is stored and will result in the
    code being pulled from the db within the `index` route.
    """
    # Set the stored_xss variable so that the homepage
    bp.config.redis.set("STORED_XSS", code)
    return redirect(
        url_for("index")
    )
