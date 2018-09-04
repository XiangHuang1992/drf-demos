from datetime import datetime
from django.utils import timezone
from django.utils.six import BytesIO
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from toys.models import Toy
from toys.serializers import ToySerializer

toy_release_date = timezone.make_aware(datetime.now(), timezone.get_current_timezone())
toy1 = Toy(name='Snoopy talking action figure', description='Snoopy speaks five languages', release_date=toy_release_date, toy_category='Action figures', was_include_in_home=False)

toy1.save()
toy2 = Toy(name='Hawaiian Barbie', description='Barbie loves Hawaii', release_date=toy_release_date, toy_category='Dolls', was_include_in_home=True)

toy2.save()

print(toy1.pk)
print(toy1.name)
print(toy1.create)
print(toy1.was_include_in_home)
print(toy2.pk)
print(toy2.name)
print(toy2.create)
print(toy2.was_include_in_home)

serializer_for_toy1 = ToySerializer(toy1)
print(serializer_for_toy1.data)
serializer_for_toy2 = ToySerializer(toy2)
print(serializer_for_toy2.data)
json_renderer = JSONRenderer()
toy1_rendered_into_json = json_renderer.render(serializer_for_toy1.data)
toy2_rendered_into_json = json_renderer.render(serializer_for_toy2.data)
print(toy1_rendered_into_json)
print(toy2_rendered_into_json)

# 使用json字符串创建一个新的toy
json_string_for_new_toy = '{"name":"Clash Royale play set","description":"6 figures from Clash Royale", "release_date":"2017-10-09T12:10:00.776594Z","toy_category":"Playset","was_included_in_home":false}'
# 字符串转换成二进制数据
json_bytes_for_new_toy = bytes(json_string_for_new_toy, encoding="UTF-8")
# buff缓冲
stream_for_new_toy = BytesIO(json_bytes_for_new_toy)
# 反序列化
parser = JSONParser()
parsed_new_toy = parser.parse(stream_for_new_toy)
print(parsed_new_toy)

new_toy_serializer = ToySerializer(data=parsed_new_toy)
# 注意：在创建序列化传递数据关键参数时，我们必须在尝试访问序列化数据之前调用is_valid()
if new_toy_serializer.is_valid():
    toy3 = new_toy_serializer.save()
    print(toy3.name)

"""
正如我们从前面的代码中看到的那样，Django REST框架可以很容易地将对象序列化为JSON，并从JSON反序列化为对象，这是我们必须执行CRUD操作的RESTful Web服务的核心要求。
"""

quit()
