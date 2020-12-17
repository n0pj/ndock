import subprocess

from ndock.classes.Color import Color


class EnvNDock:
    def __init__(self):
        pass

    def call(self, command):
        eval(f'self.{command}()')

    def setup(self):
        print(Color.green('Starting DockerNDock setup ...'))
        try:
            subprocess.check_call(
                'docker-compose -f ndock/ndock.yml up -d', shell=True)
            print('Setup ndock ... ' + Color.green('done'))
        except Exception:
            print(Color.red('Fatal Error.'))

    def stop(self):
        try:
            subprocess.check_call(
                'docker-compose -f ndock/ndock.yml down', shell=True)
            print(Color.green('Downed ndock ... '))

        except Exception:
            print(Color.red('Fatal Error.'))

    def start(self):
        pass
