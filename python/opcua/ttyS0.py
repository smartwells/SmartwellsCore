#import os


with open('/dev/ttyS0', 'wb') as f:
    print(f)
    f.write(b'$01F')
print(f)

'''
f = open('/dev/ttyS0', 'wb')
print(f)
f.write(b'$01F')
f.close()
f = open('/dev/ttyS0', 'rb')
print(f.read())
f.close()
'''
