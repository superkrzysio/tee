import sys
import datetime

fp = None
if len(sys.argv) == 1:
    print("Usage: command | tee output.txt")
    exit()

if len(sys.argv) > 1:
    fp = open(sys.argv[1], "w")


for line in sys.stdin:
    dt = datetime.datetime.now() 
    mark = dt.strftime("%H:%M:%S") + "." + str(int(dt.microsecond/1000))
    line = mark + ": " + str(line)
    if fp is not None:
        fp.write(line)
    print(line, end="")

if fp is not None:
    fp.close()
