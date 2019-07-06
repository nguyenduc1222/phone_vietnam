import sys
import fileinput
from decimal import *

# replace all occurrences of 'sit' with 'SIT' and insert a line after the 5th
stt = 0
for i, line in enumerate(fileinput.input('xaw2', inplace=1)):
    newLine = line.replace('\n', '')
    data = newLine.split(",")
    
    data[1] = str(Decimal(data[1]))
    data[2] = str(Decimal(data[2]))
    data[0] = data[2] + "_" + data[1]
    
    newLine = data[0] + "," + data[1] + "," + data[2] + "\n"
    sys.stdout.write(newLine)  # replace 'sit' and write

