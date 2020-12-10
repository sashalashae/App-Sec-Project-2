import os
arr = os.listdir()
for i in arr:
    command = './giftcardreader 1 ' + i
    os.system(command)
    command = ''