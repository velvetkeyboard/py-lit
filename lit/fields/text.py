from lit.fields.base import Field
from lit.fields.base import TextType

class TextField(Field):
    sql_type = TextType()
    py_type = str

