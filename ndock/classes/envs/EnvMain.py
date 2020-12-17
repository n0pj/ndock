import subprocess
import os
from ndock.classes.Color import Color


class EnvMain:
    def __init__(self):
        pass

    def call(self, command, **kwargs):
        eval(f'self.{command}(**{kwargs})')

    # def setup(self):
    #     try:
    #         subprocess.check_call(
    #             'export UID && docker-compose -f ndock/ndock.yml up -d', shell=True)
    #         print(Color.green('ndock setup now...'))
    #     except Exception:
    #         print(Color.red('Fatal Error.'))

    def stop(self, **kwargs):
        try:
            print(Color.green('Stop main...'))
            subprocess.check_call(
                'docker-compose -f docker/main.yml stop', shell=True)
            print('Stop main ... ' + Color.green('done'))

        except Exception:
            print(Color.red('Fatal Error.'))

    def down(self, **kwargs):
        try:
            print(Color.green('Stop main...'))
            subprocess.check_call(
                'docker-compose -f docker/main.yml down --rmi all', shell=True)
            print('Stop main ... ' + Color.green('done'))

        except Exception:
            print(Color.red('Fatal Error.'))

    def start(self, **kwargs):

        try:
            print(Color.green('Start main...'))
            subprocess.check_call(
                'docker-compose -f docker/main.yml up -d', shell=True)
            print('Start main ... ' + Color.green('done'))

        except Exception:
            print(Color.red('Fatal Error.'))

    def clone(self, **kwargs):
        url = kwargs.get('url')
        branch = kwargs.get('branch')

        if not url:
            print(Color.red('Expected -u, --url uption.'))
            print(Color.red('Fatal Error.'))
            exit()

        branch = branch if branch else 'main'

        cwd = os.getcwd()
        os.chdir('volumes/www/')

        try:
            print(Color.green('Start main...'))
            subprocess.check_call(
                f'git clone -b {branch} {url}', shell=True)
            print('Start main ... ' + Color.green('done'))
            os.chdir(cwd)

        except Exception:
            print(Color.red('Fatal Error.'))
            os.chdir(cwd)
