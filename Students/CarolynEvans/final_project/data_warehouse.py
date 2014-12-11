import psycopg2
from psycopg2._psycopg import ProgrammingError
from config import config

class data_warehouse(object):
    '''
    This class is used to get data from the Rightside data warehouse.
    The complete data warehouse documentation can be found at
        https://wiki.rightside.net/display/tnt/BI
    '''

    def __init__(self):
        """
        This method sets the data warehouse connection string from the config.
        """
        cnf = config()
        dbname = cnf.get('dw_dbname')
        user = cnf.get('dw_user')
        password = cnf.get('dw_password')
        host = cnf.get('dw_host')
        port = cnf.get('dw_port')

        self.dw_connection_string = \
         "dbname='{}' user='{}' password='{}' host='{}' port='{}'".format(dbname,user,password,host,port)


    def __call__(self, query):
        """
        This method calls the data warehouse API.
        The complete data warehouse documentation can be found at
            https://wiki.rightside.net/display/tnt/BI
        :param query: A string containing a valid redshift data warehouse query.
        :return: This depends on the query.
                 If the query returns records, as in a 'select' query, the records are returned.
                 If the query does not return records, as in an 'update' query, a unicode string is returned.
        """
        with psycopg2.connect(self.dw_connection_string) as conn:
            with conn.cursor() as curs:
                curs.execute(query)

                try:
                    records = curs.fetchall()
                    return records
                except ProgrammingError as e:
                    # This error occurs when there are no records to return,
                    # for example, queries such as inserts, updates, and unloads.
                    message = unicode(e)
                    if message == u'no results to fetch':
                        return message
                    else:
                        raise message



