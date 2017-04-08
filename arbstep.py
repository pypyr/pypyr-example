"""This shows an arbitrary .py script not inside a package.

To get your arbitrary python code to run as a pypyr step, use this blueprint.
The important thing is the run_step(context) signature.
"""
import pypyr.log.logger


logger = pypyr.log.logger.get_logger(__name__)


def run_step(context):
    """Run code in here. This shows you code a custom pipeline step."""
    logger.debug("started")

    logger.info("This is an arbitrary step that isn't in a package.")

    logger.debug("done")
    return context
