import re
txt="The is an aux"
print(re.search("^The.*aux$",txt))# this is to check the pattern
time="The time is 11:45"
print(re.findall("[0-4][0-9]",time))
print(re.findall("[a-c].*",txt))