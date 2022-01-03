### Khan2

In this Phase, we used "re" and "sys" libraries in order to use regex, and use the operating system to transfer between folders.
As for the first step, we call Khan1's parent function that is "preprocess()" to transform the C code into the txt format.
Then we define the following regexes:

1. **operationRegex** : Recognizes operations inside the input such as: +,=,-,/,%,...

2. **comparisonRegex** : Recognizes comparison statements for the common loops which includes: >,<,==,...

3. **punctuationRegex** : Recognizes other components such as: ;,( ,),{ ,} ,...

4. **keyword** : An array of C keywords including: for, if, while,...

We read data line by line from the "new.txt" file and remove the spaces between words and send it to the "dfa" function.

Dfa Function:We put the lines inside a buffer. Then, with the help of two iterators called "begin" and "i" we go through buffer and check the sample character by character. The iteration continues until we reach a element not related to previous elements. After that, by using pre-defined regexes we evaluate element which is from "begin" to "i" and specify its token kind inside the "output" list.

As an example-> We have following C code:
int ab = 2 ;

In this case, we put begin and i on the first character ("i") and start the iteration. i goes through "n" and "t", respectively. Finally it reaches " " which is not a word or number. As a result, we start from the begin and go through i and reach the word "int". Then we evaluate the "int" with regexes and find that "int" is a keyword and consequently put this result inside the output list. Finally, we begin=i+1 and continue the iteration until the end of the input code.

**Note that: We find the lexical errors during the iteration with the help of defined regexes.**

The last step in this Khan is writting output list inside a file called "answer.txt".

Fall 1400
