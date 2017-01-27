WOCAT
==============================

World Overview of Conservation Approaches and Technologies


Settings
------------
* POSTGRES_USER: User for postgres database
* POSTGRES_PASSWORD: Password for postgres database
* DJANGO_ADMIN_URL: URL of Django admin interface
* DJANGO_SETTINGS_MODULE: Python path syntax to django settings module
* DJANGO_SECRET_KEY: A secret key for a particular Django installation
* DJANGO_ALLOWED_HOSTS: A list of strings representing the host/domain names that this Django site can serve
* DJANGO_SERVER_EMAIL: The email address that error messages come from
* DJANGO_ACCOUNT_ALLOW_REGISTRATION: Allow registration of new users (default True)
* DJANGO_SENTRY_DSN: DSN for Sentry error tracking
* ELASTICSEARCH_BACKEND: Elasticsearch backend
* ELASTICSEARCH_URL: Elasticsearch URL
* NEWSLETTER_API_KEY: Mailchimp API Key
* NEWSLETTER_LIST_ID: Mailchimp List ID

Requirements
------------

* Python >= 3.0
* Elasticsearch/Tika
* CAS/QCAT

Installation
------------


1. Create and activate virtualenv (optional)

.. code-block:: bash
   $ virtualenv customenv
   $ source customenv/bin/activate

2. Install requirements

.. code-block:: bash

    $ pip install -r requirements/local.txt
    or for production:
    $ pip install -r requirements/production.txt


3. Install database (Postgres)

.. code-block:: sql

  $ psql -d database_name -c "create role <USER> with password <PASSWORD>";
  $ psql -d database_name -c "create database <DATABASE> with owner <USER>";
  $ python manage.py migrate

4. Copy „env.example“ to „.env“, adapt settings

5. Collect static files (required only for deployment server)

.. code-block:: bash

  $ python manage.py collectstatic --no-input

5. Run server

.. code-block:: bash

  $ python manage.py runserver

Deployment
----------

Deployment requires SSH access to the deployment server without password using SSH keychain. We recommend using fabric to pull code, update new requirements, collect static files, compile translations and migrate the database.

.. code-block:: bash

  # for development:
  $ fab development deploy 
  # for staging:
  $ fab staging deploy
  # for production:
  $ fab production deploy


Update of packages
------------------


.. code-block:: bash

  $ pip install -rU requirements.txt

CAS and QCAT
------------

The project requires:

* CAS running at https://wocat.net/cas/ (using https://github.com/jbittel/django-mama-cas)
* QCAT running at https://qcat.wocat.net/en/wocat/ (using https://github.com/CDE-UNIBE/qcat/tree/feature/1055-new-authentication and https://github.com/mingchen/django-cas-ng)

Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

Import users from CSV
^^^^^^^^^^^^^^^^^^^^^

To import users from CSV use this command:

.. code-block:: bash

    $ python ../manage.py import_users_data /path/to/institutions.csv /path/to/users.csv

The CSV file specs are (sample file: )

* encoding: UTF-8
* delimiter: ";"
* quoting: 
* escape character:

Attention: Please check before the import again whether the data basis is clean, especially regarding the institutes!

Rebuild search index
^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    $ ./manage.py update_index [--backend <backend name>]

This command rebuilds the search index from scratch. It is only required when using Elasticsearch.

It is recommended to run this command once a week and at the following times:

whenever any pages have been created through a script (after an import, for example)
whenever any changes have been made to models or search configuration
The search may not return any results while this command is running, so avoid running it at peak times.

.. code-block:: bash

    $ ./manage.py search_garbage_collect

Wagtail keeps a log of search queries that are popular on your website. On high traffic websites, this log may get big and you may want to clean out old search queries. This command cleans out all search query logs that are more than one week old (or a number of days configurable through the WAGTAILSEARCH_HITS_MAX_AGE setting).

LESS to CSS compilation
^^^^^^^^^^^^^^^^^^^^^^^

The style sheets are written in LESS. They will be compiled to a single CSS file by *$ lessc* while running Fabric. See *compile_less()* in *fabfile.py*.

Sentry
^^^^^^

Sentry is an error logging aggregator service. You can sign up for a free account at http://getsentry.com or download and host it yourself.
The system is setup with reasonable defaults, including 404 logging and integration with the WSGI application.

You must set the DSN url in production.