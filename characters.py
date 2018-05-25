import re
x = "asdfklsd1224qq.p r*"
new = re.sub('[\w]+' ,'.',x)
print(len(new))
