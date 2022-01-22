import re
import sys
sys.path.append('./')
from Khan5.registerTable import makeRegisterTable

makeRegisterTable()

with open("Khan4\semanticTree.txt") as f:
    content = f.readlines()

with open("Khan5\\registerTable.txt") as f:
    lines = f.readlines()

result = lines
codeGenerationOutput = []
for item in content:
    if("+" in item or "-" in item or "/" in item or "*" in item):
        items = item[:-1].split("=")[1].split(" ")
        items = [x for x in items if x]
        newArr = []
        for value in items:
            if(re.findall("^[a-zA-Z_][a-zA-Z_0-9]*", value)):
                for line in lines:
                    if(line[:-1].split(" ")[0] == value):
                        newArr.append(str(line[:-1].split(" ")[2]))
                        printedValue = "lw %s %s" % (str(line[:-1].split(" ")[1]), str(line[:-1].split(" ")[2]))
                        print(printedValue)
                        codeGenerationOutput.append(printedValue)
            else:
                newArr.append(value)
        res = "".join(newArr)
        for line in lines:
            if(line[:-1].split(" ")[0] == item[:-1].split("=")[0].split(" ")[0]):
                printedValue = "lw %s %s" % (line[:-1].split(" ")[1], line[:-1].split(" ")[2])
                print(printedValue)
                codeGenerationOutput.append(printedValue)
                printedValue = "add %s 0 %s" % (line[:-1].split(" ")[1], eval(res))
                print(printedValue)
                codeGenerationOutput.append(printedValue)
                result[lines.index(line)] = "%s %s %s\n" % (line[:-1].split(" ")[0], line[:-1].split(" ")[1], eval(res))
                with open("Khan5\\registerTable.txt", "w") as f:
                    f.write("".join(result))
    else:
        for line in lines:
            if(line[:-1].split(" ")[0] == item[:-1].split("=")[0].split(" ")[1]):
                printedValue = "sw %s %s" % (line[:-1].split(" ")[1],item[:-1].split("=")[1].split(" ")[1])
                print(printedValue)
                codeGenerationOutput.append(printedValue)
                result[lines.index(line)] = "%s %s %s\n" % (
                    line[:-1].split(" ")[0], line[:-1].split(" ")[1], item[:-1].split("=")[1].split(" ")[1])
                with open("Khan5\\registerTable.txt", "w") as f:
                    f.write("".join(result))

with open("out/codeGeneration.txt","w") as f:
    f.write("\n".join(codeGenerationOutput))