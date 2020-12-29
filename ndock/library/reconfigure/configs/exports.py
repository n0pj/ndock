from ..configs.base import Reconfig
from ..parsers import ExportsParser
from ..builders import BoundBuilder
from ..items.exports import ExportsData


class ExportsConfig (Reconfig):
    """
    ``/etc/fstab``
    """
    def __init__(self, **kwargs):
        k = {
            'parser': ExportsParser(),
            'builder': BoundBuilder(ExportsData),
        }
        k.update(kwargs)
        Reconfig.__init__(self, **k)
