# 学习Django认证系统
+ User对象的属性：
  + username
  + password
  + email
  + first_name
  + last_name
+ 创建User：
  ```python
  from django.contrib.auth.models import User

  user = User.objects.create_user('john','lennon@thebeatles.com','johnpassword')
  ```
+ 修改密码：
  ```python
  user.set_password('new password')
  user.save()
  ```
+ 验证账户：（低层次的用法）
  ```python
  user = authenticate(username='john',password='secret')
  if user is not Nonne:
    if user.is_active:
      ...
    else:
      ...
  else:
    ...
  ```
+ 登录账户：
  ```python
  login(request,user)
  ```
+ **注意**：第一次获取User的permissions后，Django会将其缓存。因此在为User增加permission后，应当再次获取User，以更新permissions
+ login_required decrator
  login_required() does the following:
    + If the user isn’t logged in, redirect to `settings.LOGIN_URL`, passing the current absolute path in the query string. Example: `/accounts/login/?next=/polls/3/`.
    + If the user is logged in, execute the view normally. The view code is free to assume the user is logged in.

  ```python
  from django.contrib.auth.decorators import login_required

  @login_required
  def my_view(request):
    ...
  ```
+ 可以用 `user_passes_test(test_func, login_url=None, redirect_field_name='next')` 来测试用户是否可以访问特定的页面
  ```python
  from django.contrib.auth.decorators import user_passes_test

  def email_check(user):
      return user.email.endswith('@example.com')

  @user_passes_test(email_check)
  def my_view(request):
    ...
  ```
+ `permission_required(perm, login_url=None, raise_exception=False)`
  ```python
  from django.contrib.auth.decorators import permission_required

  @permission_required('polls.can_vote')
  def my_view(request):
    ...
  ```
# Authentication in EasyAce
## 1. 控制登录用户才能访问的view
### `settings.py`
```python
LOGIN_URL = 'myAuth:login' #设置登录页面的url，如果访问的页面需要登录，则跳转到此url
```
### `views.py`
```python
from django.contrib.auth.decorators import login_required

@login_required
def my_auth(request):
  pass

def login(request):
  next = request.GET.get('next') or ''
  if request.method == 'POST':
    pass
    if user.is_active:
      # 跳转到登入前的页面
      if request.POST['next']:
        next = request.POST['next']
        return HttpResponseRedirect(next)
      # 如果没有登入前页面，则跳转到首页
      else:
        return HttpResponseRedirect('index')
  else:
    return render(request,'login.html',{'next':next})
```
### `login.html`

在`submit`按钮后增加： `<input type="hidden" name="next" value="{{ next }}" />`，使得提交的表单中多一项：`next:{{ next }}`