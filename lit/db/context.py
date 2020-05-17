import sqlite3


class Database(object):
    def __init__(self, file_path):
        self.conn = sqlite3.connect(file_path)

    def run_query(self, mode, txt):
        c = self.conn.cursor()
        if mode == 'ddl':
            c.execute(txt)
            self.conn.commit()
        elif mode == 'dml':
            c.execute(txt)
            self.conn.commit()
        elif mode == 'dql':
            c.execute(txt)


class Query(object):

    def __init__(self, db):
        self.db = db
        self.dql = ''

    def select(self, *args, **kwargs):
        if args:
            columns = ','.join(args)
            self.dql = f"SELECT {columns}"
        else:
            self.dql = 'SELECT *'
        return self

    def from(self, table_name):
        self.dql += f'FROM {table_name}'
        return self

    def run(self):
        self.db.run_query('dql', self.dql)
