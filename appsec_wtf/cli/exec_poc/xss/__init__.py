"""
Generate XSS injection payloads.
"""

def set_cli_opts(parser):
    """
    TODO: DOC
    """
    parser.set_defaults(func=entry)

    parser.add_argument(
        "--host",
        default="localhost",
        help="""
        Set the host that should be used in the generated payload. Default is
        %(default)s.
        """
    )
    parser.add_argument(
        "--port",
        default=3000,
        help="""
        Set the port that should be used in the generated payload. Default is
        %(default)s.
        """
    )
    parser.add_argument(
        "--endpoint",
        default="/",
        help="""
        Set the endpoint that should be used in the generated payload. Default
        is %(default)s.
        """
    )

def entry(args):
    """
    TODO: DOC
    """
    pass
