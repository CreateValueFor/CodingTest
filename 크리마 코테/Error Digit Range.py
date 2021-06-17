def findRange(num):
    num = str(num)
    maxV, minV = num, num
    minI = -1
    replaceM, replacem = "", ""
    for i in range(len(num)):
        if num[i] == '9':
            continue
        replaceM = maxV[i]
        break
    if replaceM != "":
        maxV = maxV.replace(replaceM, '9')
    if num[0] != '1':
        replacem = minV[0]
        minV = minV.replace(replacem,'1')
    else:
        for i in range(1, len(num)):
            if num[i] != '1':
                replacem = minV[i]
                break
        if replacem != "":
            minV = minV.replace(replacem,'0')

    return int(maxV) - int(minV)

print(findRange(123512))