from ..configs.base import Reconfig
from ..parsers import SSVParser
from ..builders import BoundBuilder
from ..items.passwd import PasswdData


class PasswdConfig (Reconfig):
    """
    ``/etc/passwd``
    """

    def __init__(self, **kwargs):
        k = {
            'parser': SSVParser(separator=':'),
            'builder': BoundBuilder(PasswdData),
        }
        k.update(kwargs)
        Reconfig.__init__(self, **k)
