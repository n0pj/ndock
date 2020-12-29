import subprocess
import os
from ndock.classes.Color import Color
from ndock.classes.Loader import Loader
from ndock.classes.Parser import Parser
# from ndock.library.nginxparser_eb import load, dump, UnspacedList
from pprint import pprint
import ndock.library.crossplane057 as crossplane


class EnvMain:
    www_dir: str = 'volumes/www'

    def __init__(self):
        pass

    def call(self, command, **kwargs):
        self.generate_yaml()
        eval(f'self.{command}(**{kwargs})')

    # def setup(self):
    #     try:
    #         subprocess.check_call(
    #             'export UID && docker-compose -f ndock/ndock.yml up -d', shell=True)
    #         print(Color.green('ndock setup now...'))
    #     except Exception:
    #         print(Color.red('Fatal Error.'))

    def generate_yaml(self):
        default_yaml: object = Loader.load_yaml('docker/default.yaml')
        settings: object = Loader.load_yaml('settings.yaml')
        docker_settings: object = settings['docker_settings']
        # print(docker_settings)
        services = default_yaml['services']

        # print(docker_settings)
        for key, setting in docker_settings.items():
            use = setting['use']
            # print(setting)
            if not use:
                del services[key]

        # print(default_yaml)
        Loader.save_yaml(default_yaml, 'docker/main.yaml')
        print('Generate yaml ... ' + Color.green('done'))

    def analyze_with_generate_nginx_conf(self):
        www_dir_list = os.listdir(self.www_dir)
        www_dir_count = len(www_dir_list)
        # nginx_conf = load(open('docker/images/nginx/test.conf'))
        # print(type(nginx_conf))
        # nginx_conf = list(nginx_conf)
        # print(type(nginx_conf))
        # nginx_conf = dict(nginx_conf)
        # print(type(nginx_conf))
        # print(nginx_conf)

        payload = crossplane.parse('docker/images/nginx/default.conf')
        # print(payload)
        parsed_config = payload['config'][0]['parsed']
        http_block = parsed_config[0]['block']
        server_block = http_block[0]['block']

        root_block = Parser.search_directive('root', server_block)
        location_blocks = []
        root_args = ['/var/www/']
        if www_dir_count == 0:
            pass
        elif www_dir_count == 1:
            root_args = ['/var/www/' + www_dir_list[0]]
        else:
            for name in www_dir_list:

                # print(name)
                # location_blocks_args = ['/var/www/' + name]
                location_blocks_args = ['/var/www']
                location_blocks.append(
                    {
                        # 'args': [f'/{name}'],
                        'args': [f'/{name}'],
                        'directive': 'location',
                        'block': [
                            {
                                'directive': 'root',
                                'args': location_blocks_args
                            }
                        ]
                    }
                )

        root_block['args'] = root_args

        root_block = [root_block]

        new_server_block = Parser.insert_block(
            root_block, server_block, 'root'
        )

        new_server_block = Parser.insert_block(
            location_blocks, new_server_block
        )

        if location_blocks:
            new_server_block = Parser.insert_block(
                [], new_server_block, 'root'
            )
        # print(new_server_block)

        # parsed_config[0]['block'][0]['block'] = new_server_block

        new_server_block = [
            {
                'directive': 'server',
                'args': [],
                'block': new_server_block
            }
        ]

        build_config = crossplane.build(new_server_block)
        # pprint(build_config)

        with open('docker/images/nginx/main.conf', 'w') as f:
            f.write(build_config)
            print('Generate nginx conf ... ' + Color.green('done'))

    def copy_nginx_conf(self):
        payload = crossplane.parse('docker/images/nginx/default.conf')
        parsed_config = payload['config'][0]['parsed']
        http_block = parsed_config[0]['block']
        server_block = http_block[0]['block']

        new_server_block = [
            {
                'directive': 'server',
                'args': [],
                'block': server_block
            }
        ]

        build_config = crossplane.build(new_server_block)

        with open('docker/images/nginx/main.conf', 'w') as f:
            f.write(build_config)
            print('Copy nginx conf ... ' + Color.green('done'))

    def stop(self, **kwargs):
        try:
            print(Color.green('Stop main...'))
            subprocess.check_call(
                'docker-compose -f docker/main.yaml stop', shell=True)
            print('Stop main ... ' + Color.green('done'))

        except Exception:
            print(Color.red('Fatal Error.'))

    def down(self, **kwargs):
        try:
            print(Color.green('Stop main...'))
            subprocess.check_call(
                'docker-compose -f docker/main.yaml down --rmi all', shell=True)
            print('Stop main ... ' + Color.green('done'))

        except Exception:
            print(Color.red('Fatal Error.'))

    def start(self, **kwargs):
        settings_yaml = Loader.load_yaml()
        nginx_settings = settings_yaml['docker_settings']['nginx']

        if nginx_settings['parse_conf'] is True:
            self.analyze_with_generate_nginx_conf()
        else:
            self.copy_nginx_conf()
        try:
            print(Color.green('Start main...'))
            subprocess.check_call(
                'docker-compose -f docker/main.yaml up -d --remove-orphans', shell=True)
            print('Start main ... ' + Color.green('done'))

        except Exception:
            print(Color.red('Fatal Error.'))

    def build(self, **kwargs):
        settings_yaml = Loader.load_yaml()
        nginx_settings = settings_yaml['docker_settings']['nginx']

        if nginx_settings['parse_conf'] is True:
            self.analyze_with_generate_nginx_conf()
        else:
            self.copy_nginx_conf()
        try:
            print(Color.green('Build main...'))
            subprocess.check_call(
                'docker-compose -f docker/main.yaml build', shell=True)
            print('Build main ... ' + Color.green('done'))

        except Exception:
            print(Color.red('Fatal Error.'))

    def rm_db(self, **kwargs):
        settings_yaml = Loader.load_yaml()
        nginx_settings = settings_yaml['docker_settings']['nginx']

        if nginx_settings['parse_conf'] is True:
            self.analyze_with_generate_nginx_conf()
        else:
            self.copy_nginx_conf()
        try:
            print(Color.green('Remove main database ...'))
            subprocess.check_call(
                'sudo rm -rf volumes/mysql/pool/*', shell=True)
            print('Remove main database ... ' + Color.green('done'))

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
