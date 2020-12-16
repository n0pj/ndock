import subprocess

from .Color import Color


class DockerMain:
    def __init__(self):
        pass

    def call(self, command):
        eval(f'self.{command}()')

    def setup(self):
        try:
            subprocess.check_call(
                'docker-compose -f ndock/ndock.yml up -d', shell=True)
            print(Color.green('ndock setup now...'))
        except Exception:
            print(Color.red('Fatal Error.'))

    def stop(self):
        try:
            subprocess.check_call(
                'docker-compose -f ndock/ndock.yml down', shell=True)
            print(Color.green('ndock downed...'))

        except Exception:
            print(Color.red('Fatal Error.'))

    def start(self):
        pass
