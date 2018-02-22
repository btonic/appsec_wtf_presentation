"""
TODO: DOC
"""
from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

bp = Blueprint('css', __name__,
                template_folder='../templates/css')

@bp.route("/", methods=["GET"])
def index():
    """
    TODO: DOC
    """
    pass

@bp.route("/inject", methods=["POST"])
def post_inject():
    """
    TODO: DOC
    """
    pass
