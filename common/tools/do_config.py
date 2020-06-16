# 读取，读出来的数据都是str
# res_value_1 = cf.get('MODE', 'mode')
# res_value_2 = cf['MODE']['mode']
# res_section = cf.sections()
# res_option = cf.options()
# res_option_1 = cf.item('MODE')

import configparser  # 读取配置文件
from project_path import *


class DoConfig:
    @staticmethod
    def read_config(config_file_name, section, option):
        cf = configparser.ConfigParser()
        cf.read(config_file_name, encoding='utf-8')  # 打开文件
        return cf.get(section, option)


if __name__ == '__main__':
    section = 'MODE'
    option = 'mode'
    mode = DoConfig().read_config(conf_path, section, option)
    print(mode)
