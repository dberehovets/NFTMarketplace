from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from services.configurator import configurator


class DB:

    def __init__(self):
        engine = create_engine(
            'postgresql+psycopg2://{user}:{password}@{host}/{name}'.format(
                user=configurator.DB_USER,
                password=configurator.DB_PASSWORD,
                host=configurator.DB_HOST,
                name=configurator.DB_NAME
            )
        )
        _Session = sessionmaker(bind=engine)
        self.session = _Session()
        self.Model = declarative_base()


db = DB()
