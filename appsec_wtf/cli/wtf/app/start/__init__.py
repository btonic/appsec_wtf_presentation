"""
Start the application web server.
"""

from appsec_wtf.app import app

def set_cli_opts(parser):
    """
    Configure CLI options for this CLI entrypoint.
    """
    # Set the entry point to be this modules `entry` command.
    parser.set_defaults(func=entry)
    parser.add_argument(
        "--host",
        default="0.0.0.0",
        help="""
        Set the host address that the application should listen on. Default is
        %(default)s.
        """
    )
    parser.add_argument(
        "--port",
        default=3000,
        help="""
        Set the port that the application should listen on. Default is
        %(default)s.
        """
    )
    parser.add_argument(
        "--debug",
        default=False,
        action="store_true",
        help="""
        Enable debugging. Default is %(default)s.
        """
    )

def entry(args):
    """
    The entry point for this command.
    """
    app.run(
        debug=args.debug,
        host=args.host,
        port=args.port
    )
