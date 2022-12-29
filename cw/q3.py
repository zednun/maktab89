import re
text = 'Python Exercises'
text = text.replace (" ", "_")
print(text)
text = text.replace ("_", " ")
print(text)

# s = 'this is an __example__'
# translate_table = str.maketrans({' ': '_', '_': ' '})
# print(s.translate(translate_table))