def parsetoarray(inputtext):
    data=[]
    data_lines=inputtext.split('\r\n')
    for line in data_lines:
        line = line.replace('\t',' ')
        data.append(line)
    return data

def parsetoarrayfromfile(inputtext):
    data=[]
    inputtext = inputtext[2:-1]
    data_lines=inputtext.split('\\n')
    for line in data_lines:
        line = line.replace('\\r', ' ')
        line = line.replace('\\t',' ')
        data.append(line)
    return data