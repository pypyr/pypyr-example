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
  $ pypyr --name simple --log 20

  # run the pipelines/simple.yaml pipeline with the default DEBUG log level.
  # this will give you all the gory details.
  $ pypyr --name simple
