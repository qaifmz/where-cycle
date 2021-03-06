import os
import sqlalchemy as sql


jdbc_props = {
    'driver': 'org.postgresql.Driver',
    'user': os.environ['PSQL_USER'],
    'password': os.environ['PSQL_PASSWORD']
}

jdbc_url = 'jdbc:postgresql://' + \
    os.environ['PSQL_HOST'] + ':' + os.environ['PSQL_PORT'] + \
    '/' + os.environ['PSQL_DATABASE']

py_engine = sql.create_engine(
    'postgresql://' +
    os.environ['PSQL_USER'] + ':' + os.environ['PSQL_PASSWORD'] +
    '@' + os.environ['PSQL_HOST'] + ':' + os.environ['PSQL_PORT'] +
    '/' + os.environ['PSQL_DATABASE']
)
