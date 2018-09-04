from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from toys.models import Toy
from toys.serializers import ToySerializer
# Create your views here.
"""
当Django服务器收到HTTP请求时，Django会创建一个HttpRequest实例，特别是一个django.http.HttpRequest对象。此实例包含有关请求的元数据，此元数据包括HTTP谓词，如GET，POST或PUT。 method属性提供了一个字符串，表示请求中使用的HTTP谓词或方法。
"""


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


"""
列出所有toy或者创建一个新的toy
"""
@csrf_exempt
def toy_list(request):
    if request.method == 'GET':
        toys = Toy.objects.all()
        toys_serializer = ToySerializer(toys, many=True)
        return JSONResponse(toys_serializer.data)

    elif request.method == 'POST':
        # 根据请正文中包含的json数据创建新的toy。
        # 解析json并保存到toy_data
        toy_data = JSONParser().parse(request)
        # 创建toy_serializer实例
        toy_serializer = ToySerializer(data=toy_data)
        # 确认toy实例是否有效，如果有效则保存
        if toy_serializer.is_valid():
            toy_serializer.save()
            return JSONResponse(toy_serializer.data, status=status.HTTP_201_CREATED)
        return JSONResponse(toy_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def toy_detail(request, pk):
    try:
        toy = Toy.objects.get(pk=pk)
    except Toy.DoesNotExits:
        return HttpResponse(status=status.HTTP_404HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        toy_serializer = ToySerializer(toy)
        return JSONResponse(toy_serializer.data)
    elif request.method == 'PUT':
        toy_data = JSONParser().parse(request)
        toy_serializer = ToySerializer(toy, data=toy_data)
        if toy_serializer.is_valid():
            toy_serializer.save()
            return JSONResponse(toy_serializer.data)
        return JSONResponse(toy_serializer.errors, status=status.HT400HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        toy.delete()
    return HttpResponse(status=status.http2HTTP_204_NO_CONTENT)
