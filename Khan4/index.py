from ast import literal_eval
from semanticTable import makeSemanticTable
import re

makeSemanticTable()

inOrderTraversal = []

with open("out/identifierTable.txt") as f:
    identifierTable = f.readlines()

with open("out/new.txt") as f:
    inOrderTraversal = literal_eval(f.read())

sepratedSyntaxTree = []
begin = 0

for index in range(len(inOrderTraversal)):
    if index < len(inOrderTraversal)-2 and inOrderTraversal[index][0] in ["identifier", "number"] and inOrderTraversal[index+1][0] in ["identifier"]:
        sepratedSyntaxTree.append(inOrderTraversal[begin:index+1])
        begin = index+1
sepratedSyntaxTree.append(inOrderTraversal[begin:])

syntaxTable = ""

for index in range(len(sepratedSyntaxTree)):
    currentType = ""
    if(len(sepratedSyntaxTree[index]) == 2 and sepratedSyntaxTree[index][0][0] == "identifier" and sepratedSyntaxTree[index][1][0] == "number"):
        for i in range(len(identifierTable)):
            if sepratedSyntaxTree[index][0][1] in identifierTable[i].split(" ")[1]:
                currentType = identifierTable[i].split(" ")[0]
        secondItem = ""
        if(re.findall("^[0-9]+$", sepratedSyntaxTree[index][1][1])):
            secondItem = "number "
        else:
            secondItem = "char "
        syntaxTable += "%s = %s\n" % (currentType, secondItem)
    else:
        for j in range(len(sepratedSyntaxTree[index])):
            if sepratedSyntaxTree[index][j][0] == "identifier":
                for i in range(len(identifierTable)):
                    if sepratedSyntaxTree[index][j][1] in identifierTable[i].split(" ")[1]:
                        syntaxTable += "%s " % identifierTable[i].split(" ")[0]
            else:
                if(re.findall("^[0-9]+$", sepratedSyntaxTree[index][j][1])):
                    syntaxTable += "number "
                elif(re.findall("^[a-zA-Z_][a-zA-Z_0-9]*", sepratedSyntaxTree[index][j][1])):
                    syntaxTable += "char "
                else:
                    syntaxTable+="%s "%sepratedSyntaxTree[index][j][1]
        syntaxTable += "\n"

lines=syntaxTable.split("\n")
for index in range(len(lines)):
    if(("char" in lines[index] and "int" in lines[index]) or ("char" in lines[index] and "number" in lines[index])):
        print("Semantic Error !!!")
