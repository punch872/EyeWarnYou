fileRead = open('accident_th.txt','r').read()
splitFile = fileRead.split('\n')

for eachLine in splitFile:
    output =eachLine.encode('utf-8')
    print(output)
    decOutput = output.decode('unicode-escape')
    print(decOutput) 