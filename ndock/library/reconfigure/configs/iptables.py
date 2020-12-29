from ..configs.base import Reconfig
from ..parsers import IPTablesParser
from ..builders import BoundBuilder
from ..items.iptables import IPTablesData


class IPTablesConfig (Reconfig):
    """
    ``iptables-save`` and ``iptables-restore``
    """

    def __init__(self, **kwargs):
        k = {
            'parser': IPTablesParser(),
            'builder': BoundBuilder(IPTablesData),
        }
        k.update(kwargs)
        Reconfig.__init__(self, **k)
