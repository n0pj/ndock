from ndock.classes.NDock import NDock
import argparse


def main():
    ndock: object = NDock()
    # print('test')
    # print(ndock.load_yaml('./ndock.yml'))
    # yaml = ndock.load_yaml('./ndock.yml')
    # print(yaml['version'])
    # print(ndock.to_json(yaml))
    # json = ndock.to_json(yaml)
    parser = argparse.ArgumentParser()

    parser.add_argument('-e', '--env')
    parser.add_argument('-c', '--command')
    parser.add_argument('-u', '--url')
    parser.add_argument('-b', '--branch')

    args = parser.parse_args(args=None, namespace=None)

    env = args.env
    command = args.command
    url = args.url
    branch = args.branch
    # ndock.run(env, command, url=url, branch=branch)
    yaml = ndock.load_yaml('ndock/ndock.yml')
    yaml = ndock.load_yaml('docker/main.yml')

    string: str = 'test'
    print(string)
    # print(yaml)
    # yaml['services']['python']['tty'] = True
    # print(yaml)
    # yaml = ndock.save_yaml(yaml)


if(__name__ == '__main__'):
    main()
