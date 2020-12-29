from ..configs.base import Reconfig
from ..parsers import IniFileParser
from ..builders import BoundBuilder
from ..items.netatalk import NetatalkData


class NetatalkConfig (Reconfig):
    """
    Netatalk afp.conf
    """

    def __init__(self, **kwargs):
        k = {
            'parser': IniFileParser(),
            'builder': BoundBuilder(NetatalkData),
        }
        k.update(kwargs)
        Reconfig.__init__(self, **k)
