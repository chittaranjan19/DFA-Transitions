# DFA-Transitions
A Python script to mimic the working of a Deterministic Finite Automaton

The program when run prompts the user for a file name and input string.
The file contains the transition table for a DFA (in the format specified below). Then it looks at the input string given and prints out whether the string is accepted or rejected.

The transition table is given in this format in the file:

First row contains the alphabets separated by tabs. Assume that the alphabet whatever it is will be only one character. For example, it won't have "alphabet" as an alphabet . The next row will indicate the transitions for q0 which can be assumed as the start state.

In each of the entries, i is used to indicate a state qi. After all the rows of the transition table are done, there is one blank line, following which the state numbers of the final states are mentioned(tab separated).

So, the transition table file for the DFA which accepts the set of all strings that DO NOT contain aab (the alphabet is: {a,b,c}) is as follows:

a	b	c
1	0	0
2	0	0
2	3	0
3	3	3

0	1	2
