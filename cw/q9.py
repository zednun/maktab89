import re

text = "The following example creates 25 an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
for m in re.finditer("\d+", text):
    print(m.group())
    print("Index position:", m.start() ,m.end())