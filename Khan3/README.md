### Khan3

In this phase, first of all we implement a class named "Node" in order to make a format for parse tree.

Next, we made a ll1 dictionary according to "LL1 Grammers.txt" which is actually ll1 table.

As for graphical output, we used graphviz library in order to make a graphical parse tree.
For each node we need a label and uniqueId and for implementation of uniqueId we needed a "counter".

We read a "linesNumber.txt" from Khan2 and append it into the "pairs".Separated into the key,value,lineNumber.

We initialized array named "buffer" for the inputs & put "$" inside it.Also we initialized stack and put "$" and "mainStatement" inside it to.
Then we move inside a while loop & continue the loop until there is only a "$" inside the stack.

Inside the while loop, we iterate the buffer and compare it with the top of the stack and do the push and pop operations.
MeanWhile with the help of graphviz, we also make our graphical tree according to the stack.

We also made an array named "inOrderTraversal" as like as pairs for the convinience of next khan.

StackProccess : Is used for as a backup for the changes that happend in the "stack".

At last we write the "StackProccess" & "inOrderTraversal" inside the files named "StackProccess.txt" & "inOrderTraversal.txt", respectively.

Fall 1400
