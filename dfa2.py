import re
# inputFile = input("Enter Input Path\n")
# outputFile = input("Enter Output Path\n")
with open("In/test.c") as f:
    lines = f.readlines()

output: list = []
operationRegex = "[\+|\-|\*|\/|\%]+[\=]|[\+]+[\+]|[\-]+[\-]|[\+|\-|\*|\/|\%]|[\=]"
comparisonRegex = "[\<|\>|\=|\!]+[\=]|[\<]|[\>]"
punctuationRegex = "\(|\)|\;|\,|\[|\]|\{|\}"
keyword = ["if", "else", "main", "while", "int",
           "float", "for", "string", "do", "#include"]


def finder(arr: list):
    return [x for x in arr if x]


def dfa(str1: str):
    begin = 0
    if(str1.startswith("#include")):
        output.append(("library", str1.split(" ")[1][1:-1]))
        return
    if(str1.startswith("#define")):
        output.append(("definition", " ".join(str1.split(" ")[1:])))
        return
    # str1 = str1.replace(" ", "")
    flag = False
    for i in range(len(str1)):
        if(finder(re.findall("^[a-zA-Z_0-9]*", str1[i]))):
            continue
        else:
            token = str1[begin:i]
            if(token in keyword):
                output.append(("keyword", token))
            elif(finder(re.findall("^[0-9]*", token))):
                output.append(("number", token))
            elif(finder(re.findall("^[a-zA-Z_0-9]*", token))):
                output.append(("identifier", token))
            if(finder(re.findall(punctuationRegex, str1[i]))):
                output.append(("punctuation", str1[i]))
            if(i <= len(str1)-2 and finder(re.findall(comparisonRegex, str1[i]+str1[i+1]))):
                if(not(flag) and len(re.findall(comparisonRegex, str1[i]+str1[i+1])[0]) == 2):
                    output.append(("comparison", str1[i]+str1[i+1]))
                    flag = True
                elif(not(flag) and len(re.findall(comparisonRegex, str1[i]+str1[i+1])[0]) == 1):
                    output.append(("operation", str1[i]))
                else:
                    flag = False
            if(i <= len(str1)-2 and finder(re.findall(operationRegex, str1[i]+str1[i+1]))):
                if(not(flag) and len(re.findall(operationRegex, str1[i]+str1[i+1])[0]) == 2):
                    output.append(("operation", str1[i]+str1[i+1]))
                    flag = True
                elif(not(flag) and len(re.findall(operationRegex, str1[i]+str1[i+1])[0]) == 1):
                    output.append(("operation", str1[i]))
                else:
                    flag = False
            begin = i+1


isComment = False

for i in lines:
    i = i.strip()
    # Delete Comments
    if i.endswith("*/"):
        isComment = False
    if isComment:
        isComment = False
        continue
    if not i.startswith("//") and not i.startswith("/*"):
        dfa(i.strip())
    elif i.startswith("/*"):
        isComment = True
with open("out/answer.txt", "w") as f:
    for i in output:
        f.write(i[0])
        f.write(":: ")
        f.write(i[1])
        f.write("\n")
