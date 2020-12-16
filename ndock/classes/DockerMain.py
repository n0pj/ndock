import subprocess

from .Color import Color


class DockerMain:
    def __init__(self):
        pass

    def call(self, command):
        eval(f'self.{command}()')

    # def setup(self):
    #     try:
    #         subprocess.check_call(
    #             'export UID && docker-compose -f ndock/ndock.yml up -d', shell=True)
    #         print(Color.green('ndock setup now...'))
    #     except Exception:
    #         print(Color.red('Fatal Error.'))

    def stop(self):
        try:
            print(Color.green('Stop main...'))
            subprocess.check_call(
                'docker-compose -f docker/main.yml down', shell=True)
            print('Stop main ... ' + Color.green('done'))

        except Exception:
            print(Color.red('Fatal Error.'))

    def start(self):

        try:
            print(Color.green('Start main...'))
            subprocess.check_call(
                'docker-compose -f docker/main.yml up -d', shell=True)
            print('Start main ... ' + Color.green('done'))

        except Exception:
            print(Color.red('Fatal Error.'))
