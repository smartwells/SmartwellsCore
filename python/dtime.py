import _datetime
import time

d = _datetime.datetime.now()
d = d.strftime('%Y-%m-%d %H.%M.%S')
print(d)
print(time.localtime())
