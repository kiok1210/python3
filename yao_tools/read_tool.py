
@staticmethod
def read_config(md_file, sign=':'):
    '''
    读取文件，参数化，参数文件按照key1:value1 换行 key2:value2的方式存储
    :param md_file: 文件路径，一般放在同级目录下
    :param sign: 默认符号使用冒号分隔参数
    :return: jsonlines type {}
    '''

    data = open(md_file, 'r')
    config_data = data.readlines()
    data.close()

    jsonlines = {}
    for line in config_data:
        print(line)
        line_arr = line.split(sign)
        jsonlines[line_arr[0]] = line_arr[1]

    return jsonlines