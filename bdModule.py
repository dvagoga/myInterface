def result(NpList):
    res = []
    for name in NpList:
        listItem = ("file_" + name['name'], name['parameter'])
        res.append(listItem)
    return res
