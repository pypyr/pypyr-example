"""This is a barebones example of a custom pipeline step.

This python module exists in the mypythonpackage. This pattern is useful if
your custom step will be calling code in other modules.

I normally prefer keeping the heavy lifting out of the run_step itself and
refactor it into its own modules instead, for all the usual reasons of
encapsulation, easier unit testing, et.
"""
import pypyr.log.logger


logger = pypyr.log.logger.get_logger(__name__)


def run_step(context):
    """Run code in here. This shows you how to code a custom pipeline step."""
    logger.debug("started")

    logger.info("you prob want to do something useful here. . .")

    logger.debug("done")
    return context
