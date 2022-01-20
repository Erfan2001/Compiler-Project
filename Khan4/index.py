import graphviz
import os
os.environ["PATH"] += os.pathsep + 'C:\Program Files (x86)\Graphviz2.38\\bin'
ll1 = {"int": {"mainStatement": "int main ( ) { statement", "statement": "initialize-statement", "semicolon-temp": "statement", "brace-temp": "statement", "initialize-statement": "type identifier initialize-statement-temp", "type": "int", "for-init-statement": "type identifier = expression-statement", },
       ")": {"exp-st": "epsilon", "condition-temp": "epsilon"},
       "{": {"statement": "compound-statement", "semicolon-temp": "statement", "brace-temp": "statement", "compound-statement": "{ statement"},
       ";": {"semicolon": "; semicolon-temp", "exp-st": "epsilon", "initialize-statement-temp": "semicolon", "condition-temp": "epsilon"},
       "}": {"semicolon-temp": "brace", "brace": "} brace-temp", "brace-temp": "}"},
       "identifier": {"statement": "labeled-statement", "semicolon-temp": "statement", "brace-temp": "statement", "labeled-statement": "identifier labeled-statement-temp", "expression-statement": "identifier exp-st", "condition": "expression-statement condition-temp", "for-init-statement": "identifier", "for-process": "identifier steps", "var": "identifier"},
       "++": {"labeled-statement-temp": "++ semicolon", "steps": "++"},
       "--": {"labeled-statement-temp": "-- semicolon", "steps": "--"},
       "=": {"labeled-statement-temp": "calculation expression-statement semicolon", "calculation": "=", "initialize-statement-temp": "= expression-statement semicolon", "steps": "calculation var"},
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
       "==": {"exp-st": "epsilon", "condition-temp": "comparison expression-statement", "comparison": "=="},
       ">=": {"exp-st": "epsilon", "condition-temp": "comparison expression-statement", "comparison": ">="},
       "<=": {"exp-st": "epsilon", "condition-temp": "comparison expression-statement", "comparison": "<="},
       "!=": {"exp-st": "epsilon", "condition-temp": "comparison expression-statement", "comparison": "!="},
       ">": {"exp-st": "epsilon", "condition-temp": "comparison expression-statement", "comparison": ">"},
       "<": {"exp-st": "epsilon", "condition-temp": "comparison expression-statement", "comparison": "<"},
       "while": {"statement": "iteration-statement", "	semicolon-temp": "statement", "brace-temp": "statement", "iteration-statement": "while ( condition ) statement"},
       "do": {"statement": "iteration-statement", "semicolon-temp": "statement", "brace-temp": "statement", "iteration-statement": "do statement while ( condition ) semicolon"},
       "for": {"statement": "iteration-statement", "semicolon-temp": "statement", "brace-temp": "statement", "iteration-statement": "for ( for-init-statement ; condition ; for-process ) statement"},
       "break": {"statement": "jump-statement", "semicolon-temp": "statement", "brace-temp": "statement", "jump-statement": "break semicolon"},
       "continue": {"statement": "jump-statement", "semicolon-temp": "statement", "brace-temp": "statement", "jump-statement": "continue semicolon"},
       "return": {"statement": "jump-statement", "semicolon-temp": "statement", "brace-temp": "statement", "jump-statement": "return expression-statement semicolon"},
       "$": {"brace-temp": "epsilon"}
       }


pairs = []
dot = graphviz.Digraph()
stackProccess = []
counter = 0
epsilonCounter=-100
with open("./out/answer.txt") as f:
    content = f.readlines()


for line in content:
    splittedLine = line.split(":: ")
    pairs.append((splittedLine[0], splittedLine[1][:-1]))

buffer = []

for item in pairs:
    if item[0] == "identifier" or item[0] == "number":
        buffer.append(item[0])

    else:
        buffer.append(item[1])

buffer.append("$")
stack = [('$', counter)]
counter += 1
stack.append(("mainStatement", counter))
counter += 1
bufferIterator = 0
flag1 = False
flag2 = False
dot.node('Tree', 'Tree')
dot.node(str(1), 'mainStatement')
dot.edge('Tree', str(1))
test=[]
while(stack[-1][0] != '$'):
    top = stack[-1]
    top=top[0]
    if(top == buffer[bufferIterator]):
        bufferIterator += 1
        stack.pop()
        flag1 = True
        continue

    else:
        try:
            if(ll1[buffer[bufferIterator]][top] == "epsilon"):
                x = stack.pop()
                dot.node(str(epsilonCounter), 'Epsilon')
                dot.edge(str(x[1]), str(epsilonCounter))
                epsilonCounter+=1
                continue
        except KeyError as e:
            raise Exception('Syntax Error : {}'.format(e)) from None
        flag2 = True
        non_space = ll1[buffer[bufferIterator]][top].split()
        non_space.reverse()
        parent = stack.pop()
        if parent!="mainStatement":
            dot.node(str(parent[1]), parent[0]) 
        for word in non_space:
            dot.node(str(counter), word)
            if(word=="identifier"or word=="=" or word=="+"or word=="number"):
                test.append(word)
            dot.edge(str(parent[1]), str(counter))
            stack.append((word,counter))
            counter+=1
        stackProccess.append(stack.copy())
    if(not flag1 and not flag2):
        raise Exception('Syntax Error : {}'.format(e)) from None
stackProccess.append(stack.copy())
content=""
for item in stackProccess:
    arr=[]
    for tupleItems in item:
        arr.append(tupleItems[0])
    content+=" ".join(arr)+"\n"
with open("out/ParseTree/StackProccess.txt","w") as f:
    f.write(content)
# dot.render('out/ParseTree/ParseTree.gv', view=True)
print(test)