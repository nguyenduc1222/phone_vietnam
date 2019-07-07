import sys
import fileinput
from decimal import *

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))


for i, line in enumerate(fileinput.input(sys.argv[1], inplace=1)):
    newLine = line.replace('\n', '')
    data = newLine.split(",")
    
    data[1] = str(Decimal(float(data[1])))
    data[2] = str(Decimal(float(data[2])))
    data[0] = data[2] + "_" + data[1]
    
    newLine = data[0] + "," + data[1] + "," + data[2] + "\n"
    sys.stdout.write(newLine)  # replace 'sit' and write

