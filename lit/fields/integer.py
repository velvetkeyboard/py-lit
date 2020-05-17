from lit.fields.base import Field
from lit.fields.base import IntegerType

class IntField(Field):
    sql_type = IntegerType()
    py_type = int

