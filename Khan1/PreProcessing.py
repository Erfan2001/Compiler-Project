import re

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
            # with open("""Khan1/%s""" % fileName) as f:
            with open("Khan1/%s" % fileName) as f:
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


def PreProcess():

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

    # Write In New File
    with open("In/new.txt", "w") as f:
        f.write(result3)
