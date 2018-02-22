"""
Perform application web-server related operations.
"""
import start

def set_cli_opts(parser):
    """
    Configure CLI options for this CLI subparser.
    """
    app_subparsers = parser.add_subparsers()

    start_subparser = app_subparsers.add_parser(
        "start",
        help=start.__doc__
    )
    start.set_cli_opts(start_subparser)
