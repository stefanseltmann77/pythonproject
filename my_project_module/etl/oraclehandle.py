import logging
from configparser import ConfigParser

import cx_Oracle


class OracleHandle:
    """Basic database handle for Oracle

    In order to work correctly you have to provide a config parser with the
    database name as the section and the connection paramters (without passwords) as the subconfigs of this section.
    """
    logger: logging.Logger
    configs: ConfigParser
    _conn: cx_Oracle.Connection

    def __init__(self, configs: ConfigParser):
        self.logger = logging.getLogger(__name__)
        self.configs = configs

    def get_dsn(self, db_name: str):
        configs = dict(self.configs[db_name].items())
        return cx_Oracle.makedsn(**configs)

    def get_cursor(self, db_name: str, user: str, password: str) -> cx_Oracle.Cursor:
        self._conn = cx_Oracle.connect(dsn=self.get_dsn(db_name=db_name),
                                       user=user,
                                       password=password)
        cursor = self._conn.cursor()
        self.logger.info(f"Established cursor on Oracle database {db_name} for {user}.")
        return cursor
