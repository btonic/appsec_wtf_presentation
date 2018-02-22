"""
TODO: DOC
"""
from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

bp = Blueprint('nosql', __name__,
                template_folder='../templates')

@bp.route("/", methods=["GET"])
def index():
    """
    TODO: DOC
    """
    pass

@bp.route("/query_graphql", methods=["POST"])
def query_graphql():
    """
    TODO: DOC
    """
    pass

@bp.route("/mutate_graphql", methods=["POST"])
def mutate_graphql():
    """
    TODO: DOC
    """
    pass
