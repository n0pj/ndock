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
            with open('.env', 'w') as env:
                # uid = subprocess.run('id -u', stdout=env, shell=True)
                uid_bytes = subprocess.check_output('id -u', shell=True)
                uid_str = uid_bytes.decode()
                uid_str = f'UID={uid_str}'
                env.write(uid_str)

            print(Color.green('Start main...'))
            subprocess.check_call(
                'docker-compose -f docker/main.yml up -d', shell=True)
            print('Start main ... ' + Color.green('done'))

        except Exception:
            print(Color.red('Fatal Error.'))
