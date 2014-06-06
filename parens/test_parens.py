import pytest
import parens

def test_open_parens():
    myString = "(a+b)*((x/2)"
    assert parens.check_parens(myString) == 1
    myString = "(((((((()))(((())))"
    assert parens.check_parens(myString) == 1

def test_broken_parens():
    myString = "(a=b)*'this'+)/(9)"
    assert parens.check_parens(myString) == -1
    myString = ")(((())))"
    assert parens.check_parens(myString) == -1
    myString = "(()))(((()))))"
    assert parens.check_parens(myString) == -1

def test_balanced_parens():
    myString = "(a+b*(3y))"
    assert parens.check_parens(myString) == 0
    myString = "(((((((())))))))(((())))((((()))))"
    assert parens.check_parens(myString) == 0