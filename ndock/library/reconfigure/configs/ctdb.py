from ..configs.base import Reconfig
from ..parsers import IniFileParser
from ..parsers import SSVParser
from ..builders import BoundBuilder
from ..items.ctdb import CTDBData, NodesData, PublicAddressesData


class CTDBConfig (Reconfig):
    """
    ``CTDB main config``
    """

    def __init__(self, **kwargs):
        k = {
            'parser': IniFileParser(sectionless=True),
            'builder': BoundBuilder(CTDBData),
        }
        k.update(kwargs)
        Reconfig.__init__(self, **k)


class CTDBNodesConfig (Reconfig):
    """
    ``CTDB node list file``
    """

    def __init__(self, **kwargs):
        k = {
            'parser': SSVParser(),
            'builder': BoundBuilder(NodesData),
        }
        k.update(kwargs)
        Reconfig.__init__(self, **k)


class CTDBPublicAddressesConfig (Reconfig):
    """
    ``CTDB public address list file``
    """

    def __init__(self, **kwargs):
        k = {
            'parser': SSVParser(separator=' '),
            'builder': BoundBuilder(PublicAddressesData),
        }
        k.update(kwargs)
        Reconfig.__init__(self, **k)
