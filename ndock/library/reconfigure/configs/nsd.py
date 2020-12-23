from ..configs.base import Reconfig
from ..parsers import NSDParser
from ..builders import BoundBuilder
from ..items.nsd import NSDData


class NSDConfig (Reconfig):
    """
    ``NSD DNS server nsd.conf``
    """

    def __init__(self, **kwargs):
        k = {
            'parser': NSDParser(),
            'builder': BoundBuilder(NSDData),
        }
        k.update(kwargs)
        Reconfig.__init__(self, **k)
