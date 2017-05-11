"""
The existing fabfile is used for sinnwerkstatts hosting.
This fabfile follows the CDEs default structure to integrate with continuous
delivery.
"""
from os import environ
from contextlib import contextmanager

from fabric.api import cd, run, env
from fabric.context_managers import prefix
from fabric.decorators import task
from fabric.operations import require


ENVIRONMENTS = {
    'develop': {
        'host_string': environ['WOCAT_DEV_HOST'],
        'source_path': environ['WOCAT_DEV_PATH'],
        'virtualenv_path': environ['WOCAT_DEV_VIRTUALENV'],
        'git_remote': 'origin',
        'git_branch': 'develop',
        'requirements_file': 'requirements/base.txt',
        'touch_file': environ['WOCAT_DEV_TOUCH_FILE']
    },
    'master': {
        'host_string': environ['WOCAT_BETA_HOST'],
        'source_path': environ['WOCAT_BETA_PATH'],
        'virtualenv_path': environ['WOCAT_BETA_VIRTUALENV'],
        'git_remote': 'origin',
        'git_branch': 'master',
        'requirements_file': 'requirements/base.txt',
        'touch_file': environ['WOCAT_BETA_TOUCH_FILE']
    }
}


@task
def develop():
    setup_environment('develop')


@task
def master():
    setup_environment('master')


@task
def deploy():
    require('environment', provided_by=(develop, master, ))
    with cd(env.source_path):
        _set_maintenance('on')
        _update_source()
        _install_dependencies()
        _compile_less()
        _collectstatic()
        _migrate()
        _set_maintenance('off')


def _update_source():
    run("git pull %(git_remote)s %(git_branch)s" % env)


def _install_dependencies():
    with virtualenv():
        run("pip install -Ur %(requirements_file)s" % env)


def _compile_less():
    run("lessc wocat/static/less/wocat.less wocat/static/css/wocat.css")


def _collectstatic():
    with virtualenv():
        run("python manage.py collectstatic --noinput")


def _migrate():
    with virtualenv():
        run("python manage.py migrate")


def _set_maintenance(switch: str):
    with virtualenv():
        run("python manage.py maintenance %s" % switch)
    _reload_webserver()


def _reload_webserver():
    run('touch %(touch_file)s' % env)


def setup_environment(environment_name: str):
    """
    Set the proper environment and read the configured values.
    """
    env.environment = environment_name
    for option, value in ENVIRONMENTS[environment_name].items():
        setattr(env, option, value)


@contextmanager
def virtualenv():
    with prefix('source %(virtualenv_path)s' % env):
        yield
