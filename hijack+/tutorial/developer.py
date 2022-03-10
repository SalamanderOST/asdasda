import os
import time

print("RESTART DISCORD TO WORK")
apd = os.getenv('APPDATA')
appd = apd + "\\discord\\settings.json"
file1 = open('dev settings\\setting.txt', 'r')
f = file1.read()
file1 = open(appd, 'w')
file1.write(f)
file1 = open(appd, 'r')
f = file1.read()
print(f)
file1.close()
time.sleep(10)
