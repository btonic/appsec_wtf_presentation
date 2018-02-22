"""
Generate various payloads for XSS injection.
"""

import encode
import turndownforwhat_example

def set_cli_opts(parser):
    """
    TODO: DOC
    """
    xss_subparsers = parser.add_subparsers()

    encode_xss_subparser = xss_subparsers.add_parser(
        "encode",
        help=encode.__doc__
    )
    encode.set_cli_opts(encode_xss_subparser)

    turndownforwhat_example_xss_subparser = xss_subparsers.add_parser(
        "turndownforwhat_example",
        help=turndownforwhat_example.__doc__
    )
    turndownforwhat_example.set_cli_opts(turndownforwhat_example_xss_subparser)
