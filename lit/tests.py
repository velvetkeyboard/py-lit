from unittest import TestCase
from lit.fields.integer import IntField
from lit.fields.text import TextField
from lit.models.base import Model
from lit.db import *


class IntFieldTestCase(TestCase):
    def test_ddl(self):
        f = IntField(name='field_name')
        self.assertEqual(f.get_sql_ddl(), 'field_name INT')
        f = IntField(name='field_name', pk=True)
        self.assertEqual(f.get_sql_ddl(), 'field_name INT PRIMARY KEY')
        f = IntField(name='field_name', unique=True)
        self.assertEqual(f.get_sql_ddl(), 'field_name INT UNIQUE')
        f = IntField(name='field_name', not_null=True)
        self.assertEqual(f.get_sql_ddl(), 'field_name INT NOT NULL')
        f = IntField(name='field_name', pk=True, unique=True, not_null=True)
        self.assertEqual(f.get_sql_ddl(), 'field_name INT PRIMARY KEY UNIQUE NOT NULL')

    def test_convertion(self):
        f = IntField(name='field_name', value='1')
        self.assertEqual(f.from_sql_to_python(), 1)


class TextFieldTestCase(TestCase):
    def test_ddl(self):
        f = TextField(name='field_name')
        self.assertEqual(f.get_sql_ddl(), 'field_name TEXT')
        f = TextField(name='field_name', pk=True)
        self.assertEqual(f.get_sql_ddl(), 'field_name TEXT PRIMARY KEY')
        f = TextField(name='field_name', unique=True)
        self.assertEqual(f.get_sql_ddl(), 'field_name TEXT UNIQUE')
        f = TextField(name='field_name', not_null=True)
        self.assertEqual(f.get_sql_ddl(), 'field_name TEXT NOT NULL')
        f = TextField(name='field_name', pk=True, unique=True, not_null=True)
        self.assertEqual(f.get_sql_ddl(), 'field_name TEXT PRIMARY KEY UNIQUE NOT NULL')

    def test_convertion(self):
        f = TextField(name='field_name', value='txt')
        self.assertEqual(f.from_sql_to_python(), 'txt')


class ModelTestCase(TestCase):
    def test_ddl(self):
        class User(Model):
            name = TextField()
            age = IntField()
        u = User()
        u.name = 'john'
        u.age = 1
        self.assertEqual(
                u.get_sql_ddl(), 'CREATE TABLE user (age INT,name TEXT);')

    def test_dml(self):
        class User(Model):
            name = TextField()
            age = IntField()
        u = User()
        u.name = 'john'
        u.age = 1
        self.assertEqual(
                u.get_sql_dml(), "INSERT INTO user (age,name) VALUES (1,'john')")

    def test_field_instance_ref(self):
        class User(Model):
            first_name = TextField()
            last_name = TextField()
        u = User()
        u.first_name = 'John'
        u.last_name = 'Doe'
        self.assertEqual(
            u.get_sql_dml(), "INSERT INTO user (first_name,last_name) VALUES ('John','Doe')")

