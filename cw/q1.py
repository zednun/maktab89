import re
# text = input ("Enter your string:").split(,)
text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
for match in re.findall(pattern, text):
    print(f'{match}')