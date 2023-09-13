import re

str = "sadjasdjdsa #ffffff sadasdads #ffffff sadasdads #ffffff sadasdads #ffff"

pattern = r"#[a-fA-F0-9]{6}"  # 正则表达式模式，用于匹配六位十六进制颜色代码

matches = re.findall(pattern, str)  # 查找所有匹配项

print(matches)

'''
正则表达式基本匹配顺序：
------------------------------------------------
导入 re

变量 = 字符串

变量 = 正则表达式

变量 = re.findall(正则表达式变量,字符串变量)

打印（匹配项变量）
'''