from ..configs.base import Reconfig
from ..parsers import SSVParser
from ..builders import BoundBuilder
from ..items.resolv import ResolvData


class ResolvConfig (Reconfig):
    """
    ``/etc/resolv.conf``
    """

    def __init__(self, **kwargs):
        k = {
            'parser': SSVParser(maxsplit=1),
            'builder': BoundBuilder(ResolvData),
        }
        k.update(kwargs)
        Reconfig.__init__(self, **k)
