# HTML表单
+ `<form>` 的 action 属性指定 URL，method 属性指定方法（GET，POST）。

# Django的Form类入门
+ 一个例子：

  ```python
  # forms.py
  from django import forms

  class NameForm(forms.Form):
      your_name = forms.CharField(label='Your name', max_length=100)
  ```    
+ 处理表单的视图例子：

  ```python
  from django.shortcuts import render
  from django.http import HttpResponseRedirect

  from .forms import NameForm

  def get_name(request):
      # if this is a POST request we need to process the form data
      if request.method == 'POST':
          # create a form instance and populate it with data from the request:
          form = NameForm(request.POST)
          # check whether it's valid:
          if form.is_valid():
              # process the data in form.cleaned_data as required
              # ...
              # redirect to a new URL:
              return HttpResponseRedirect('/thanks/')

      # if a GET (or any other method) we'll create a blank form
      else:
          form = NameForm()

      return render(request, 'name.html', {'form': form})
  ```
+ 一个模板例子：

  ```python
  <form action="/your-name/" method="post">
      {% csrf_token %}
      {{ form }}
      <input type="submit" value="Submit" />
  </form>
  ```

# Django Form类详解
+ 所有的表单都作为`django.forms.Form`的子类
+ `ModelForm`, 它将根据 Model 类构建一个表单以及适当的字段和属性。
+ 一旦通过 is_valid() 成功验证，验证后的表单数据将位于form.cleaned_data 字典中。这些数据已经转换为Python 的类型。
+ 视图中如何处理表单数据：

  ```python
  from django.core.mail import send_mail

  if form.is_valid():
      subject = form.cleaned_data['subject']
      message = form.cleaned_data['message']
      sender = form.cleaned_data['sender']
      cc_myself = form.cleaned_data['cc_myself']

      recipients = ['info@example.com']
      if cc_myself:
          recipients.append(sender)

      send_mail(subject, message, sender, recipients)
      return HttpResponseRedirect('/thanks/')
  ```
+ @阿康，看这个：[表单渲染选项](http://python.usyiyi.cn/django/topics/forms/index.html#form-rendering-options)
+ 动态的初始值：`f = ContactForm(initial={'subject': 'Hi there!'})`
+ 可以通过 `f.fields['name']` 访问表单中的字段

# 从模型创建表单
+ ModelForm：
  ```python
  from django.forms import ModelForm
  from myapp.models import Article
  class ArticleForm(ModelForm):
    class Meta:
      model = Article
      fields = ['pub_date',...]
  ```
