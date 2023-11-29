import argparse

from dundie.core import load  # noqa


def main():
    parser = argparse.ArgumentParser(
        description="Dunder Mifflin Rewards CLI",
        epilog="Enjoy and use with cautious.",
    )
    parser.add_argument(
        "subcommand",
        type=str,
        help="The subcommand top run",
        choices=("load", "show", "send"),
        default="help",
    )
    parser.add_argument("filepath", type=str, help="File path to load", default=None)  # noqa
    args = parser.parse_args()

    print(*globals()[args.subcommand](args.filepath))
