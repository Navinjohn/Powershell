import pytest   #importing the pytest library
from Module import f   #importing the Module f from the Module file

#This function will test the string values
def string():
    assert f("hello") == {'h': 0, 'e': 0, 'l': 1, 'o': 0}

#This function will test the empty string
def empty_string():
    assert f("") == {}

#This function will test the List values
def list():
    assert f(["hello","hello","bye"]) == {'hello': 1, 'bye': 0}

#This function will test the combined or mixed values
def all():
    assert f(["hello",1,1,"bye"]) == {'hello': 0, '1': 1, 'bye': 0}