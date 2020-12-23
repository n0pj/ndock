from ..configs.base import Reconfig
from ..parsers import SquidParser
from ..builders import BoundBuilder
from ..items.squid import SquidData


class SquidConfig (Reconfig):
    def __init__(self, **kwargs):
        k = {
            'parser': SquidParser(),
            'builder': BoundBuilder(SquidData),
        }
        k.update(kwargs)
        Reconfig.__init__(self, **k)
