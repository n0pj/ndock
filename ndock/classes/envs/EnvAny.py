import subprocess

from ndock.classes.Color import Color


class EnvAny:
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
            print(Color.green('Stop any...'))
            subprocess.check_call(
                'docker stop `docker ps -a -q`', shell=True)
            print('Stop any ... ' + Color.green('done'))

        except Exception:
            print(Color.red('Fatal Error.'))

    def rm_all(self):
        try:
            print(Color.green('Stop any...'))
            subprocess.check_call(
                'docker rm `docker ps -a -q`', shell=True)
            print('Stop any ... ' + Color.green('done'))

        except Exception:
            print(Color.red('Fatal Error.'))

    def rmi_all(self):
        try:
            print(Color.green('Stop any...'))
            subprocess.check_call(
                'docker rmi `docker images -q`', shell=True)
            print('Stop any ... ' + Color.green('done'))

        except Exception:
            print(Color.red('Fatal Error.'))

    def rmi_force_all(self):
        try:
            print(Color.green('Stop any...'))
            subprocess.check_call(
                'docker rmi -f `docker images -q`', shell=True)
            print('Stop any ... ' + Color.green('done'))

        except Exception:
            print(Color.red('Fatal Error.'))

    def remove_all(self):
        try:
            print(Color.green('Stop any...'))
            subprocess.check_call(
                'docker rm `docker ps -a -q`', shell=True)
            print('Stop any ... ' + Color.green('done'))

        except Exception:
            print(Color.red('Fatal Error.'))
