ll1 = {"int": {"mainStatement": "int main ( ) { statement", "statement": "initialize-statement", "semicolon-temp": "statement", "brace-temp": "statement", "initialize-statement": "type identifier initialize-statement-temp", "type": "int", "for-init-statement": "type identifier = expression-statement", },
       ")": {"exp-st": None, "condition-temp": None},
       "{": {"statement": "compound-statement", "semicolon-temp": "statement", "brace-temp": "statement", "compound-statement": "{ statement"},
       ";": {"semicolon": "; semicolon-temp", "exp-st": None, "initialize-statement-temp": "semicolon", "condition-temp": None},
       "}": {"semicolon-temp": "brace", "brace": "} brace-temp", "brace-temp": "}"},
       "identifier": {"statement": "labeled-statement", "semicolon-temp": "statement", "brace-temp": "statement", "labeled-statement": "identifier labeled-statement-temp", "expression-statement": "identifier exp-st", "	condition": "expression-statement condition-temp", "for-init-statement": "identifier", "for-process": "identifier steps", "var": "identifier"},
       "++": {"labeled-statement-temp": "++ semicolon", "steps": "++"},
       "--": {"labeled-statement-temp": "-- semicolon", "steps": "--"},
       "=": {"labeled-statement-temp": "calculation expression-statement semicolon", "calculation": "=", "	initialize-statement-temp": "= expression-statement semicolon", "steps": "calculation var"},
       "+=": {"labeled-statement-temp": "calculation expression-statement semicolon", "calculation": "+=", "steps": "calculation var"},
       "-=": {"labeled-statement-temp": "calculation expression-statement semicolon", "calculation": "-=", "steps": "calculation var"},
       "*=": {"labeled-statement-temp": "calculation expression-statement semicolon", "calculation": "*=", "steps": "calculation var"},
       "/=": {"labeled-statement-temp": "calculation expression-statement semicolon", "calculation": "/=", "steps": "calculation var"},
       "%=": {"labeled-statement-temp": "calculation expression-statement semicolon", "calculation": "%=", "steps": "calculation var"},
       "+": {"operation": "+", "exp-st": "operation expression-statement"},
       "-": {"operation": "-", "exp-st": "operation expression-statement"},
       "*": {"operation": "*", "exp-st": "operation expression-statement"},
       "/": {"	operation": "/", "exp-st": "operation expression-statement"},
       "%": {"operation": "%", "exp-st": "operation expression-statement"},
       "number": {"expression-statement": "number exp-st", "condition": "expression-statement condition-temp", "var": "number"},
       "float": {"statement": "initialize-statement", "semicolon-temp": "statement", "brace-temp": "statement", "initialize-statement": "type identifier initialize-statement-temp", "type": "float", "for-init-statement": "type identifier = expression-statement"},
       "char": {"statement": "initialize-statement", "semicolon-temp": "statement", "brace-temp": "statement", "initialize-statement": "type identifier initialize-statement-temp", "type": "char", "for-init-statement": "type identifier = expression-statement"},
       "if": {"statement": "selection-statement", "semicolon-temp": "statement", "	brace-temp": "statement", "selection-statement": "if ( condition ) statement"},
       "==": {"exp-st": None, "condition-temp": "comparison expression-statement", "comparison": "=="},
       ">=": {"exp-st": None, "condition-temp": "comparison expression-statement", "comparison": ">="},
       "<=": {"exp-st": None, "condition-temp": "comparison expression-statement", "comparison": "<="},
       "!=": {"exp-st": None, "condition-temp": "comparison expression-statement", "comparison": "!="},
       ">": {"exp-st": None, "condition-temp": "comparison expression-statement", "comparison": ">"},
       "<": {"exp-st": None, "condition-temp": "comparison expression-statement", "comparison": "<"},
       "while": {"statement": "iteration-statement", "	semicolon-temp": "statement", "brace-temp": "statement", "iteration-statement": "while ( condition ) statement"},
       "do": {"statement": "iteration-statement", "semicolon-temp": "statement", "brace-temp": "statement", "iteration-statement": "do statement while ( condition ) semicolon"},
       "for": {"statement": "iteration-statement", "semicolon-temp": "statement", "brace-temp": "statement", "iteration-statement": "for ( for-init-statement ; condition ; for-process ) statement"},
       "break": {"statement": "jump-statement", "semicolon-temp": "statement", "brace-temp": "statement", "jump-statement": "break semicolon"},
       "continue": {"statement": "jump-statement", "semicolon-temp": "statement", "brace-temp": "statement", "jump-statement": "continue semicolon"},
       "return": {"statement": "jump-statement", "semicolon-temp": "statement", "brace-temp": "statement", "jump-statement": "return expression-statement semicolon"},
       "$": {"brace-temp": None}
       }


pairs = []
with open("out/answer.txt") as f:
    content = f.readlines()
for line in content:
    # print(content)
    splittedLine = line.split(":: ")
    pairs.append((splittedLine[0], splittedLine[1][:-1]))
buffer = []
for item in pairs:
    if item[0] == "identifier" or item[0] == "number":
        buffer.append(item[0])
    else:
        buffer.append(item[1])
buffer.append("$")
stack = ['$']
stack.append("mainStatement")
bufferIterator = 0
while(stack[-1] != '$'):
    top = stack[-1]
    if(top == buffer[bufferIterator]):
        bufferIterator += 1
        stack.pop()
        continue
    else:
        tmp = ll1[buffer[bufferIterator]][top].split()   #اصلاح شود
        tmp.reverse()
        stack.pop()
        for word in tmp:
            stack.append(word)
        print(stack)
    # elif(top==None):
    #     pass
    # elif(ll1[top] is None):

print(stack)
