# CitiesTranslatePinyin  
将文本内的的中文城市名称以首字母大写排序，并额外生成关联外键，转化为Json格式。  
也可以用于排序人名、商标等信息。

Json格式可以通过修改代码来重新自由构建。

```angular2html
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
```

使用命令安装`pypinyin`
```
pip install -r requirements.txt
```

