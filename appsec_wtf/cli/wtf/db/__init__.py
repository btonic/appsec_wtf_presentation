"""
Perform application database related operations.
"""
import reset

def set_cli_opts(parser):
    """
    TODO: DOC
    """
    db_subparsers = parser.add_subparsers()

    reset_db_subparser = db_subparsers.add_parser(
        "reset",
        help=reset.__doc__
    )
    reset.set_cli_opts(reset_db_subparser)
