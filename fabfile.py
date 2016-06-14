from fabric.api import cd, run, env
from fabvenv import virtualenv


def staging():
    env.name = 'staging'
    env.hosts = ['wocat@wocat.sinnwerkstatt.com']
    env.path = '/srv/wocat.sinnwerkstatt.com/wocat'
    env.virtualenv_path = '/srv/wocat.sinnwerkstatt.com/wocatenv'
    env.backup_path = '/srv/wocat.sinnwerkstatt.com/backups'
    env.push_branch = 'staging'
    env.push_remote = 'origin'
    env.reload_cmd = 'supervisorctl restart wocat'
    env.db_name = 'wocat'
    env.db_username = 'wocat'
    env.after_deploy_url = 'http://wocat.sinnwerkstatt.com'
    env.settings = '--settings=config.settings.production'
    env.requirements = 'requirements/production.txt'


def production():
    env.name = 'production'
    env.hosts = ['wocat@87.230.93.115']
    env.path = '/home/wocat/wocat'
    env.virtualenv_path = '/home/wocat/.virtualenvs/wocat'
    env.backup_path = '/home/wocat/backups'
    env.push_branch = 'master'
    env.push_remote = 'origin'
    env.reload_cmd = 'supervisorctl restart wocat'
    env.db_name = 'wocat'
    env.db_username = 'wocat'
    env.after_deploy_url = 'http://beta.wocat.de'
    env.settings = '--settings=config.settings.production'
    env.requirements = 'requirements/production.txt'


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
        run("lessc --clean-css %(path)s/wocat/static/less/wocat.less %(path)s/wocat/static/css/wocat.css" % env)


def ping():
    run(
        "echo %(after_deploy_url)s returned:  \>\>\>  $(curl --write-out %%{http_code} --silent --output /dev/null %(after_deploy_url)s)" % env)


def deploy():
    with cd(env.path):
        run("git pull %(push_remote)s %(push_branch)s" % env)
        compile_less()
        with virtualenv(env.virtualenv_path):
            run("pip install -Ur %(requirements)s" % env)
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
