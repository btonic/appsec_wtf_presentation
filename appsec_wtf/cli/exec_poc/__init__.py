"""
TODO: DOC
"""

import css
import xss
import nosql

def set_cli_opts(parser):
    """
    TODO: DOC
    """
    exec_poc_subparsers = parser.add_subparsers()

    css_exec_poc_subparser = exec_poc_subparsers.add_parser(
        "css",
        help=css.__doc__
    )
    css.set_cli_opts(css_exec_poc_subparser)

    xss_exec_poc_subparser = exec_poc_subparsers.add_parser(
        "xss",
        help=xss.__doc__
    )
    xss.set_cli_opts(xss_exec_poc_subparser)

    nosql_exec_poc_subparser = exec_poc_subparsers.add_parser(
        "nosql",
        help=nosql.__doc__
    )
    nosql.set_cli_opts(nosql_exec_poc_subparser)
