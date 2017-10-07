"""
Just a general all around utility functions that might be used in the app
"""
from . import db


def util_list_tables(database_name):
    return [(str(t),str(t)) for t in db.get_tables_for_bind(database_name)]



