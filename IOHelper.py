import configparser


def parseConfig(filename):
    '''Takes path to config file.
    Returns phonemes, allophones, declension rules, dictionary
    of word generation categories and word generation settings.
    '''
    parser = configparser.ConfigParser()
    parser.read(filename)

    rawphonemes = convertList(parser["TRANSCRIPTION"]["Phonemes"])
    phonemes = convertListToDic(rawphonemes)
    rawallophones = convertList(parser["TRANSCRIPTION"]["Allophones"])
    allophones = convertListToDic(rawallophones)

    declensions = {}
    for rule in parser["DECLENSION"]:
        declensions[rule] = parser["DECLENSION"][rule]

    wordgencategories = {}
    for cat in parser["WORDGEN-CATEGORIES"]:
        wordgencategories[cat] = convertList(parser["WORDGEN-CATEGORIES"][cat])

    wordsettings = {}
    wordsettings["maxS"] = int(parser["WORDGEN-SETTINGS"]["MaxSyllable"])
    wordsettings["minS"] = int(parser["WORDGEN-SETTINGS"]["MinSyllable"])
    wordsettings["rule"] = parseSylRule(parser["WORDGEN-SETTINGS"]["Rule"])

    return (phonemes, allophones, declensions, wordgencategories, wordsettings)


def parseSylRule(string):
    cats = string.split("|")
    rule = []
    for item in cats:
        if item[0] is not "(":
            rule.append(item)
        else:
            rule.append([item[1:-1], None])
    return rule


def convertList(string):
    '''Takes a list in string form such as "1, 2, 3" and returns
    a proper List.
    '''
    return string.replace(" ", "").split(",")


def convertListToDic(l):
    '''Takes a list of strings such as "'1:2', 'a:b'" and returns
    a dictionary.
    '''
    d = {}
    for item in l:
        isplit = item.split(":")
        d[isplit[0]] = isplit[1]
    return d


def parseDic(filename):
    '''Takes path to text file structured like so:
            example:8
            anotherexample:āçj
       And returns a dictionary with the first item of each line as the key and
       the second as the value.
    '''
    d = {}
    with open(filename, mode="r") as f:
        for line in f:
            l = line.strip()
            if l is not None:
                lsplit = l.split(":")
                d[lsplit[0]] = lsplit[1]
    return d


def parseList(filename):
    '''Takes path the text file structured like so:
            a
            b
            another value
       And returns a dictionary including each item.
    '''
    l = []
    with open(filename, mode="r") as f:
        for line in f:
            l.append(line.strip())
    return l


def createMenu(prompt, options):
    '''Takes a list of options and a prompt. Creates an input menu. Returns
    the item selected by the user.
    '''
    print(prompt + ":")
    for index, item in enumerate(options):
        bullet = "(" + str(index + 1) + ") "
        print(bullet + item)

    response = int(input("Enter selection: "))
    while response not in range(1, len(options) + 1):
        print("Selection not in range")
        response = int(input("Enter selection: "))

    return options[response - 1]


def chooseOption(prompt, options):
    olist = " ("
    for o in options[:-1]:
        olist = olist + o + "/"
    olist = olist + options[-1] + "): "

    response = input(prompt + olist)

    while response not in options:
        print("Response not in options")
        response = input(prompt + olist)

    return response


def yesNo(prompt):
    response = input(prompt + "? (y/n): ")
    while response not in ["y", "n"]:
        response = input(prompt + "? (y/n): ")

    if response == "y":
        return True
    else:
        return False
