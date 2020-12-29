from ..tests.parsers.base_test import BaseParserTest
from ..parsers import ShellParser
from ..nodes import *


class ShellParserTest (BaseParserTest):
    parser = ShellParser()
    source = """
# The following
# otherwise they
PORTS_pop3d="110,995"
PORTS_htpasswd="80,443" # b
"""
    parsed = RootNode(
        None,
        PropertyNode('PORTS_pop3d', '110,995',
                     comment='The following\notherwise they'),
        PropertyNode('PORTS_htpasswd', '80,443', comment='b'),
    )


del BaseParserTest
