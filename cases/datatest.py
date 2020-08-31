import yaml

with open("../datas/data.yml",encoding='utf-8') as f:
    a = yaml.safe_load(f)
    print(type(a['add_approve_1'][0]))

