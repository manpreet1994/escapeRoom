# escapeRoom
python function for suggested answers of android game Escape Room

EscapeRoom solver
Escape Room is an android word game. The game is level based. In each level, user is given clue(s) and a set of words from which words can be formed with length of answer visible. This standalone code provides possible answer given all possible alphabets and length of answer.

Getting Started
Simply run this standalone code with two functions available wordsthatmatter and wordsthatmatterRepotition

1. wordsthatmatter
input  = string of possible alphabets (eg 'lkjyhgtfh'), length of answer (5)
output = list of words of length 5 using possible alphabets without any repetition


2. wordsthatmatterRepotition
input  = string of possible alphabets (eg 'lkjyhgtfh'), length of answer (5)
output = list of words of length 5 using possible alphabets with repetition among possible alphabets

Prerequisites
1. nltk wordnet

License
This project is licensed under the GNU - see the LICENSE.md file for details
