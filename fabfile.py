from fabric.api import cd, run, env
from fabvenv import virtualenv


def staging():
    env.name = 'staging'
    env.hosts = ['wocat@wocat.sinnwerkstatt.com']
    env.path = '/srv/wocat.sinnwerkstatt.com/wocat'
    env.virtualenv_path = '/srv/wocat.sinnwerkstatt.com/wocatenv'
    env.backup_path = '/srv/ms-wissenschaft.sinnwerkstatt.com/backups'
    env.push_branch = 'staging'
    env.push_remote = 'origin'
    env.reload_cmd = 'supervisorctl restart ms-wissenschaft'
    env.db_name = 'mswissenschaft'
    env.db_username = 'mswissenschaft'
    env.after_deploy_url = 'http://ms-wissenschaft.sinnwerkstatt.com'
    env.settings = '--settings=config.settings.production'


def production():
    env.name = 'production'
    env.hosts = ['msw@87.230.93.115']
    env.path = '/home/msw/ms-wissenschaft'
    env.virtualenv_path = '/home/msw/.virtualenvs/msw'
    env.backup_path = '/home/msw/backups'
    env.push_branch = 'master'
    env.push_remote = 'origin'
    env.reload_cmd = 'supervisorctl restart msw'
    env.db_name = 'msw'
    env.db_username = 'msw'
    env.after_deploy_url = 'http://beta.ms-wissenschaft.de'
    env.settings = '--settings=config.settings.production'


def reload_webserver():
    run("%(reload_cmd)s" % env)


def migrate():
    with virtualenv(env.virtualenv_path):
        run("%(path)s/manage.py migrate %(settings)s" % env)


def recompile_cache():
    with virtualenv(env.virtualenv_path):
        run("rm -rf %(path)s/staticfiles/CACHE" % env)
        run("%(path)s/manage.py compress --force %(settings)s" % env)


def compile_less():
    with virtualenv(env.virtualenv_path):
        run("lessc --clean-css %(path)s/mswissenschaft/static/css/msw.less %(path)s/mswissenschaft/static/css/msw.css" % env)


def ping():
    run(
        "echo %(after_deploy_url)s returned:  \>\>\>  $(curl --write-out %%{http_code} --silent --output /dev/null %(after_deploy_url)s)" % env)


def deploy():
    with cd(env.path):
        run("git pull %(push_remote)s %(push_branch)s" % env)
        compile_less()
        with virtualenv(env.virtualenv_path):
            run("pip install -Ur requirements.txt")
            run("./manage.py collectstatic --noinput %(settings)s" % env)
            run("./manage.py compilemessages %(settings)s" % env)

    migrate()
    reload_webserver()
    ping()


def init_fixtures():
    with virtualenv(env.virtualenv_path):
        run("%(path)s/manage.py loaddata init.json" % env)


def update():
    ''' Only deploy and reload modules from git, do no installing or migrating'''
    with cd(env.path):
        run("git pull %(push_remote)s %(push_branch)s" % env)

    reload_webserver()


def backup():
    with cd(env.backup_path):
        run("pg_dump -U %(db_username)s %(db_name)s > %(db_name)s_backup_$(date +%%F-%%T).sql" % env)
        run("ls -lt")
