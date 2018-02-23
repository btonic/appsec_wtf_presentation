"""
Generate nosql injection payloads.
"""

import redis_takeover

def set_cli_opts(parser):
    """
    TODO: DOC
    """
    nosql_subparsers = parser.add_subparsers()

    redis_takeover_nosql_subparser = nosql_subparsers.add_parser(
        "redis_takeover",
        help=redis_takeover.__doc__
    )
    redis_takeover.set_cli_opts(redis_takeover_nosql_subparser)
