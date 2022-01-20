with open('out/answer.txt') as f:
    content = f.readlines()
identifierTable = []
keywords = ["int", "float", "char"]
keyword = None
for i in range(len(content)):
    if (content[i].split(" ")[1][:-1] in keywords):
        keyword = content[i].split(" ")[1][:-1]
    if(content[i].startswith("identifier") and keyword):
        identifierTable.append((keyword,content[i].split(" ")[1][:-1]))
    if(content[i].split(" ")[1][:-1] == ";" and keyword):
        keyword=None

with open("out/ParseTree/ParseTree.gv") as f:
    parseTreeContent=f.readlines()

print(parseTreeContent)