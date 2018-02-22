"""
Controller for the XSS endpoint. Handles the routes:

    /
    /reflective/<code>
    /stored/<code>
    /reset

"""
# For hooking into routing in app.py
from flask import Blueprint
# Render response templates
from flask import render_template
# Handles redirection and routing
from flask import redirect, url_for
# Access to request query/body values
from flask import request
# Access to the current application for config settings
from flask import current_app as app

DEFAULT_REFLECTIVE = "Take a peek into the mirror. What do you see?"
DEFAULT_STORED = "Is it your reflection? Or something more?"

bp = Blueprint('xss', __name__,
                template_folder='../templates')


@bp.route("/", methods=["GET"])
def index():
    """
    Render the index template, and allow for reflective or stored XSS.
    Reflective XSS is facilitated through the `flask.request` variable, which
    exposes query parameters sent with the request. Stored XSS is pulled from
    redis, unless it isn't set, in which case it defaults to `DEFAULT_STORED`.
    """
    return render_template(
        "xss/index.jinja",
        stored_xss=app.config["redis"].get("STORED_XSS") or DEFAULT_STORED,
        reflective_xss=request.args.get("reflective_xss", DEFAULT_REFLECTIVE)
    )

@bp.route("/reflective/<code>", methods=["GET"])
def reflective(code=DEFAULT_REFLECTIVE):
    """
    Redirect to the index page with the `reflective_xss` parameter set.
    """
    return redirect(
        url_for("xss.index", reflective_xss=code)
    )

@bp.route("/stored/<code>", methods=["GET"])
def stored(code=DEFAULT_STORED):
    """
    Set the `STORED_XSS` key in Redis, then redirect to the index page. No
    query parameter is required, since this is stored and will result in the
    code being pulled from the db within the `index` route.
    """
    # Set the stored_xss variable so that the homepage
    app.config["redis"].set("STORED_XSS", code)
    return redirect(
        url_for("xss.index")
    )

@bp.route("/reset", methods=["GET"])
def reset():
    """
    Reset the `STORED_XSS` value wthin redis.
    """
    app.config["redis"].delete("STORED_XSS")
    return redirect(
        url_for("xss.index")
    )
