import logging

from app.core.logging_config import setup_logging
from app.core.settings import settings

logger = logging.getLogger(__name__)

def on_startup():

    setup_logging()

    logger.info("--------------------------------------")
    logger.info(settings.APP_NAME)
    logger.info("Application Started Successfully")
    logger.info("--------------------------------------")