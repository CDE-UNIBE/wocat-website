WOCAT
==============================

World Overview of Conservation Approaches and Technologies


Settings (defined in .env)
--------------------------
* POSTGRES_USER: User for postgres database
* POSTGRES_PASSWORD: Password for postgres database
* DJANGO_ADMIN_URL: URL of Django admin interface
* DJANGO_SETTINGS_MODULE: Python path syntax to django settings module
* DJANGO_SECRET_KEY: A secret key for a particular Django installation
* DJANGO_ALLOWED_HOSTS: A list of strings representing the host/domain names that this Django site can serve
* DJANGO_ACCOUNT_ALLOW_REGISTRATION: Allow registration of new users (default True)
* DJANGO_SENTRY_DSN: DSN for Sentry error tracking
* WAGTAILSEARCH_BACKEND: 'db' for regular Psql, 'elasticsearch' or 'elasticsearch2' for ES1 or 2.
* ELASTICSEARCH_URL: Elasticsearch URL
* NEWSLETTER_API_KEY: Mailchimp API Key
* NEWSLETTER_LIST_ID: Mailchimp List ID
* DJANGO_EMAIL_HOST: The host to use for sending email
* DJANGO_EMAIL_HOST_USER: Username to use for the SMTP server
* DJANGO_EMAIL_HOST_PASSWORD: Password to use for the SMTP server
* DJANGO_EMAIL_PORT: Port to use for the SMTP server
* DJANGO_EMAIL_USE_TLS: Whether to use a TLS (secure) connection when talking to the SMTP server
* DJANGO_EMAIL_USE_SSL: Whether to use an implicit TLS (secure) connection when talking to the SMTP server
* DJANGO_DEFAULT_FROM_EMAIL: Default email address to use for various automated correspondence from the site manager(s)
* DJANGO_SERVER_EMAIL: The email address that error messages come from

Requirements
------------

* Python >= 3.0
* Elasticsearch/Tika
* CAS

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

Central Authentication Service (CAS)
------------------------------------

To use a single sign on for Qcat and Wocat, we agreed on using CAS.
To use CAS with Django, we set up [Mama CAS](https://github.com/jbittel/django-mama-cas) server on our side
and any other service wanting to facilitate this server can use [django-cas-ng](https://github.com/mingchen/django-cas-ng) to connect.
The setup is straight forward and by following the tutorials on each services side, it's up and running in ~5min.
Sebastian Manger already made [a branch for qcat](https://github.com/CDE-UNIBE/qcat/tree/feature/1055-new-authentication)

Newsletter
----------

Create mailchimp list
^^^^^^^^^^^^^^^^^^^^^

The project uses `mailchimp`: https://mailchimp.com/

https://login.mailchimp.com/signup
Please follow their instructions on how to setup an account and create a list.
Both the api key and list id need to be set in order for the integration to work.
(please see settings section for respective environment variable setup)

Import users to list
^^^^^^^^^^^^^^^^^^^^

There is a newsletter management interface to create a filtered list of users, that can be pasted into the mailchimp list.

1. Go to https://example.com/newsletter/management/
2. Select filters and copy output to clipboard
3. Go to mailchimp list, under „Add contacts“ select „Import contacts“
4. Select „Copy/paste from file“ and paste from clipboard
5. Match columns and import


Register unsubscribe webhook
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To synchronize the newsletter flag upon unsubscription via newsletter email link a webhook needs to be registered.
http://kb.mailchimp.com/integrations/api-integrations/how-to-set-up-webhooks

1. Go to mailchimp list
2. Under „Settings“ select „Webhooks“
3. Select „Create new webhook“ and paste URL: https://example.com/newsletter/unsubscribe/
4. Select only the checkbox for „Unsubscribes“ and save

Elasticsearch
-------------
To use Elasticsearch as a search-backend, it suffices to just set it up (through your distributions package management) and change the WAGTAILSEARCH_BACKEND-variable accordinly.
As of writing this, a feature for indexing PDFs and other documents has not made it into upstream wagtail (https://github.com/wagtail/wagtail/pull/3028) . Once this feature is merged,
we can retroactively index all uploaded documents. (The index engine for ElasticSearch is based on [Tika](https://tika.apache.org/) and can therefore index anything Tika can.)


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

    $ python manage.py import_users_data /path/to/institutions.csv /path/to/users.csv

The CSV file specs are (check samples files in /import folder)

* encoding: UTF-8
* delimiter: ";"
* quoting:
* escape character:

Attention: Please check before the import again whether the data basis is clean, especially regarding the institutes!

Send reset password link to users
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

After the final import of the users, they are informed by e-mail that they have to re-assign their password.
This mail to the user contains a personal link, which allows you to set a password directly (without having to go through the password-forgotten function).
The mail is therefore sent by the CMS, implemented here for a command which triggers the emails:

.. code-block:: bash

    $ python manage.py send_user_password_reset_links


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

    $ python manage.py search_garbage_collect

Wagtail keeps a log of search queries that are popular on your website. On high traffic websites, this log may get big and you may want to clean out old search queries. This command cleans out all search query logs that are more than one week old (or a number of days configurable through the WAGTAILSEARCH_HITS_MAX_AGE setting).

LESS to CSS compilation
^^^^^^^^^^^^^^^^^^^^^^^

The style sheets are written in LESS. They will be compiled to a single CSS file by *$ lessc* while running Fabric. See *compile_less()* in *fabfile.py*.

Sentry
^^^^^^

Sentry is an error logging aggregator service. You can sign up for a free account at http://getsentry.com or download and host it yourself.
The system is setup with reasonable defaults, including 404 logging and integration with the WSGI application.

You must set the DSN url in production.
