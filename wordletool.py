import argparse
from operator import contains

parser = argparse.ArgumentParser(
    epilog="Aditional info: Known bug where -n letters will be excluded even if they appear in -w somewhere \n"
    +"Example usage: python3 wordle.py -n t -c s...e ..ra. -w la... ")
parser.add_argument("-n", help="Letters in this string do not appear in word")
parser.add_argument("-y", help="Letters in this string must appear anywhere in word")
parser.add_argument("-c", help="Letter appears somewhere but not in a particular spot eg: ..e.. multiple arguments accepted", nargs="+")
parser.add_argument("-w", "--word", help="The word has letters in exact positions: 'c.im.' periods are wildcards. ")
parser.add_argument("--cheat", action="store_true", help="Only gives you words that are final solution words")
parser.add_argument("-v","--verbose", action="store_true",help="display words and scores")

def wordsAreCompatible(input:str,compareString:str):
    '''Finds input in comppare string. Returns false if no match'''    
    outputList = list()
    for idx, char in enumerate(list(input)):
        if char == ".":
            continue
        if char == compareString[idx]:
            outputList.append(char)
        else:
            return False
    return True

def containsAllChars(chars:str,word:str):
    for letter in list(chars):
        if word.find(letter) == -1: # -1 if not in the word
            return False
    return True
    
def containsAnyChars(chars:str,word:str):
    '''returns true if any character is in that word'''
    for letter in list(chars):
        if word.find(letter) != -1:
            return True
    return False

def hasLettersElsewhere(listOLetters,word):
    for item in listOLetters:
        for idx, char in enumerate(item):
            if char == ".":
                continue
            else:
                if word[idx] == char:
                    return False
    chars = set()
    for item in listOLetters:
        chars.update(list(item))
    chars.remove(".") # remove the period if it's there
    return containsAllChars("".join(chars),word) # containsAllChars wants a string

def occurancesAtIdx(listOWords):
    listOccurances = list()
    for idx in range(5):
        dictOccurances = dict()
        wordles = list(listOWords)
        wordles = [wordle[idx] for wordle in wordles]
        bigstring = "".join(wordles)
        for letter in "abcdefghijklmnopqrstuvwxyz":
            dictOccurances[letter] = bigstring.count(letter)
            dictOccurances = dict(sorted(dictOccurances.items(), key=lambda item: item[1]))
        listOccurances.append(dictOccurances)
    return listOccurances

def occurancesAnywhere(listOWords):
    wordles = list(listOWords)
    bigstring = "".join(wordles)
    dictOccurances = dict()
    for letter in "abcdefghijklmnopqrstuvwxyz":
        dictOccurances[letter] = bigstring.count(letter)
    return dict(sorted(dictOccurances.items(), key=lambda item: item[1]))

def wordScore(word,scores):
    acc = 0
    for letter in set(word):
        acc += scores[letter]
    return acc

def wordScorePositional(word,scores):
    acc = 0
    for idx,letter in enumerate(list(word)):
        acc += scores[idx][letter]
    return acc
        
if __name__ == "__main__":
    args = parser.parse_args()
    if args.cheat is True:
        output = [item.strip() for item in open("cheater.txt")]
    else:
        output = [item.strip() for item in open("csw19-5-lower.txt")]

    if args.word is not None:
        newOutput = list()
        for wordle in output:
            if(wordsAreCompatible(args.word,wordle)):
                newOutput.append(wordle)
        output = newOutput

    if args.n is not None:
        newOutput = list()
        for wordle in output:
                if containsAnyChars(args.n,wordle) is False:
                    newOutput.append(wordle) # neg letters aren't in our word
        output = newOutput

    if args.c is not None:
        newOutput = list()
        for wordle in output:
            if hasLettersElsewhere(args.c,wordle):
                newOutput.append(wordle)
        output = newOutput
    
    if args.y is not None:
        newOutput = list()
        for wordle in output:
            if containsAllChars(args.y,wordle) is True:
                newOutput.append(wordle)
        output = newOutput

    scoredOutput = dict()
    scoredOutputPositional = dict()
    combined = dict()
    anywhereCriteria = occurancesAnywhere(output)
    positionalCriteria = occurancesAtIdx(output)
    for word in output:
        scoredOutput[word] = wordScore(word,anywhereCriteria)
    for word in output:
        scoredOutputPositional[word] = wordScorePositional(word,positionalCriteria)
    for word in output:
        combined[word] = wordScore(word,anywhereCriteria) + wordScorePositional(word,positionalCriteria)
        pass

    scoredOutput = dict(sorted(scoredOutput.items(), key=lambda item: item[1]))
    scoredOutputPositional = dict(sorted(scoredOutputPositional.items(), key=lambda item: item[1]))
    combined = dict(sorted(combined.items(), key=lambda item: item[1]))
    if(args.verbose):
        print("By positional score:")
        print(scoredOutput)
        print("By any occurance:")
        print(scoredOutputPositional)
        print("overall score:")
        print(combined)
    print(f'Got {len(output)} words. Here\'s the top 3:')
    print(list(combined.items())[-3:])