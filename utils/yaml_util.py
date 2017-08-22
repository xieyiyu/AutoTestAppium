import yaml

def get_yaml(path):
    """
    获取yaml文件
    :param path: yaml文件路径
    :return:
    """
    try:
        with open(path, encoding='utf-8') as f:
            return yaml.load(f)
    except FileNotFoundError:
        print(u"can't find yaml file: ", path)