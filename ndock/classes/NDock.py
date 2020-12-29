from .Color import Color
from .envs.EnvNDock import EnvNDock
from .envs.EnvAny import EnvAny
from .envs.EnvMain import EnvMain
from .Loader import Loader
from typing import Union
import subprocess
# from ndock.library.dotenv.main import load_dotenv
import ndock.library.dotenv0150 as dotenv
import os


class NDock:
    ENVS_JSON_PATH: str = 'ndock/settings/envs.json'
    COMMANDS_JSON_PATH: str = 'ndock/settings/commands.json'
    ALLOW_COMMANDS_JSON_PATH: str = 'ndock/settings/allow_commands.json'
    NDOCK_DOTENV_PATH: str = '.env'

    env: Union[str, None] = None
    command: Union[str, None] = None
    yaml_path: str = ''

    def __init__(self) -> None:
        print(Color.green('Starting ndock initialize...'))

    def __del__(self) -> None:
        print(Color.green('Ended ndock...'))

    def set_env(self, specify_env):
        envs = Loader.load_json(self.ENVS_JSON_PATH)

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
        commands = Loader.load_json(self.COMMANDS_JSON_PATH)

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
        allow_envs = Loader.load_json(self.ENVS_JSON_PATH)
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
        allow_command_envs = Loader.load_json(self.ALLOW_COMMANDS_JSON_PATH)
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
            envs = Loader.load_json(self.ENVS_JSON_PATH)
            if specify_env is None:
                if dotenv.get('DEFAULT_ENV'):
                    return dotenv.get('DEFAULT_ENV')
                return envs[0]
            else:
                return specify_env

        if arg == 'command':
            specify_command = val
            commands = Loader.load_json(self.COMMANDS_JSON_PATH)
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
