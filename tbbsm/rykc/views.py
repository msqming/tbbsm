from django.shortcuts import render
from django.shortcuts import redirect


from rykc import models

def index(request):


    return render(request,'index.html')

def api_index(request):

    data_list = models.CommInfo.objects.filter(id__lt=20)
    res = {
        'code':0,
        'msg':'',
        'data':[]
    }
    for data in data_list:
        res['data'].append({
            'id': data.id,
            '型号': data.xinghao,
            '品类': data.pinglei,
            '新/旧': data.new_old,
            '定位': data.dingwei,
            '品名': data.pingming,
            'CPU': data.cpu,
            '显卡': data.xianka,
            '内存': data.neicun,
            'SSD': data.ssd,
            'HHD': data.hhd,
            '模具名称': data.model_name,
            '配置': data.config,
            'PN': data.pn
        })

    return render(request, 'api_index.html',{'res':res})
