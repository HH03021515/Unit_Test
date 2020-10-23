# author:ToddCombs
import yaml
file = open('a.yaml', encoding='utf-8')
# 打印字典
res = yaml.load(file, Loader=yaml.FullLoader)
print(res)