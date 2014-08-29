
def voiceEnter():
    return 0
def textEnter():
    result = "text"
    import textEnterModule
    result = textEnterModule.result()
    return result
def conversionToNP(inStr):
    result = []
    if "редактировать" in inStr:
        param = "bdModule"
        result.append({'name':"IDLE", 'parameter':param})
    if "яндекс" in inStr:
        if "открыть" in inStr:
            result.append({'name':"www", 'parameter':"www.yandex.ru"})
        else:
            result.append({'name':"return", 'parameter':"яндекс"})
    return result
def BD(keys):
    result = []
    import bdModule
    result = bdModule.result(keys)
    return result
def linker(tableOfContent):
    result = "fileExec"
    import linkerModule
    result = linkerModule.result(tableOfContent)
    return result
def vMachine(fileName):
    result = 0
    import fileExec
    return result

while True:
    userInstructions = textEnter()
    print(userInstructions)
    NpCommand = conversionToNP(userInstructions)
    print(NpCommand)
    tempFilesAtr = BD(NpCommand)
    print(tempFilesAtr)
    scriptName = linker(tempFilesAtr)
    print(">>>>>>>>>>> result script ::::::::")
    with open(scriptName, 'r') as f:
        print(f.read())
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    vMachine(scriptName)

