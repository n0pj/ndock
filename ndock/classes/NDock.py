import yaml
import json
from .Color import Color
from .DockerNDock import DockerNDock
from .DockerMain import DockerMain
import subprocess


class NDock:
    ENVS_JSON_PATH = 'ndock/settings/envs.json'
    COMMANDS_JSON_PATH = 'ndock/settings/commands.json'
    ALLOW_COMMANDS_JSON_PATH = 'ndock/settings/allow_commands.json'

    env = None
    command = None

    def __init__(self):
        print(Color.green('Starting ndock initialize...'))

    def __del__(self):
        print(Color.green('Ended ndock...'))

    def load_yaml(self, path):
        if not path:
            return False

        with open(path)as file:
            yml = yaml.load(file, Loader=yaml.SafeLoader)
            return yml

    def load_json(self, path):
        with open(path) as f:
            json_dict = json.load(f)

        return json_dict

    def to_json(self, yml):
        if not yml:
            return False

        json_obj = json.dumps(yml, indent=2)
        return json_obj

    def to_yaml(self, yml):
        if not yml:
            return False

        json_obj = json.dumps(yml, indent=2)
        return json_obj

    def set_env(self, specify_env):
        envs = self.load_json(self.ENVS_JSON_PATH)
        if specify_env is None:
            specify_env = envs[0]

        if specify_env in envs:
            self.env = specify_env
            print(Color.cyan(f'Set current env is {self.env}.'))
            return self.env

        else:
            self.env = envs[0]
            print(Color.red(f'Undefined env {specify_env}.'))
            print(Color.cyan(f'Set current env is {self.env}.'))
            return self.env

    def set_command(self, specify_command):
        commands = self.load_json(self.COMMANDS_JSON_PATH)
        if specify_command is None:
            specify_command = commands[0]

        if specify_command in commands:
            self.command = specify_command
            print(Color.cyan(f'Set current command is {self.command}.'))
            return self.command

        else:
            self.command = commands[0]
            print(Color.red(f'Undefined command {specify_command}.'))
            print(Color.cyan(f'Set current command is {self.command}.'))
            return self.command

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

    def run(self):
        is_confirm = self.confirm_command()

        if not is_confirm:
            print(Color.red('Error, ndock exited.'))
            exit()

        env = self.env
        # command = self.command
        eval(f'self.docker_{env}()')

    def docker_ndock(self):

        docker = DockerNDock()
        docker.call(self.command)

    def docker_main(self):
        docker = DockerMain()
        docker.call(self.command)
        pass

    def generate_env(self):
        with open('.env', 'w') as env:
            # uid = subprocess.run('id -u', stdout=env, shell=True)
            uid_bytes = subprocess.check_output('id -u', shell=True)
            uid_str = uid_bytes.decode()
            uid_str = f'UID={uid_str}'
            env.write(uid_str)
