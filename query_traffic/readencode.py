import io

sampleFile = open('traffic.txt','rb').read()
splitFile = sampleFile.split('\n')

for eachLine in splitFile:
    x= eachLine.encode('utf-8')
    en = x.decode('unicode-escape')
    output_file = open('Output.txt', 'w')
    output_file.write(en)
    output_file.close()


