from ..nodes import Node, PropertyNode
from ..items.bound import BoundData


class PasswdData (BoundData):
    pass


class UserData (BoundData):
    fields = ['name', 'password', 'uid', 'gid', 'comment', 'home', 'shell']

    def template(self):
        return Node(
            'line',
            *[
                Node('token', children=[
                    PropertyNode('value', '')
                ])
                for x in UserData.fields
            ]
        )


PasswdData.bind_collection('users', item_class=UserData)
for i in range(0, len(UserData.fields)):
    def path(i): return lambda x: x.children[i]
    UserData.bind_property('value', UserData.fields[i], path=path(i))
