"""
Controller for the default pages endpoint. Handles the routes:

    /

"""
from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

bp = Blueprint('pages', __name__,
                template_folder='../templates')

@bp.route("/", methods=["GET"])
def index():
    """
    Handles the root hopmepage rendering.
    """
    return render_template("pages/index.jinja")
