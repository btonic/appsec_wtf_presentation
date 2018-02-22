"""
Generate various payloads for CSS injection.
"""
import keylogger_example
import encode

def set_cli_opts(parser):
    """
    Set the CLI options supported by this command.
    """
    css_subparsers = parser.add_subparsers()

    encode_css_subparser = css_subparsers.add_parser(
        "encode",
        help=encode.__doc__
    )
    encode.set_cli_opts(encode_css_subparser)

    keylogger_example_css_subparser = css_subparsers.add_parser(
        "keylogger_example",
        help=keylogger_example.__doc__
    )
    keylogger_example.set_cli_opts(keylogger_example_css_subparser)
