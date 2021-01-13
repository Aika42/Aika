# Exercise 12.7.1
def springcount(s: str):
    def count(s: str) -> dict:
        d = {}
        for ch in s:
            if ch != ' ':
                if ch in d:
                    d[ch] = d[ch] + 1
                else:
                    d[ch] = 1
        return d

    d = count(s)
    l = sorted([(k.lower(),v) for k,v in d.items()])

    for k, v in l:
        print(k, v)

# springcount('ThiS is String with Upper and lower case Letters')

# Exercise 12.7.4 Longest word in a file
def analysis():
    with open("/pythonProject1/alice.txt", "r") as f:

        l = []

        for line in f.readlines():
            for word in line.split():
                l.append(word)

        max = 0
        for ch in l:
            if len(ch) > max:
                max = len(ch)
        print(max)
        return max
# analysis()

# Exercise 12.7.5
def translator(sent: str) -> str:

    d = {'sir': 'matey', 'hotel': 'fleabag inn', 'student': 'swabbie', 'boy': 'matey', 'madam': 'proud beauty',
         'professor': 'foul blaggart', 'restaurant': 'galley', 'your': 'yer', 'excuse': 'arr', 'students': 'swabbies',
         'are': 'be', 'lawyer': 'foul blaggart', 'the': "th’", 'restroom': 'head', 'my': 'me', 'hello': 'avast', 'is': 'be',
         'man': 'matey'}

    words = sent.split()
    pirate_words = []
    for word in words:
        toappend = d.get(word, word)
        pirate_words.append(toappend)
    print(' '.join(pirate_words))

# translator('hello there students')

def translator1(sentence):

    pirate = {}
    pirate['sir'] = 'matey'
    pirate['hotel'] = 'fleabag inn'
    pirate['student'] = 'swabbie'
    pirate['boy'] = 'matey'
    pirate['restaurant'] = 'galley'
    pirate['hello'] = 'avast'
    pirate['students'] = 'swabbies'

    psentence = []
    words = sentence.split()
    for aword in words:
        if aword in pirate:
            psentence.append(pirate[aword])
        else:
            psentence.append(aword)

    return " ".join(psentence)

# translator1('hello there students')






