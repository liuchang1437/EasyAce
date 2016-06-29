#URL
## 命名组：
`(?P<name>pattern)`
## URL的反向解析：
```
from django.conf.urls import url

from . import views

urlpatterns = [
    #...
    url(r'^articles/([0-9]{4})/$', views.year_archive, name='news-year-archive'),
    #...
]
```
在模板中：
```
<a href="{% url 'news-year-archive' 2012 %}">2012 Archive</a>

<ul>
{% for yearvar in year_list %}
<li><a href="{% url 'news-year-archive' yearvar %}">{{ yearvar }} Archive</a></li>
{% endfor %}
</ul>
```
在python代码中：
```
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

def redirect_to_year(request):
    # ...
    year = 2006
    # ...
    return HttpResponseRedirect(reverse('news-year-archive', args=(year,)))
```
+ 注意，若在appname前加`namespace:`，django会在include()的urls中寻找url，因此如果没有定义include()，使用名字空间应该是找不到想要的url的。

## 通过传统的”?”传递参数 
例如，http://127.0.0.1:8000/plist/?p1=china&p2=2012，url中‘?’之后表示传递的参数，这里传递了p1和p2两个参数。
通过这样的方式传递参数，就不会出现因为正则匹配错误而导致的问题了。在Django中，此类参数的解析是通过request.GET.get方法获取的。
配置URL及其视图如下：
```
url(r'^plist/$', helloParams1）
 
def helloParams(request):
    p1 = request.GET.get('p1')
    p2 = request.GET.get('p2')
    return HttpResponse("p1 = " + p1 + "; p2 = " + p2)
```