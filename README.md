# wordle tool
A python shell tool to help solve wordle-like puzzles

it takes the solution set and the CSW-19 dictionary of 5 letter words and removes them from either set based on user inputs
"-n asdf" will remove words with a,s,d and f. 
"-c a.... .b... ..d.." will remove words that don't have a,b, or d in them or if it has them in those locations. 
"-w ..abc" will remove words that don't have a, b, or c in those exact positions.
—cheat lets you switch between CSW-19 and wordles solution dictionaries
—verbose lets you see the scores of each word

 "any occurance"is scoring where each letter carries a score equal to the number of occurrences in the worlde dictionary. 
"positional" is scoring where each letter carries a score equal to the number of words that have that letter in that position of the word (So there's 5 dicts containing scores)
and then combined combines the two.
