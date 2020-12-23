from ..configs.base import Reconfig
from ..parsers import JsonParser
from ..builders import BoundBuilder
from ..items.ajenti import AjentiData


class AjentiConfig (Reconfig):
    def __init__(self, **kwargs):
        k = {
            'parser': JsonParser(),
            'builder': BoundBuilder(AjentiData),
        }
        k.update(kwargs)
        Reconfig.__init__(self, **k)
