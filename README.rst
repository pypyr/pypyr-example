###############################################
Examples of using the pypyr cli pipeline runner
###############################################

.. image:: https://cdn.345.systems/wp-content/uploads/2017/03/pypyr-logo-small.png
    :alt: pypyr-logo
    :align: left


pypyr is a command line interface to run pipelines defined in yaml. These
examples show you how to code your own custom steps for the pipeline processor.
It also shows you some example pipeline definition yaml files.

.. contents::

.. section-numbering::

Installation
============
.. code-block:: bash

  $ pip install pypyr


Usage
=====
Run a simple example
--------------------
In the repo root, run:

.. code-block:: bash

  # run the pipelines/simple.yaml pipeline with INFO log level.
  $ pypyr simple

  # run the pipelines/simple.yaml pipeline with the default DEBUG log level.
  # this will give you all the gory details.
  $ pypyr simple --log 10

aws
---
You need to have the pypyr aws plug-in installed to run the aws samples.

.. code-block:: bash

  $ pip install pypyraws

For authentication, get full details
`here <https://github.com/pypyr/pypyr-aws/tree/dev#aws-authentication>`__

You're probably running this on a dev box. Seriously, don't run this anywhere
close to production, or anything you actually care about.

Since you're on a dev box, the easiest way to configure aws authentication is
by just using the ``aws configure`` cli command. pypyr will automatically use
these authentication credentials in lieu of any other authentication config.

.. code-block:: bash

  $ aws configure
  AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
  AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
  Default region name [None]: us-west-2
  Default output format [None]: ENTER


Obligatory tiresome note:

WARNING: Using aws costs money. These examples are for quick and dirty demo
purposes and do not neccesarily delete resources they create. If you don't want
surprise bills, you need to delete these yourself.

slack
------
You need to have the pypyr slack plug-in installed to run the slack samples.

.. code-block:: bash

  $ pip install pypyrslack


Check ./pipelines/slack.yaml for details.

You will need a slack API token. I generally create a bot:
`create a bot <https://my.slack.com/services/new/bot>`__. You don't care
particularly about responding to events, just the bot api key so you can send
as the bot user. Maybe set a nice profile picture and bot name so your
notifications look pretty.

Remember to invite and add the bot you create to the slack channel(s) to which
you want to post. You invite the bot to the channel like you would a normal
user.
