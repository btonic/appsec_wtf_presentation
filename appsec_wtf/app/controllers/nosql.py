"""
TODO: DOC
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

bp = Blueprint('nosql', __name__,
                template_folder='../templates')

SECRET_USERS = ["secret-user-sarah", "secret-user-matt", "secret-user-david"]
USERS = ["user-kevin", "user-zach", "user-sav"]

@bp.route("/", methods=["GET"])
def index():
    """
    TODO: DOC
    """
    return render_template("nosql/index.jinja")

@bp.route("/users", methods=["GET"])
def users():
    """
    TODO: DOC
    """
    users = app.config["redis"].keys(request.args.get("search_query", "user-*")) or []
    value_mapping = dict( (user, app.config["redis"].get(user)) for user in users)
    return render_template(
        "nosql/users.jinja",
        users = value_mapping
    )

@bp.route("/users/reset", methods=["GET"])
def reset_users():
    """
    TODO: DOC
    """
    for user in SECRET_USERS:
        app.config["redis"].set(user, "I *may* be in the illuminati. Maybe.")

    for user in USERS:
        app.config["redis"].set(user, "I'm just normal :]")

    return redirect(
        url_for("nosql.index")
    )
