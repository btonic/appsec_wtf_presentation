"""
Controller for the CSS endpoint. Handles the routes:

    /
    /inject/<css>
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

bp = Blueprint('css', __name__,
                template_folder='../templates')

@bp.route("/", methods=["GET"])
def index():
    """
    Render the CSS Injection index page. This can also contain the CSS
    injection code if the `CSS_INJECTION` value is set in Redis.
    """
    return render_template(
        "css/index.jinja",
        css_injection=app.config["redis"].get("CSS_INJECTION") or None
    )

@bp.route("/inject/<path:css>", methods=["GET"])
def inject(css):
    """
    Stores the provided CSS value within the `CSS_INJECTION` key in Redis,
    then redirects back to the css injection index page. For simplicity and
    to prevent potentially super long URLs on index, this exploit has been made
    as a backend-stored exploit.
    """
    app.config["redis"].set("CSS_INJECTION", css.decode("base64"))
    return redirect(
        url_for("css.index")
    )

@bp.route("/reset", methods=["GET"])
def reset():
    """
    Resets the currently set `CSS_INJECTION` value in Redis.
    """
    app.config["redis"].delete("CSS_INJECTION")
    return redirect(
        url_for("css.index")
    )
