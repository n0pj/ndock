from ndock.classes.NDock import NDock
import argparse


def main():
    ndock = NDock()
    # print('test')
    # print(ndock.load_yaml('./ndock.yml'))
    # yaml = ndock.load_yaml('./ndock.yml')
    # print(yaml['version'])
    # print(ndock.to_json(yaml))
    # json = ndock.to_json(yaml)
    parser = argparse.ArgumentParser()

    parser.add_argument('-e', '--env')
    parser.add_argument('-c', '--command')

    args = parser.parse_args(args=None, namespace=None)

    env = args.env
    command = args.command
    ndock.run(env, command)
    yaml = ndock.load_yaml('ndock/ndock.yml')
    yaml = ndock.load_yaml('docker/main.yml')
    # print(yaml)
    # yaml['services']['python']['tty'] = True
    # print(yaml)
    # yaml = ndock.save_yaml(yaml)


if(__name__ == '__main__'):
    main()
