Word Ladder is a game, possibly invented by Lewis Carroll (who called it “Doublets”), where
you are given two six-letter words and have to find a path from the first word to the second. The
path consists of valid words that differ from their adjacent words by only one letter. A list of
valid words is provided and all word paths must come from that list. For example, on input
(beaker, listen), one possible path is beaker, beater, better, fetter, fitter, fitted, fisted, listed, listen
and the number of steps is 9.

Each word in this particular file is 6 letters long and there is
one word per line—if there are any empty lines, code should ignore such lines.
Program should output the length of the shortest path between the two words along with the
actual path of words, or state that no such path exists. It should exit gracefully if the input is not
in the expected format (e.g. words are the wrong length or not valid).
