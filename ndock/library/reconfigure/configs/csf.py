from ..configs.base import Reconfig
from ..parsers import ShellParser
from ..builders import BoundBuilder
from ..items.csf import CSFData


class CSFConfig (Reconfig):
    """
    ``CSF main config``
    """

    def __init__(self, **kwargs):
        k = {
            'parser': ShellParser(),
            'builder': BoundBuilder(CSFData),
        }
        k.update(kwargs)
        Reconfig.__init__(self, **k)
