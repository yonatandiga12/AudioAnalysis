

def addTextToDB(text, path, nameOfFile):
    pathToSave = path + nameOfFile + '.txt'

    with open(pathToSave, "a") as f:
        f.write(text)

