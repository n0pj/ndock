# import yaml
import ndock.library.yaml531 as yaml
import json
from .Color import Color
# from ndock.library.dotenv.main import load_dotenv
import ndock.library.dotenv0150 as dotenv
import os


class Loader:
    ENVS_JSON_PATH = 'ndock/settings/envs.json'
    COMMANDS_JSON_PATH = 'ndock/settings/commands.json'
    ALLOW_COMMANDS_JSON_PATH = 'ndock/settings/allow_commands.json'
    NDOCK_DOTENV_PATH = '.env'
    DEFAULT_SETTINGS_YAML_PATH = 'settings.yaml'

    env = None
    command = None
    yaml_path = ''

    def __init__(self) -> None:
        pass
        # print(Color.green('Starting ndock initialize...'))

    def __del__(self) -> None:
        pass
        # print(Color.green('Ended ndock...'))

    @classmethod
    def load_yaml(cls, path=None) -> dict:
        path = path if path else cls.DEFAULT_SETTINGS_YAML_PATH
        cls.yaml_path = path

        with open(path) as file:
            yml = yaml.load(file, Loader=yaml.SafeLoader)
            return yml

    @classmethod
    def save_yaml(cls, yml, path=None) -> bool:
        path = path if path else cls.yaml_path

        with open(path, 'w') as file:
            yml = yaml.dump(yml, file)
            return yml

    @classmethod
    def load_json(cls, path) -> dict:
        with open(path) as f:
            json_dict = json.load(f)

        return json_dict

    def to_json(self, yml) -> str:
        json_obj = json.dumps(yml, indent=2)
        return json_obj

    def to_yaml(self, yml):
        if not yml:
            return False

        json_obj = json.dumps(yml, indent=2)
        return json_obj

    @classmethod
    def load_dotenv(cls, path=''):
        dotenv.load_dotenv(verbose=True)
        dotenv.load_dotenv(path)
        return os.environ
        # UID = os.environ.get('UID')
        # print('current: ' + UID)
