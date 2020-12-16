import json


class JSON:
    def __init__(self):
        pass

    def load(self, path):
        with open(path) as f:
            json_dict = json.load(f)

        return json_dict
