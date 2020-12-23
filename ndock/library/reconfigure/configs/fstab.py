from ..configs.base import Reconfig
from ..parsers import SSVParser
from ..builders import BoundBuilder
from ..items.fstab import FSTabData


class FSTabConfig (Reconfig):
    """
    ``/etc/fstab``
    """

    def __init__(self, **kwargs):
        k = {
            'parser': SSVParser(),
            'builder': BoundBuilder(FSTabData),
        }
        k.update(kwargs)
        Reconfig.__init__(self, **k)
