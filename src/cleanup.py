"""
Script to delete users who have not verified their email after 30 days.
"""
import datetime
import os
import sys

import structlog
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from logconfig import configure_logging
from models import Customer


def get_database_connection():
    return create_engine(os.getenv("DATABASE_URL"))


def run():
    assert sys.version_info >= (3, 6), "Script needs at least python 3.6"
    configure_logging()
    logger = structlog.get_logger()
    before_date = datetime.datetime.today() - datetime.timedelta(days=30)
    logger.info("Starting cleanup for unverified users older than: %s" % before_date)
    session = sessionmaker(bind=get_database_connection())()
    logger.info(str(session.query(Customer).all()[:5]))


if __name__ == "__main__":
    run()
