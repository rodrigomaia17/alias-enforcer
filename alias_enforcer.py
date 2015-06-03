import sys

commands = []
parcialCommand = ""
allArgs = sys.argv


def isNewCommand(text):
    if "=" in text and not("--pretty") in text:
        return True
    return False


def getCommands():
    for text in allArgs:
        if isNewCommand(text):
            commands.append(parcialCommand)
            parcialCommand = text
        else:
            parcialCommand += " " + text


def convertToReversedAlias(alias):
    firstPart = alias.split('=', 1)[0]
    secondPart = alias.split('=', 1)[1]
    finalPhrase = "alias {}=\"echo 'Please use the alias '{}' instead of '{}''\"".format(secondPart,firstPart,
                                                              secondPart)
    return finalPhrase
