### Khan5

In this phase we have 2 parts:
1. **RegisterTable** : Reads "semanticTree.txt" from khan4 and saves identifier,register and value inside the "registerTable.txt".

  For example:
  
    Input: int b = 2
    
    Output: b 0 2
2. **Index** : We read from "semanticTree.txt" & "registerTable.txt".Inside the "semanticTree.txt" if we had ( +,-,/,* ) we calculate the right side of "=" and if we had identifier we search its value inside the registerTable and replace it.At last we put the calculation inside the left side register and save it inside its registerTable.
Nevertheless, we store the right side value inside the left side register in its refisterTable.

At last we saved the final result inside "codeGeneration.txt".

Fall 1400
