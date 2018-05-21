import linecache
from TaskRunner import *

def cal2():
    print str(125835842357435 * 52345234)
    time.sleep(2)
    print str(1 * 4523452345234524572348577385745)

def cal1():
    time.sleep(4)
    print str(1000000000000000000000000 / 33434452345)

datalist = [cal1, cal2]
runTasks(datalist)
