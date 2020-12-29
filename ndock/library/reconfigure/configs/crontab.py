from ..configs.base import Reconfig
from ..parsers import CrontabParser
from ..builders import BoundBuilder
from ..items.crontab import CrontabData


class CrontabConfig (Reconfig):
    def __init__(self, **kwargs):
        k = {
            'parser': CrontabParser(),
            'builder': BoundBuilder(CrontabData),
        }
        k.update(kwargs)
        Reconfig.__init__(self, **k)
