import os
import sys
from pathlib import Path

import pandas

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from sqlalchemy import select

from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from dotenv import load_dotenv


load_dotenv(Path(__file__).resolve().parent / '.env')

POSTGRES_USER = os.getenv('POSTGRES_USER', default='')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', default='')
POSTGRES_HOST = os.getenv('POSTGRES_HOST', default='')
POSTGRES_PORT = os.getenv('POSTGRES_PORT', default='')
POSTGRES_DATABASE_NAME = os.getenv('POSTGRES_DATABASE_NAME', default='')


def get_database_url():
    return (
        f'postgresql://'
        f'{POSTGRES_USER}:{POSTGRES_PASSWORD}'
        f'@{POSTGRES_HOST}:{POSTGRES_PORT}/'
        f'{POSTGRES_DATABASE_NAME}'
    )


# sqlalchemy declaring endpoint_names table
Base = declarative_base()


class EndpointName(Base):
    __tablename__ = 'endpoint_names'

    endpoint_id = Column(Integer, primary_key=True)
    endpoint_name = Column(String(250))


def get_row_from_excel(file_name: str):
    excel_data = pandas.read_excel(file_name)
    for row in excel_data.iterrows():
        # row[x] - index of row
        endpoint_id = row[1][0]
        endpoint_name = row[1][1]

        # check endpoint_name is not NaN or empty string, if so replace to None
        yield (
            endpoint_id,
            None if (
                isinstance(endpoint_name, float) and pandas.isna(endpoint_name)
            )
            else endpoint_name
        )


if __name__ == '__main__':
    file_name = sys.argv[1]

    db_engine = create_engine(
        get_database_url(),
        echo=True,
        future=True
    )

    with Session(db_engine) as session:
        for row in get_row_from_excel(file_name):
            endpoint = EndpointName(
                endpoint_id=row[0],
                endpoint_name=row[1]
            )
            session.add(endpoint)

        session.commit()

        query = select(EndpointName)
        for operator in session.scalars(query):
            print(operator.endpoint_id, operator.endpoint_name)
