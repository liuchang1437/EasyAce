# 使用
## 消息级别
  |Level|tag|
  |-----|---|
  |DEBUG|debug|
  |INFO|info|
  |SUCCESS|success|
  |WARNING|warning|
  |ERROR|error|

## 视图中使用消息
+ 新增消息
  ```python
  from django.contrib import messages
  messages.add_message(request, messages.INFO,'message')

  messages.debug(request,'message')
  messages.info(request,'message')
  messages.success(request,'message')
  messages.warning(request,'message')
  messages.error(request,'message')
  ```
+ 获取消息
  ```python
  from django.contrib.messages import get_messages
  storage = get_messages(request)
  for message in storage:
    do_something_with_the_message(message)
  ```

## 模板中显示消息
+ 示例：
  ```html
  {% if messages %}
  <ul class="messages">
      {% for message in messages %}
      <li{% if message.tags %} class="{{ message.tags }}"{% endif %}>
          {% if message.level == DEFAULT_MESSAGE_LEVELS.ERROR %}Important: {% endif %}
          {{ message }}
      </li>
      {% endfor %}
  </ul>
  {% endif %}
  ```

## message类
+ 属性：
  + message
  + level
  + tags
  + extra_tags
  + level_tag

# message in EasyACE
## 模板中使用：
在`base.html`文件中加入如下代码：
```html
  {% if messages %}
  <ul class="messages">
    {% for message in messages %}
    <li>
      <div {% if message.tags %} class="alert alert-{{ message.tags }} alert-dismissible"{% endif %} role="alert">
        <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
        {{ message }}
      </div>
    </li>
    {% endfor %}
  </ul>
  {% endif %}
```
@阿康，该消息与网站图标重合类，需要进行位置调整

## view中使用：
在完成表单处理后，发出消息通知用户成功处理。