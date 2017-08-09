import yaml

# 获取Yaml文件
def get_yaml(path):
    try:
        with open(path, encoding='utf-8') as f:
            return yaml.load(f)
    except FileNotFoundError:
        print(u"can't find yaml file: ", path)