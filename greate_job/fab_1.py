from fabric.api import run, env, sudo

env.hosts = ['root@192.168.73.143']  # ssh要用到的参数
env.password = 'zhou199567'


def host_type():
    run('uname -s')


def host():
    run('hostname')


def ls(path='.'):
    run('ls {}'.format(path))


def tail(path='/etc/passwd', line=10):
    sudo('tail -n{0} {1}'.format(line, path))


def main():
    host_type()
    host()
    tail()
    ls()


if __name__ == '__main__':
    main()
