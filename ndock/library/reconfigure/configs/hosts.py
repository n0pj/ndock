from ..configs.base import Reconfig
from ..parsers import SSVParser
from ..builders import BoundBuilder
from ..items.hosts import HostsData


class HostsConfig (Reconfig):
    """
    ``/etc/hosts``
    """

    def __init__(self, **kwargs):
        k = {
            'parser': SSVParser(),
            'builder': BoundBuilder(HostsData),
        }
        k.update(kwargs)
        Reconfig.__init__(self, **k)
