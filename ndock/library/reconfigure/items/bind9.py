from ..nodes import Node, PropertyNode
from ..items.bound import BoundData


class BIND9Data (BoundData):
    pass


class ZoneData (BoundData):
    def template(self):
        return Node(
            'zone',
            PropertyNode('type', 'master'),
            PropertyNode('file', 'db.example.com'),
            parameter='"example.com"',
        )


def quote(x): return '"%s"' % x
def unquote(x): return x.strip('"')


BIND9Data.bind_collection(
    'zones', selector=lambda x: x.name == 'zone', item_class=ZoneData)
ZoneData.bind_attribute('parameter', 'name', getter=unquote, setter=quote)
ZoneData.bind_property('type', 'type')
ZoneData.bind_property('file', 'file', getter=unquote, setter=quote)
