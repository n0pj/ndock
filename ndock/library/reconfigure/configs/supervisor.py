from ..configs.base import Reconfig
from ..parsers import IniFileParser
from ..includers import SupervisorIncluder
from ..builders import BoundBuilder
from ..items.supervisor import SupervisorData


class SupervisorConfig (Reconfig):
    """
    ``/etc/supervisor/supervisord.conf``
    """

    def __init__(self, **kwargs):
        k = {
            'parser': IniFileParser(),
            'includer': SupervisorIncluder(),
            'builder': BoundBuilder(SupervisorData),
        }
        k.update(kwargs)
        Reconfig.__init__(self, **k)
