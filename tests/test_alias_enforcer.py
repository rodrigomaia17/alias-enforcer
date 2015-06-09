import alias_enforcer
from nose.tools import assert_equal

aliasEcho="e=echo"
aliasEchoReversed="alias echo=\"echo 'Please use the alias 'e' instead of 'echo''\""
aliasVim="v=vim"
aliasVimReversed="alias vim=\"echo 'Please use the alias 'v' instead of 'vim''\""


def test_should_known_when_is_new_command():
    assert alias_enforcer.isNewCommand("ei=")


def test_should_convert_one_simple_alias():
    simpleAlias = [aliasEcho]
    expected = [aliasEchoReversed]
    actual = alias_enforcer.convertToReversedAlias(simpleAlias)
    assert_equal(actual, expected)

def test_should_convert_two_simple_alias():
    alias = [aliasEcho,aliasVim]
    expected = [aliasEchoReversed,aliasVimReversed]
    actual = alias_enforcer.convertToReversedAlias(alias)
    assert_equal(actual,expected)
