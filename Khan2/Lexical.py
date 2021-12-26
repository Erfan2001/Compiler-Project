import re
import sys
sys.path.append( './' )
from Khan1.PreProcessing import PreProcess


# Input Path

# inputFile = input("Enter Input Path\n")

# Output Path

# outputFile = input("Enter Output Path\n")


# Get Value from regex

def finder(arr: list):
    return [x for x in arr if x]


PreProcess()


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
    flag = False

    for i in range(len(str1)):
        if(finder(re.findall("^[a-zA-Z_0-9\.]*", str1[i]))):
            continue

        else:
            token = str1[begin:i]

            if(token in keyword):
                output.append(("keyword", token))

            elif(finder(re.findall("^[0-9]+[a-df-zA-Z_]+[a-zA-Z_0-9]*", token))):
                print("lexical error that happened in line : %d " % lineNumber)

            elif(finder(re.findall("^[a-zA-Z]+[.]+[a-zA-Z_0-9]*", token))):
                print("lexical error that happened in line : %d " % lineNumber)

            elif(finder(re.findall("^[0-9]+[.]+[0-9]*[e][a-zA-Z_]+[a-zA-Z_0-9]*", token))):
                print("lexical error that happened in line : %d " % lineNumber)

            elif(finder(re.findall("^[0-9]+[.]+[0-9]*[e]$", token))):
                print("lexical error that happened in line : %d " % lineNumber)

            elif(finder(re.findall("^[0-9]+[.]+[0-9]*[a-df-zA-Z_]+[a-zA-Z_0-9]*", token))):
                print("lexical error that happened in line : %d " % lineNumber)

            elif(finder(re.findall("^[0-9]+[.][0-9]+$", token))):
                output.append(("number", token))

            elif(finder(re.findall("^[0-9]+$", token))):
                output.append(("number", token))

            elif(finder(re.findall("^[0-9]+[.][0-9]+[e][0-9]+$", token))):
                output.append(("number", token))

            elif(finder(re.findall("^[0-9]+[e][0-9]+$", token))):
                output.append(("number", token))

            elif(finder(re.findall("^[a-zA-Z_][a-zA-Z_0-9]*", token))):
                output.append(("identifier", token))

            if(finder(re.findall(punctuationRegex, str1[i]))):
                output.append(("punctuation", str1[i]))

            if(i <= len(str1)-2 and finder(re.findall(comparisonRegex, str1[i]+str1[i+1]))):
                if(not(flag) and len(re.findall(comparisonRegex, str1[i]+str1[i+1])[0]) == 2):
                    output.append(("comparison", str1[i]+str1[i+1]))
                    flag = True

                elif(not(flag) and len(re.findall(comparisonRegex, str1[i]+str1[i+1])[0]) == 1):
                    output.append(("comparison", str1[i]))

                else:
                    flag = False
            elif(i <= len(str1)-2 and finder(re.findall(operationRegex, str1[i]+str1[i+1]))):
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

# remove Space between words

for i in lines:
    lineWords = []
    newArr = i.split(" ")

    for i in range(len(newArr)):
        if(newArr[i] in keyword):
            lineWords.append(newArr[i]+" ")

        elif(newArr[i][0:3] == "for" and newArr[i].split("(")[1] in keyword):
            lineWords.append(newArr[i]+" ")

        else:
            lineWords.append(newArr[i])

    dfa("".join(lineWords), lineNumber)
    lineNumber += 1


# Write in Output File

with open("out/answer.txt", "w") as f:
    for i in output:
        f.write(i[0])
        f.write(":: ")
        f.write(i[1])
        f.write("\n")


# def errorHandling(data: str):
    # # Default Value should be 1 for "int main()"
    # loopsCount = 1
    # parenthesesCount = 0
    # # Loops Count
    # for item in ["for", "while", "if", "else"]:
    #     loopsCount += data.count(item)
    # # Parentheses Count
    # for item in ["{", "}"]:
    #     parenthesesCount += data.count(item)
    # res = data.split("\n")
    # for index in range(len(res)):
    #     # Parentheses Checking in while and for loop
    #     if(res[index].startswith("for") or res[index].startswith("while")):
    #         if(not(finder(re.findall("\)", res[index]) and finder(re.findall("\(", res[index]))))):
    #             print("In Line %d Has Error!!!!" % index)
    #     # Semicolon Checking
    #     if finder(re.findall("^int|float|string|char", res[index])):
    #         if(res[index][-1] != ";" and not finder(re.findall("main", res[index]))):
    #             print("In Line %d Has Error!!!!" % index)
    #      # ParenthesesCount in forLoop Checking
    #     if finder(re.findall("^for", res[index])):
    #         if(res[index].count(";") != 2):
    #             print("In Line %d Has Error!!!!" % index)
    #     # ParenthesesCount Checking
    #     if(loopsCount*2 != parenthesesCount):
    #         print("ParenthesesCount Error!!!!")
    #     # Check File Exist
    #     if(res[index].startswith("#include")):
    #         fileName = res[index].split(" ")[1:]
    #         if(not os.path.isfile(fileName)):
    #             print("In Line %d Has Error!!!!" % index)
