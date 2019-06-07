def parsetoarray(inputtext):
    data=[]
    data_lines=inputtext.split('\r\n')
    for line in data_lines:
        line = line.replace('\t',' ')
        data.append(line)
    return data