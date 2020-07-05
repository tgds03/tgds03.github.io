#!/usr/bin/python3
import re, sys

try:
    with open(sys.argv[1], 'r') as f: data = f.read()
except IndexError:
    sys.exit("Error : please append a path of file will be converted")
except FileNotFoundError:
    sys.exit("Error : cannot open file: " + sys.argv[1])

# linebreakFormat = re.compile(r'\\{2}')
inlineFormat = re.compile(r'\$([^\$\n]+?)\$')
blockFormat = re.compile(r'\${2}(.*?)\${2}', re.DOTALL)

# data = re.sub(inlineFormat, r'{% raw %}\(\1\){% endraw %}', data)
# data = re.sub(blockFormat, r'{% raw %}\[\1\]{% endraw %}', data)
# data = re.sub(linebreakFormat, r'\\\\\\\\', data)
data = re.sub(inlineFormat, r'`\( \1 \)`', data)
data = re.sub(blockFormat, r'`\[ \1 \]`', data)
# for match in re.finditer(blockFormat, data):
#     print(match.group())

# print(data)
with open(sys.argv[1], 'w') as f:
    f.write(data)