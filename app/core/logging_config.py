import logging

from app.config.settings import settings


def setup_logging():

    logging.basicConfig(
        level=settings.LOG_LEVEL,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )