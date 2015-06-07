import alias_enforcer
from nose.tools import assert_equal

def test_should_known_when_is_new_command():
    assert alias_enforcer.isNewCommand("ei=")

def test_should_convert_one_simple_alias():
    simpleAlias = ["e=echo"]
    expected = ["alias echo=\"echo 'Please use the alias 'e' instead of 'echo''\""]
    actual = alias_enforcer.convertToReversedAlias(simpleAlias)
    assert_equal(actual,expected)


