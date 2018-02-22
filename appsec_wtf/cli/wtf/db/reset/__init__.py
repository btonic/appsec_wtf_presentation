"""
Deletes all values currently set on the specified Redis endpoint.
"""

def set_cli_opts(parser):
    """
    Set the CLI options to control this command.
    """
    parser.set_defaults(entry=entry)

    parser.add_argument(
        "--host",
        default="localhost",
        help="""
        The host Redis is currently running on. Default is %(default)s.
        """
    )
    parser.add_argument(
        "--port",
        default=6379,
        help="""
        The port the Redis instance is listening on. Default is %(default)s.
        """
    )
    parser.add_argument(
        "--db",
        default=0,
        help="""
        The DB to reset on the redis instance. Default is %(default)s.
        """
    )

def entry(args):
    """
    The entrypoint for the command.
    """
    pass
