from my_tools import myrequests, dingding
import requests
from faker import Faker
import urllib3

urllib3.disable_warnings()
fake = Faker()

headers = {
    # 'cookie': '_xmLog=h5&f4df416c-fae8-491f-8ff8-962ee9ffca49&2.1.2; x_xmly_traffic=utm_source%253A%2526utm_medium%253A%2526utm_campaign%253A%2526utm_content%253A%2526utm_term%253A%2526utm_from%253A; Hm_lvt_4a7d8ec50cfd6af753c4f8aee3425070=1603182910; x_xmly_row_key=79798979834594032_album_3dd8a147d7e44c769730b44bfc98b00f; row_key=79798979834594032_album_3dd8a147d7e44c769730b44bfc98b00f; h5_channel=ambassador_79798979834594032_album_3dd8a147d7e44c769730b44bfc98b00f; x_xmly_cps_promote_info="v2_Ys7hs8UAMiwGSbr5imqbORB7gmsiLUX045fSCLgFQrfn+QtrIb0djVQp9cx4r2f8cDE7eGezLBADpaYpofBWHJoPr6BfQTlJRmHVwPHCToEFL/0e4DTjM26OzE8LqdXVKZTO+bqQQT52B1sQlksl9tSbTH+D7wSC8drCwfhszVKZStJx93YXEA=="; cps_promote_info="v2_Ys7hs8UAMiwGSbr5imqbORB7gmsiLUX045fSCLgFQrfn+QtrIb0djVQp9cx4r2f8cDE7eGezLBADpaYpofBWHJoPr6BfQTlJRmHVwPHCToEFL/0e4DTjM26OzE8LqdXVKZTO+bqQQT52B1sQlksl9tSbTH+D7wSC8drCwfhszVKZStJx93YXEA=="; x_xmly_order_context=%7B%22cps_promote_info%22%3A%22v2_Ys7hs8UAMiwGSbr5imqbORB7gmsiLUX045fSCLgFQrfn%2BQtrIb0djVQp9cx4r2f8cDE7eGezLBADpaYpofBWHJoPr6BfQTlJRmHVwPHCToEFL%2F0e4DTjM26OzE8LqdXVKZTO%2BbqQQT52B1sQlksl9tSbTH%2BD7wSC8drCwfhszVKZStJx93YXEA%3D%3D%22%2C%22orderFrom%22%3A%226%22%2C%22rowKey%22%3A%2279798979834594032_album_3dd8a147d7e44c769730b44bfc98b00f%22%7D; order_context=%7B%22cps_promote_info%22%3A%22v2_Ys7hs8UAMiwGSbr5imqbORB7gmsiLUX045fSCLgFQrfn%2BQtrIb0djVQp9cx4r2f8cDE7eGezLBADpaYpofBWHJoPr6BfQTlJRmHVwPHCToEFL%2F0e4DTjM26OzE8LqdXVKZTO%2BbqQQT52B1sQlksl9tSbTH%2BD7wSC8drCwfhszVKZStJx93YXEA%3D%3D%22%2C%22orderFrom%22%3A%226%22%2C%22rowKey%22%3A%2279798979834594032_album_3dd8a147d7e44c769730b44bfc98b00f%22%7D; x_xmly_isDistributor=false; isDistributor=false; 1&remember_me=y; 1&_token=262372295&A0C12910240N4E9A6C663B5130FF67555EB8B08EB00FFF270B727CA1CE5FC77E783B4CC621D798M5979933897F8328_; 1_l_flag=262372295&A0C12910240N4E9A6C663B5130FF67555EB8B08EB00FFF270B727CA1CE5FC77E783B4CC621D798M5979933897F8328__2020-10-2016:57:22; Hm_lpvt_4a7d8ec50cfd6af753c4f8aee3425070=1603184244',
    'user-agent': fake.chrome()
}

"""
会员以及试听的暂时没考虑解决

"""


def sound_list(spider_url):
    res = requests.get(url=spider_url, headers=headers, verify=False)
    nodes = res.json()['data']['tracks']
    for node in nodes:
        trackId = node['trackId']
        title = node['title']
        down_load(trackId, title)


def down_load(trackId, name):
    link = 'https://www.ximalaya.com/revision/play/v1/audio?id={}&ptype=1'.format(trackId)
    res = requests.get(url=link, headers=headers, verify=False)
    try:
        src = res.json()['data']['src']
        print(name, '=====>', src)
        info = requests.get(src, verify=False)
        con = info.content
        with open('D:\\喜玛亚拉\\吃货必备、人与自然\\' + name + '.m4a', 'wb') as f:
            f.write(con)
            print('保存成功', name)
    except Exception as e:
        print('data参数没取到', e)
        dingding(f'名字--{name}  data参数没取到---作品链接{src}')


if __name__ == '__main__':
    #  分类 id
    # albumId = '4256765'
    # albumId = '12576446'
    # albumId = '291718'
    # albumId = '6862804'
    # albumId = '41720334'
    # albumId = '26441397'
    # albumId = '37676146'
    albumId = '35426374'
    for page in range(1, 6):
        url = f'https://www.ximalaya.com/revision/album/v1/getTracksList?albumId={albumId}&pageNum={page}'
        sound_list(url)
