import re
import os
# Input Path
# inputFile = input("Enter Input Path\n")

# Output Path
# outputFile = input("Enter Output Path\n")

# Get Value from regex


def finder(arr: list):
    return [x for x in arr if x]

# Remove Comments Function


def remove_Comments(fileContent):
    removeMultipleComments = re.sub(
        "/\*[^*]*\*+(?:[^/*][^*]*\*+)*/", "", fileContent)
    removeSingleComments = re.sub(
        "//.*", "", removeMultipleComments)
    result = removeSingleComments
    return result

# Remove Spaces Function


def removeSpaces(data: str):
    res = data.split("\n")
    res = [x for x in res if x]
    return "\n".join(res)

# Replace Includes


def replaceIncludes(data: str):
    res = data.split("\n")
    for index in range(len(res)):
        if(res[index].startswith("#include")):
            res[index] = res[index].replace(" ", "")
            fileName = res[index].split("#include")[1][1:-1]
            with open(fileName) as f:
                fileData = f.read()
            res[index] = fileData+"\n"
        else:
            res[index] += "\n"
    return "".join(res)

# Replace Defines


def replaceDefines(data: str):
    res = data.split("\n")
    definesDic: dict = {}
    for index in range(len(res)):
        if(res[index].startswith("#define")):
            key = res[index].split(" ")[1]
            value = " ".join(res[index].split(" ")[2:])
            definesDic[key] = value
    for index in range(len(res)):
        for key, value in definesDic.items():
            res[index] = res[index].replace(key, value)
        res[index] += "\n"
    res = [x for x in res if not x.startswith("#")]
    return "".join(res)


def errorHandling(data: str):
    # Default Value should be 1 for "int main()"
    loopsCount = 1
    parenthesesCount = 0
    # Loops Count
    for item in ["for", "while", "if", "else"]:
        loopsCount += data.count(item)
    # Parentheses Count
    for item in ["{", "}"]:
        parenthesesCount += data.count(item)
    res = data.split("\n")
    for index in range(len(res)):
        # Parentheses Checking in while and for loop
        if(res[index].startswith("for") or res[index].startswith("while")):
            if(not(finder(re.findall("\)", res[index]) and finder(re.findall("\(", res[index]))))):
                print("In Line %d Has Error!!!!" % index)
        # Semicolon Checking
        if finder(re.findall("^int|float|string|char", res[index])):
            if(res[index][-1] != ";" and not finder(re.findall("main", res[index]))):
                print("In Line %d Has Error!!!!" % index)
         # ParenthesesCount in forLoop Checking
        if finder(re.findall("^for", res[index])):
            if(res[index].count(";") != 2):
                print("In Line %d Has Error!!!!" % index)
        # ParenthesesCount Checking
        if(loopsCount*2 != parenthesesCount):
            print("ParenthesesCount Error!!!!")
        # Check File Exist
        if(res[index].startswith("#include")):
            fileName = res[index].split(" ")[1:]
            if(not os.path.isfile(fileName)):
                print("In Line %d Has Error!!!!" % index)


# Read FileData from Source File
with open("In/test.c") as f:
    fileData = f.read()

# Calling remove Comments
program = remove_Comments(fileData)
# Calling remove Includes
result = replaceIncludes(program)
# Calling remove Defines
result2 = replaceDefines(result)
# Calling remove Spaces
result3 = removeSpaces(result2)
# Calling Error Handling
result4 = errorHandling(result3)
# Write In New File
with open("In/new.txt", "w") as f:
    f.write(result3)

# Operation Regex
operationRegex = "[\+|\-|\*|\/|\%]+[\=]|[\+]+[\+]|[\-]+[\-]|[\+|\-|\*|\/|\%]|[\=]"
# Comparison Regex
comparisonRegex = "[\<|\>|\=|\!]+[\=]|[\<]|[\>]"
# Punctuation Regex
punctuationRegex = "\(|\)|\;|\,|\[|\]|\{|\}"
# Keywords
keyword = ["if", "else", "main", "while", "int",
           "float", "for", "string", "do", "#include"]

output: list = []


def dfa(str1: str, lineNumber: int):
    begin = 0
    # str1 = str1.replace(" ", "")
    flag = False
    for i in range(len(str1)):

        if(finder(re.findall("^[a-zA-Z_0-9]*", str1[i]))):
            continue
        else:
            token = str1[begin:i]
            if(token in keyword):
                output.append(("keyword", token))
            elif(finder(re.findall("^[0-9]+[a-zA-Z_0-9]+", token))):
                print("lexical error that happened in line : %d " % lineNumber)
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


# Read Lines from Source File
with open("In/new.txt") as f:
    lines = f.readlines()
lineNumber = 1
for i in lines:
    dfa(i, lineNumber)
    lineNumber += 1
# Write in Output File
with open("out/answer.txt", "w") as f:
    for i in output:
        f.write(i[0])
        f.write(":: ")
        f.write(i[1])
        f.write("\n")
