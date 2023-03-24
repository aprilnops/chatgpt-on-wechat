# encoding:utf-8

import json
import os
from common.log import logger

config = {}


def load_config():
    global config
    config_path = "./config.json"
    if not os.path.exists(config_path):
        raise Exception('配置文件不存在，请根据config-template.json模板创建config.json文件')

    config_str = read_file(config_path)
    # 将json字符串反序列化为dict类型
    config = json.loads(config_str)
    config['open_ai_api_key'] = os.getenv('open_ai_api_key')
    config['single_chat_prefix'] = os.getenv('single_chat_prefix')
    config['single_chat_reply_prefix'] = os.getenv('single_chat_reply_prefix')
    config['group_name_white_list'] = os.getenv('group_name_white_list')
    logger.info("[INIT] load config: {}".format(config))



def get_root():
    return os.path.dirname(os.path.abspath( __file__ ))


def read_file(path):
    with open(path, mode='r', encoding='utf-8') as f:
        return f.read()


def conf():
    return config
