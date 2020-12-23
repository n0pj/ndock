from ..configs.base import Reconfig
from ..parsers import SSVParser
from ..builders import BoundBuilder
from ..items.group import GroupsData


class GroupConfig (Reconfig):
    """
    ``/etc/group``
    """

    def __init__(self, **kwargs):
        k = {
            'parser': SSVParser(separator=':'),
            'builder': BoundBuilder(GroupsData),
        }
        k.update(kwargs)
        Reconfig.__init__(self, **k)
