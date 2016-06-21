# To do
1. 查看 Django 模型的数据类型，确认数据库每列的数据类型。
2. 扩展内建模型 User
3. 编写数据库测试用例。

# 相关知识学习
## Part 1 - Models
1. 每个 model 是 `django.db.models.Model` 的子类
2. 每个 model 的属性代表数据库的一个域（列）
3. 每个 model 自动生成 id 列
4. Field Type，[Model field types](https://docs.djangoproject.com/en/1.9/ref/models/fields/#model-field-types)
5. Field Options, [Model field options](https://docs.djangoproject.com/en/1.9/ref/models/fields/#field-options)

## Part 2 - 重写内建认证系统 [文档](https://docs.djangoproject.com/en/1.9/topics/auth/customizing/#substituting-a-custom-user-model)
### 目标：
1. 使用 email adress 登入。
2. 能够区分教师，学生以及管理员。
3. 如果这部分比较麻烦，可以直接扩展 Default User model: 	
>Simply subclass `django.contrib.auth.models.AbstractUser` and add your custom profile fields

### 细节：
+ `AUTH_USER_MODEL = 'users.MyUser'`
+ 指定外键时，使用 `settings.AUTH_USER_MODEL` 来指定自定义用户模型
+ 使用 `django.contrib.auth.get_user_model()` 来引用用户模型
+ **通过继承 `AbstractBaseUser` 来实现自己的 User 模型**
```
class MyUser(AbstractBaseUser):
	identifier = models.EmailField(unique=True)
	USERNAME_FIELD = 'identifier'
```
+ 指定 `REQUIRED_FIELDS` ，可以指定在创建用户时需要填写的字段

# 设计与实现
### Tutor
| name	 		| field 			| remarks |
|:------		|:------:			| :--------:|
|id 				|AutoField		|自动添加|
|name				|CharField		|max_length=50|
|gender			|CharField		|见表后附录|
|birth			|DateField		|auto_now=False, auto_now_add=False|
|email			|EmailField		||
|phone			|CharField		|max_length=20|
|company_school|CharField	||
|wechat			|CharField||
|grad_test_type	|CharField|见表后附录|
|grad_results|TextField		|由前端负责组织这个域(?)|
|gce_level	|TextField		|由前端负责组织这个域(?)|
|location		|TextField		||
|state			|BooleanField	|default=False|
|duration		|CharField		|见表后附录|
|num_taught	|CharField		|见表后附录|
|stu_achive	|TextField		||
|star				|FloatField		|或 DecimalField(?)|
|role				|CharField		|见表后附录|
|students		||多对多|
|reviews		||一对多|
|prefer_tutors||一对多|
|certifacation|TextField	||
**附录：**
```python
# ============ gender =================
MALE = 'M'
FEMALE = 'F'
GENDER_CHOICES = (
	(MALE, 'Male'),
	(FEMALE, 'Female'),
)
gender = models.CharField(
	max_length=2,
	choices=GENDER_CHOICES,
)

# ========== grad_test_type ============
GRAD_TEST_TYPE = (
	('AL','A-level'),
	('PD','Polytechnic Diploma Test'),
	('GK','Gaokao'),
	('IB','IB'),
	('OT','Others'),
)
grad_test_type = models.CharField(
	max_length=2,
	choices=GRAD_TEST_TYPE,
)

# ============ duration ===============
DURATION_CHOICES = (
	('NV','Never'),
	('M1','1 month'),
	('M1_3','1-3 months'),
	('M3_6','3-6 months'),
	('M6_12','6-12 months'),
	('LT1Y','>1 year'),
	('LT2Y','>2 years'),
)
duration = models.CharField(
	max_length=6,
	choices=DURATION_CHOICES,
)

# ============== role =================
ROLE_CHOICES = (
	('NM','Normal'),
	('ST','Star'),
)
role = models.CharField(
	max_length=2,
	choices=ROLE_CHOICES,
)
```
### 
### Relationship 
1. Many to One: `ForeignKey`
2. Many to Many: `ManyToManyField`（只在一个model中定义；可以利用intermediate model附加额外信息，通过through指定）
见[ExtraField](https://docs.djangoproject.com/en/1.9/topics/db/models/#extra-fields-on-many-to-many-relationships)
3. One to One: `OneToOneField`

##Django中的用户认证
### 概览
认证系统包含：
+ 用户
+ 权限：二元（是/否）标志指示一个用户是否可以做一个特定的任务。
+ 组：对多个用户运用标签和权限的一种通用的方式。
+ 一个可配置的密码哈希系统
+ 用于登录用户或限制内容的表单和视图
+ 一个可插拔的后台系统
其他第三方包中实现的功能：
+ 密码强度检查
+ 登录尝试的制约
+ 第三方认证（例如OAuth）

###安装
已经默认安装，配置包含在settings.py中，INSTALLED_APPS设置中的两个选项：
1. 'django.contrib.auth'包含认证框架的核心和默认的模型。
2. 'django.contrib.contenttypes'是Django内容类型系统，它允许权限与你创建的模型关联。
MIDDLEWARE_CLASSES中的三个选项：
1. SessionMiddleware管理请求之间的会话。
2. AuthenticationMiddleware使用会话将用户与请求管理起来。
3. SessionAuthenticationMiddleware在密码改变后登出用户所有会话。

###认证
``` python
if request.user.is_authenticated():
	pass
else:
	pass

from django.contrib.auth import authenticate, login

def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
        else:
            # Return a 'disabled account' error message
            ...
    else:
        # Return an 'invalid login' error message.
        ...
```
### longin_required装饰器 [文档](http://python.usyiyi.cn/django/topics/auth/default.html#the-login-required-decorator)

### 扩展 User 模型 [文档](https://docs.djangoproject.com/en/1.9/topics/auth/customizing/#extending-the-existing-user-model)
1. 使用 OneToOneField 来为 User 模型扩展列。

	```Python
	from django.contrib.auth.models import User

	class Employee(models.Model):
			user = models.OneToOneField(User, on_delete=models.CASCADE)
			department = models.CharField(max_length=100)
	```









