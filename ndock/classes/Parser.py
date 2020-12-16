import argparse


class Parser:
    parser = None

    def __init__(self):
        self.parser = argparse.ArgumentParser(
            prog=None, usage=None, description=None, epilog=None, parents=[],
            formatter_class=argparse.HelpFormatter,
            prefix_chars='-', fromfile_prefix_chars=None,
            argument_default=None,
            conflict_handler='error', add_help=True, allow_abbrev=True
        )
        return None

    def add_arg(self, name, abbreviation_name):
        self.parser.add_argument(name, abbreviation_name)
        return None
