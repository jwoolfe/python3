#!/usr/bin/env python3

def test_me():
    assert True

def not_a_test():
    assert True

class TestClass:
    def test_me(self):
        assert True

    def test_me2(self):
        assert True

class MyTestClass():
    def test_it(self):
        assert True

    def test_it2(self):
        assert True
