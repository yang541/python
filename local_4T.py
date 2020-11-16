import datetime
import os
import re
import threadpool
from mysql_tools_ok import MysqlBasicOperation
from loguru import logger

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
mysql_local = MysqlBasicOperation(ip='localhost', user='root', passwd='root', port=3306)
mysql_4T = MysqlBasicOperation(ip='192.168.0.115', user='qianli', passwd='qianli', port=3306)
insert_table_name = 'db_keyuan.shunqi'


def read_log_id(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            log_id = re.findall('id:(\d+)', content)[-1]
        return log_id
    except:
        return None


def mysql_sel(table_name, file_path):
    log_id = read_log_id(file_path)
    if not log_id:
        log_id = 0
    where_str = 'id>{} limit 2'.format(log_id)
    sel_params = '*'
    result = mysql_local.mysql_select(table_name, sel_params, where_str=where_str)
    log_id = str(log_id)
    if len(log_id) == 0:
        print(f'获取表{table_name}长度为0')
        exit()
    max_iog_id = result[-1]['id']
    logger.info(f'{table_name}**id:{max_iog_id}')
    return result


def mysql_insert(item):
    item.pop('id')
    result = mysql_4T.mysql_insert(table_name=insert_table_name, item_json=item)
    print(item['city'], datetime.datetime.now().replace(microsecond=0), f'存：{result}')


if __name__ == "__main__":
    names = 'shunqi'
    table_name = f'db_shunqi.{names}'
    log_file_path = os.path.join(BASE_DIR, f'local_to_4T/local_4T/{table_name}.log')
    logger.add(log_file_path, encoding='utf-8', enqueue=True)
    while True:
        counts = 40
        task_param_list = mysql_sel(table_name, log_file_path)
        pool = threadpool.ThreadPool(counts)
        reqs = threadpool.makeRequests(mysql_insert, task_param_list)
        [pool.putRequest(req) for req in reqs]
        pool.wait()
