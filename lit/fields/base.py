class Field(object):

    sql_type = None
    py_type = None

    def __init__(self, name=None, value=None, pk=None, unique=None, not_null=None):
        self.name = name
        self.pk = pk
        self.unique = unique
        self.not_null = not_null
        self.value = value

    def set_name(self, name):
        self.name = name

    def set_value(self, value):
        self.value = value

    def get_sql_ddl(self):
        ret = f'{self.name} {self.sql_type.name}'
        if self.pk:
            ret += ' PRIMARY KEY'
        if self.unique:
            ret += ' UNIQUE'
        if self.not_null:
            ret += ' NOT NULL'
        return ret

    def from_sql_to_python(self):
        return self.py_type(self.value)

    def from_python_to_sql(self):
        return self.sql_type.from_python_to_sql(self.value)


class SqlType(object):
    name = None
    def from_python_to_sql(self, value):
        raise NotImplemented

class IntegerType(SqlType):
    name = 'INT'
    def from_python_to_sql(self, value):
        return str(value)

class TextType(SqlType):
    name = 'TEXT'
    def from_python_to_sql(self, value):
        return f"'{value}'"

