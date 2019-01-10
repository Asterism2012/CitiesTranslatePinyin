#coding=utf-8
from pypinyin import lazy_pinyin
import re
import json

'''
@Help: 用于将文本(由redis导出的db_citys.txt)中的城市信息转化为Json格式，以首字母大写进行排序，并关联外键
@From：魏泯
@UpdateTime: 2019年1月10日12点18分
@Version：v1.0
@Json预览
    # all_citys_info = [
    #     { A: {
    #         city: [],
    #         foreign: int,
    #     }},
    #     { B: {
    #         city: [],
    #         foreign: int,
    #     }},
    #      ...
    # ]
'''

def TranslatePinyin(string):
    '''
    拼音转换
    :param string: str 地区名称
    :return: str 首字母拼音
    '''
    if isinstance(string,str) and len(string) != 0:     # 边界判断
        pinyinList = lazy_pinyin(string)
        try:        # 尝试获取第一个汉字的拼音，最后将它返回
            fristPinyin = pinyinList[0]
            return fristPinyin
        except:
            print('程序错误')

def TranslateList():
    '''
    列表转换
    Parms: db_citys.txt 将包含地区的文本文档转化为列表
    :return: List
    '''
    new_str_list = []
    f = open('db_citys.txt','rb')       # 读取文件
    line = f.readlines()    # 列表形式换行读取
    for i in line:
        if len(i) > 1:      # 对追加内容进行边界判断
            result = re.match('\w+', i.decode())
            new_str_list.append(result.group())     # 追加到
    f.close()
    return new_str_list

def TranslateJson():
    '''
    Json转换
    :return: JsonStr 将所有的对应的 地区、外键、首字母进行映射
    '''

    forgKeyMappingDic = {chr(i): index + 1 for index, i in enumerate(range(ord("A"), ord("Z") + 1))}        # 生成外键映射, a-z对应数字1-26
    new_city_list = TranslateList()     # 城市列表
    end_all_citys_json = []     # 最终的Json
    end_pinyin_list = list(map(TranslatePinyin, new_city_list))     # 拼音列表

    for i,j in forgKeyMappingDic.items():       # 循环外键映射字典
        _itemDic = {}       # 临时字典
        _itemLis = []       # 临时列表
        for index, x in enumerate(end_pinyin_list):
            if x[0].lower() == i.lower():       # 判断城市首字母拼音是否符合大写字母索引的要求
                _itemLis.append(new_city_list[index])        # 用拼音列表的下标去取城市列表的内容，追加到临时列表中
        '''将生成后的“城市Lis”（value）映射到“city”（key），
        将“外键索引j”（value）映射到“forgkey”（key）,
        最后将这个字典(value)映射到“大写字母索引i”(key)
        '''
        if len(_itemLis) == 0:
            _itemLis.append('暂无城市信息')
        _itemDic[i] = {'city': _itemLis, 'forgkey': j}
        end_all_citys_json.append(_itemDic)     # 将临时字典追加到Json列表中
    return json.dumps(end_all_citys_json)
TranslateJson()

# 预览Json
# print(TranslateJson())