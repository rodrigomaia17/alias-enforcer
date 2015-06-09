import sys

commands = []
allArgs = sys.argv


def isNewCommand(text):
    if "=" in text and not("--pretty") in text:
        return True
    return False


def getCommands():
    parcialCommand = ""
    for text in allArgs:
        if isNewCommand(text):
            commands.append(parcialCommand)
            parcialCommand = text
        else:
            parcialCommand += " " + text


def convertToReversedAlias(aliasArray):
    finalAliasArray = []
    for alias in aliasArray:
        firstPart = alias.split('=', 1)[0]
        secondPart = alias.split('=', 1)[1]
        finalPhrase = "".join(["alias {}=\"echo".format(secondPart),
                               " 'Please use the alias '{}'".format(firstPart),
                               " instead of '{}''\"".format(secondPart)])
        finalAliasArray.append(finalPhrase)

    return finalAliasArray
