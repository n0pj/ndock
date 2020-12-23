import argparse
from typing import Union


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

    @classmethod
    def search_directive(cls, directive_name, any_block):
        target_directive_block = None
        for block in any_block:
            if block['directive'] == directive_name:
                target_directive_block = block

        return target_directive_block

    @classmethod
    def insert_block(
            cls,
            new_blocks: list,
            any_block: list,
            directive_name: str = None,
    ):
        new_any_block: list = []
        for block in any_block:
            if block['directive'] == directive_name and directive_name:
                # print(directive_name, 'name')
                # del block
                for new_block in new_blocks:
                    new_any_block.append(new_block)

                # print(new_blocks, 'a')
                # block = new_blocks
                # print(any_block, 'test')
                # print(new_any_block)
            else:
                new_any_block.append(block)
        if not directive_name:
            for new_block in new_blocks:
                new_any_block.append(new_block)

        return new_any_block
