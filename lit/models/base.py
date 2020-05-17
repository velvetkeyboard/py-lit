from lit.fields.base import Field


class Model(object):

    table_name_prefix = None
    table_name = None
    table_name_suffix = None
    #objects = DefaultManager(self)

    def __init__(self):
        if not self.table_name:
            self.table_name = self.__class__.__name__.lower()

    def __setattr__(self, attr, val):
        if hasattr(self, attr) and isinstance(getattr(self, attr), Field):
            getattr(self, attr).set_value(val)
            getattr(self, attr).set_name(attr)
        else:
            super(Model, self).__setattr__(attr, val)
  
    def get_full_table_name(self):
        return '{}{}{}'.format(
                self.table_name_prefix or '',
                self.table_name,
                self.table_name_suffix or '',
                )

    def get_fields(self):
        for attr in dir(self):
            field_obj = getattr(self, attr)
            if isinstance(field_obj, Field):
                yield (attr, field_obj)

    def get_sql_ddl(self):
        ret = []
        for attr, field in self.get_fields():
            field.name = attr
            ret.append(
                    field.get_sql_ddl())
        ret = ','.join(ret)
        ret = f'CREATE TABLE {self.get_full_table_name()} ({ret});'
        return ret

    def get_sql_dml(self):
        ret = ''
        ret_f = []
        ret_v = []
        for attr, field in self.get_fields():
            if not field.pk:
                ret_f.append(attr)
                ret_v.append(field.from_python_to_sql())
        ret_f = ','.join(ret_f)
        ret_v = ','.join(ret_v)
        ret = f'INSERT INTO {self.table_name} ({ret_f}) VALUES ({ret_v})'
        return ret

    def save(self):
        txt = self.get_sql_dml()
        print('dml', txt)
        #CONTEXT.run_query('dml', txt)

    def create(self):
        txt = self.get_sql_ddl()
        print('ddl', txt)
        #CONTEXT.run_query('ddl', txt)
