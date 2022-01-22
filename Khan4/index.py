from ast import literal_eval
from semanticTable import makeSemanticTable
import re

makeSemanticTable()

inOrderTraversal = []

with open("Khan4/semanticTable.txt") as f:
    identifierTable = f.readlines()

with open("Khan3/inOrderTraversal.txt") as f:
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
        if(re.findall("^[0-9]+$", sepratedSyntaxTree[index][1][1]) or re.findall("^[0-9]+[.][0-9]+$", sepratedSyntaxTree[index][1][1])):
            secondItem = "number "
        else:
            secondItem = "char "
        syntaxTable += "%s = %s :: %s\n" % (currentType, secondItem,sepratedSyntaxTree[index][0][2])
    else:
        for j in range(len(sepratedSyntaxTree[index])):
            if sepratedSyntaxTree[index][j][0] == "identifier":
                for i in range(len(identifierTable)):
                    if sepratedSyntaxTree[index][j][1] in identifierTable[i].split(" ")[1]:
                        syntaxTable += "%s " % identifierTable[i].split(" ")[0]
            else:
                if(re.findall("^[0-9]+$", sepratedSyntaxTree[index][j][1]) or re.findall("^[0-9]+[.][0-9]+$", sepratedSyntaxTree[index][j][1])):
                    syntaxTable += "number "
                elif(re.findall("^[a-zA-Z_][a-zA-Z_0-9]*", sepratedSyntaxTree[index][j][1])):
                    syntaxTable += "char "
                else:
                    syntaxTable+="%s "%sepratedSyntaxTree[index][j][1]
        syntaxTable+=":: %s"%sepratedSyntaxTree[index][j][2]
        syntaxTable += "\n"

lines=syntaxTable.split("\n")
for index in range(len(lines)):
    if(("char" in lines[index] and "int" in lines[index]) or ("char" in lines[index] and "number" in lines[index])):
        print("semantic error that happened in line : %s " % lines[index].split(":: ")[1])


result=""
for index in range(len(sepratedSyntaxTree)):
    if(sepratedSyntaxTree[index][0][0]=="identifier" and sepratedSyntaxTree[index][1][0]=="number"):
        for line in identifierTable:
            if(line.split("\n")[0].split(" ")[1]==sepratedSyntaxTree[index][0][1]):
                result+="%s %s = %s\n"%(line.split("\n")[0].split(" ")[0],line.split("\n")[0].split(" ")[1],sepratedSyntaxTree[index][1][1])
    else:
        for j in range(len(sepratedSyntaxTree[index])):
            if(sepratedSyntaxTree[index][j][0]=="identifier"):
                for line in identifierTable:
                    if(line.split("\n")[0].split(" ")[1]==sepratedSyntaxTree[index][j][1]):
                        result+="%s "%line.split("\n")[0].split(" ")[1]
            else:
                result+="%s "% sepratedSyntaxTree[index][j][1]
        result+="\n"

with open("Khan4/semanticTree.txt","w") as f:
    f.write("".join(result))
