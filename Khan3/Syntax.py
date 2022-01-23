import graphviz
import os
import re


class Node: 

    def __init__(self, value): 
        self.value = value
        self.child = []


def newNode(value):  
    tmp = Node(value)
    return tmp


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
epsilonCounter = -100
with open("Khan2/linesNumber.txt") as f:
    content = f.readlines()


for line in content:
    splittedLine = line.split(":: ")
    pairs.append((splittedLine[0], splittedLine[1], splittedLine[2][:-1]))

buffer = []
flagger = False
for index in range(len(pairs)):
    if pairs[index][0] == "identifier" or pairs[index][0] == "number":
        buffer.append((pairs[index][0], pairs[index][1], pairs[index][2]))
    elif pairs[index][0] == "operation" or pairs[index][0] == "comparison":
        buffer.append((pairs[index][1], pairs[index][1], pairs[index][2]))
    elif pairs[index][0] == "keyword" and pairs[index][1] in ["int", "float", "char"] and flagger:
        buffer.append((pairs[index][1], pairs[index+1][1], pairs[index][2]))
    else:
        flagger = True
        buffer.append((pairs[index][1], None, None))

buffer.append(("$", None))
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
inOrderTraversal = []
while(stack[-1][0] != '$'):
    top = stack[-1]
    top = top[0]
    if(top == buffer[bufferIterator][0]):
        bufferIterator += 1
        stack.pop()
        flag1 = True
        continue

    else:
        try:
            if(ll1[buffer[bufferIterator][0]][top] == "epsilon"):
                x = stack.pop()
                dot.node(str(epsilonCounter), 'Epsilon')
                dot.edge(str(x[1]), str(epsilonCounter))
                epsilonCounter += 1
                continue
        except KeyError as e:
            raise Exception('Syntax Error : {}'.format(e)) from None
        flag2 = True
        non_space = ll1[buffer[bufferIterator][0]][top].split()
        non_space.reverse()
        parent = stack.pop()
        if parent != "mainStatement":
            dot.node(str(parent[1]), parent[0])
            root = newNode(parent[0]) 
            if parent[0] == "mainStatement":
                finalTree = root
        for word in non_space:
            dot.node(str(counter), word)
            root.child.append(newNode(word)) 
            if((word == "identifier" or word == "operation" or word == "number" or word == "calculation" or word == "comparison")):
                inOrderTraversal.append(
                    (word, buffer[bufferIterator][1], buffer[bufferIterator][2]))
            dot.edge(str(parent[1]), str(counter))
            stack.append((word, counter))
            counter += 1
        stackProccess.append(stack.copy())
    if(not flag1 and not flag2):
        raise Exception('Syntax Error : {}'.format(e)) from None


def returnSyntaxTree():
    return finalTree

stackProccess.append(stack.copy())
content = ""
for item in stackProccess:
    arr = []
    for tupleItems in item:
        arr.append(tupleItems[0])
    content += " ".join(arr)+"\n"
with open("out/ParseTree/StackProccess.txt", "w") as f:
    f.write(content)
# dot.render('out/ParseTree/ParseTree.gv', view=True)
with open("Khan3/inOrderTraversal.txt", "w") as f:
    f.write("%s" % inOrderTraversal)
