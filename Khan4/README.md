### Khan4

In this phase, we have two parts that are "index.py" & "semanticTable.py".

1. **SemanticTable** : In this section we only have a function named "makeSemanticTable".We use "answer.txt" from Khan2 in order to allocate parts of our output(from keyword to semicolon) to the type(int,float,char) and write it inside the file named "semanticTable.txt".
2. **index** : First of all we call the makeSemanticTable function and read "semanticTable.txt" and "inOrderTraversal.txt" files.
In the first for loop we try to group the inputs from inOrderTraversal inside the "sepratedSyntaxTree".

  For example:
  
    Input:  [('identifier', 'b', '3'), ('number', '2', '3')]
    
    Output: [[('identifier', 'b', '3'), ('number', '2', '3')]]

In the second for loop we replace each identifier with its type & each int and float numbers to number & each character to char and at last we append a line number.

  For example:
  
    Input: [[('identifier', 'b', '3'), ('number', '2', '3')]]
    
    Output: int = number  :: 3

In third for loop with 2 conditions we chaeck the possibility of semantic errors:
1. In one line we have char & int at the same time.
2. In one line we have char & number at the same time.

In the last for loop which is a preparation for next khan that is "Code Generation" remakes each line of input code.

  For example:
  
    Input: int = number  :: 3
    
    Output: int b = 2

Fall 1400
