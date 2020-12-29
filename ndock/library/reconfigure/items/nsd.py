from ..nodes import Node, PropertyNode
from ..items.bound import BoundData


class NSDData (BoundData):
    pass


class ZoneData (BoundData):
    def template(self):
        return Node(
            'zone',
            PropertyNode('name', '"example.com"'),
            PropertyNode('file', '"example.com.zone"'),
        )


def quote(x): return '"%s"' % x
def unquote(x): return x.strip('"')


NSDData.bind_collection(
    'zones', selector=lambda x: x.name == 'zone', item_class=ZoneData)
ZoneData.bind_property('name', 'name', getter=unquote, setter=quote)
ZoneData.bind_property('zonefile', 'file', getter=unquote, setter=quote)
