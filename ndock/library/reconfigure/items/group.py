from ..nodes import Node, PropertyNode
from ..items.bound import BoundData


class GroupsData (BoundData):
    pass


class GroupData (BoundData):
    fields = ['name', 'password', 'gid', 'users']

    def template(self):
        return Node(
            'line',
            *[
                Node('token', children=[
                    PropertyNode('value', '')
                ])
                for x in GroupData.fields
            ]
        )


GroupsData.bind_collection('groups', item_class=GroupData)
for i in range(0, len(GroupData.fields)):
    def path(i): return lambda x: x.children[i]
    GroupData.bind_property('value', GroupData.fields[i], path=path(i))
