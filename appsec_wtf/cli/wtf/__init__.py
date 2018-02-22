"""
TODO: DOC
"""
import db
import app

def set_cli_opts(parser):
    """
    TODO: DOC
    """
    wtf_subparsers = parser.add_subparsers()

    wtf_app_subparser = wtf_subparsers.add_parser(
        "app",
        help=app.__doc__
    )
    app.set_cli_opts(wtf_app_subparser)

    wtf_db_subparser = wtf_subparsers.add_parser(
        "db",
        help=db.__doc__
    )
    db.set_cli_opts(wtf_db_subparser)
