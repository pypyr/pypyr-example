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

slack
------
You need to have the pypyr slack plug-in installed.

.. code-block:: bash

  $ pip install pypyr-slack


Check ./pipelines/slack.yaml for details.

You will need a slack API token. I generally create a bot:
`create a bot <https://my.slack.com/services/new/bot>`__. You don't care
particularly about responding to events, just the bot api key so you can send
as the bot user. Maybe set a nice profile picture and bot name so your
notifications look pretty.

Remember to invite and add the bot you create to the slack channel(s) to which
you want to post. You invite the bot to the channel like you would a normal
user.
