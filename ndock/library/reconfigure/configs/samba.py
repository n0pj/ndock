from ..configs.base import Reconfig
from ..parsers import IniFileParser
from ..builders import BoundBuilder
from ..items.samba import SambaData


class SambaConfig (Reconfig):
    def __init__(self, **kwargs):
        k = {
            'parser': IniFileParser(),
            'builder': BoundBuilder(SambaData),
        }
        k.update(kwargs)
        Reconfig.__init__(self, **k)
