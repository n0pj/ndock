# import yaml
import ndock.library.yaml531 as yaml
import json
from .Color import Color
from .envs.EnvNDock import EnvNDock
from .envs.EnvAny import EnvAny
from .envs.EnvMain import EnvMain
import subprocess
# from ndock.library.dotenv.main import load_dotenv
import ndock.library.dotenv0150 as dotenv
import os


class NDock:
    ENVS_JSON_PATH = 'ndock/settings/envs.json'
    COMMANDS_JSON_PATH = 'ndock/settings/commands.json'
    ALLOW_COMMANDS_JSON_PATH = 'ndock/settings/allow_commands.json'
    NDOCK_DOTENV_PATH = '.env'

    env = None
    command = None
    yaml_path = ''

    def __init__(self) -> None:
        print(Color.green('Starting ndock initialize...'))

    def __del__(self) -> None:
        print(Color.green('Ended ndock...'))

    def load_yaml(self, path) -> dict:
        self.yaml_path = path

        with open(path) as file:
            yml = yaml.load(file, Loader=yaml.SafeLoader)
            return yml

    def save_yaml(self, yml) -> bool:
        path = self.yaml_path

        with open(path, 'w') as file:
            yml = yaml.dump(yml, file)
            return yml

    def load_json(self, path) -> dict:
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

    def set_env(self, specify_env):
        envs = self.load_json(self.ENVS_JSON_PATH)

        specify_env = self.parse_dotenv('env', specify_env)
        is_confirm = False

        if specify_env in envs:
            self.env = specify_env
            print(Color.cyan(f'Set current env is {self.env}.'))

        else:
            self.env = specify_env
            print(Color.red(f'Undefined env {self.env}.'))
            print(Color.cyan(f'Set current env is {self.env}.'))

        # no command
        is_confirm = self.confirm_env()
        if not is_confirm:
            print(Color.red('Error, ndock exited.'))
            exit()
        return self.env

    def set_command(self, specify_command):
        commands = self.load_json(self.COMMANDS_JSON_PATH)

        specify_command = self.parse_dotenv('command', specify_command)
        is_confirm = False

        if specify_command is None:
            specify_command = commands[0]

        if specify_command in commands:
            self.command = specify_command
            print(Color.cyan(f'Set current command is {self.command}.'))

        else:
            self.command = specify_command
            print(Color.red(f'Undefined command {self.command}.'))
            print(Color.cyan(f'Set current command is {self.command}.'))

        # no command
        is_confirm = self.confirm_command()
        if not is_confirm:
            print(Color.red('Error, ndock exited.'))
            exit()
        return self.command

    def confirm_env(self):
        env = self.env
        allow_envs = self.load_json(self.ENVS_JSON_PATH)
        if env in allow_envs:
            print('Confirm env ... ' + Color.green('done'))
            return True
        else:
            print('Confirm env ... ' + Color.red('fail'))
            print(Color.red(f'Undefined env {env}.'))
            return False

    def confirm_command(self):
        env = self.env
        command = self.command
        allow_command_envs = self.load_json(self.ALLOW_COMMANDS_JSON_PATH)
        allow_commands_env = allow_command_envs[env]
        allow_commands = allow_commands_env['allow_commands']
        if command in allow_commands:
            print('Confirm command ... ' + Color.green('done'))
            return True
        else:
            print('Confirm command ... ' + Color.red('fail'))
            print(
                Color.red(f'Not permitted command this env: {env}'))
            print(Color.red(f'Can use commands: {allow_commands}'))
            return False

    def run(self, env, command, **kwargs):
        # command = self.command
        url = kwargs.get('url')
        self.set_env(env)
        self.set_command(command)
        env = self.env
        self.generate_dotenv()
        eval(f'self.docker_{env}(**{kwargs})')

    def docker_ndock(self, **kwargs):
        docker = EnvNDock()
        docker.call(self.command)

    def docker_any(self, **kwargs):
        docker = EnvAny()
        docker.call(self.command)

    def docker_main(self, **kwargs):
        docker = EnvMain()
        docker.call(self.command, **kwargs)

    def generate_dotenv(self):
        uid_bytes = subprocess.check_output('id -u', shell=True)
        uid_str = uid_bytes.decode()
        self.set_dotenv(self.NDOCK_DOTENV_PATH, 'UID', uid_str)

    def parse_dotenv(self, arg, val):
        dotenv = self.load_dotenv(self.NDOCK_DOTENV_PATH)
        if arg == 'env':
            specify_env = val
            envs = self.load_json(self.ENVS_JSON_PATH)
            if specify_env is None:
                if dotenv.get('DEFAULT_ENV'):
                    return dotenv.get('DEFAULT_ENV')
                return envs[0]
            else:
                return specify_env

        if arg == 'command':
            specify_command = val
            commands = self.load_json(self.COMMANDS_JSON_PATH)
            if specify_command is None:
                if dotenv.get('DEFAULT_COMMAND'):
                    return dotenv.get('DEFAULT_COMMAND')
                return commands[0]
            else:
                return specify_command

    def load_dotenv(self, path=''):
        dotenv.load_dotenv(verbose=True)
        dotenv.load_dotenv(path)
        return os.environ
        # UID = os.environ.get('UID')
        # print('current: ' + UID)

    def set_dotenv(self, path, key, value):
        value_str = str(value)
        value_str = value.replace('\n', '')

        dotenv.set_key(path, key_to_set=key, value_to_set=value_str)
        # UID = os.environ.get('UID')
        # print('current: ' + UID)
