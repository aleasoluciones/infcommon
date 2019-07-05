# -*- coding: utf-8 -*-

import os
import psycopg2.extras

from infcommon.factory import Factory
from infcommon.postgres.postgres import PostgresClient

def postgres_client_from_connection_parameters(user, password, host, port, db_name, use_dict_cursor=None):
    connection_uri = 'postgresql://{user}:{password}@{host}:{port}/{db_name}'.format(user=user, password=password, host=host, port=port, db_name=db_name)
    return _postgres_client(connection_uri, use_dict_cursor)

# TODO: remove this factory method. db_uri should be passed by application, not
# at factory
def postgres_client_from_connection_os_variable(db_uri_os_valiable_name='LOCAL_PG_DB_URI', use_dict_cursor=None):
    print("This method `postgres_client_from_connection_os_variable` should not be used. Please consider to use another factory")
    connection_uri = os.getenv(db_uri_os_valiable_name)
    return _postgres_client(connection_uri, use_dict_cursor)


def _postgres_client(connection_uri, use_dict_cursor):
    cursor_factory = _cursor_factory(use_dict_cursor)
    instance_id = "postgres_client_{}_{}".format(connection_uri, use_dict_cursor)
    return Factory.instance(instance_id,
                            lambda: PostgresClient(connection_uri, cursor_factory=cursor_factory)
                           )

def _cursor_factory(use_dict_cursor=None):
    if use_dict_cursor:
        return psycopg2.extras.DictCursor
    return None
