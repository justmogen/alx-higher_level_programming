#!/usr/bin/python3
changed = ""
for i in range(97, 123):
    if i == 101 or i == 113:
        continue
    changed = changed + chr(i)
print("{}".format(changed), end='')
