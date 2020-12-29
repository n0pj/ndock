from ..configs.base import Reconfig
from ..parsers import NginxParser
from ..builders import BoundBuilder
from ..items.dhcpd import DHCPDData


class DHCPDConfig (Reconfig):
    """
    ``DHCPD``
    """

    def __init__(self, **kwargs):
        k = {
            'parser': NginxParser(),
            'builder': BoundBuilder(DHCPDData),
        }
        k.update(kwargs)
        Reconfig.__init__(self, **k)
