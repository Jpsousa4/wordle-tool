# wordle tool
A python shell tool to help solve wordle-like puzzles

### Overview 
Wordle Tool uses the CSW-19 dictionary filtered to 5 letter words and remove words from the set based on user inputs. It then scores the remaining words according to the similarity to other words in the set. This is a weak algorithm that will prioritize words that have the highest chance of eliminating the most words from the existing possible options. 

### Arguments
**Not in set:** ```"-n asdf"``` will remove words with a,s,d and f. 

**Combination of letters:** ```"-c a.... .b... ..d.."``` will remove words that don't have a,b, or d in them or if it has them in those locations. (these letters appear yellow in wordle). These arguments are positional and can be combined. IE: ```a.... .b... ..d..``` will yield the same results as ```abd..```

**Word structure** "-w ..abc" will remove words that don't have a, b, or c in those exact positions. These are your green letters!

**—cheat** lets you switch between CSW-19 and wordles solution dictionaries. Worlde's solution set is about 2000 words, where the CSW-19 (the dictionary wordle uses to check if your input word is actually a word) is 12000 words.

**—verbose** lets you see the scores of each word

### Word scoring
**"any occurance"** is scoring where each letter carries a score equal to the number of occurrences in the worlde dictionary. "How many words do the letters in this word have similarity with?" (This currently double tracks words, but could be improved at the cost of O(n^2) operation)

**"positional"** is scoring where each letter carries a score equal to the number of words that have that letter in that position of the word (So there's 5 dicts containing scores, one per letter position). The score is the combination of the scores of each letter per position in that word
and then combined combines the two.

### Examples

``` 
python3 wordletool.py -n taes -w .ro.. -c ..r.. ...n.
Got 11 words. Here's the top 3:
[('crown', 83), ('frown', 83), ('grown', 83)]
```
```
python3 wordletool.py -n tareup -w s.... -c .o..y    
Got 4 words. Here's the top 3:
[('sybow', 26), ('sycon', 27), ('synod', 29)]
```
