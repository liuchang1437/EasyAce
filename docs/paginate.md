+ Django中有关分页的实现在 `django/core/paginator.py` 中。
+ 向Paginator传入带有count属性的类（列表，元组，...），以及每页的元素数量。`p = Paginator(objects, 2)`
+ Paginator有如下属性和方法：
  + count 总元素数量
  + num_pages 页面数
  + page_range 页面的范围，**index从1开始**
  + page(<page_num>) 获取第<page_num>页
+ 每一页的对象有如下属性和方法：
  + object_list
  + number 当前页面的页数
  + paginator 与page相关联的Paginator对象
  + has_next()
  + has_previous()
  + has_other_pages() 存在前一页或者后一页
  + next_page_number()
  + previous_page_number()
  + start_index()
  + end_index()
+ 属性示例
  ``` Python
  >>> from django.core.paginator import Paginator
  >>> objects = ['john', 'paul', 'george', 'ringo']
  >>> p = Paginator(objects, 2) # 向Paginator传入带有count属性的类（列表，元组，...），以及每页的元素数量。

  >>> p.count
  4
  >>> p.num_pages
  2
  >>> p.page_range
  [1, 2]

  >>> page1 = p.page(1)
  >>> page1
  <Page 1 of 2>
  >>> page1.object_list
  ['john', 'paul']

  >>> page2 = p.page(2)
  >>> page2.object_list
  ['george', 'ringo']
  >>> page2.has_next()
  False
  >>> page2.has_previous()
  True
  >>> page2.has_other_pages()
  True
  >>> page2.next_page_number()
  Traceback (most recent call last):
  ...
  EmptyPage: That page contains no results
  >>> page2.previous_page_number()
  1
  >>> page2.start_index() # The 1-based index of the first item on this page
  3
  >>> page2.end_index() # The 1-based index of the last item on this page
  4

  >>> p.page(0)
  Traceback (most recent call last):
  ...
  EmptyPage: That page number is less than 1
  >>> p.page(3)
  Traceback (most recent call last):
  ...
  EmptyPage: That page contains no results
  ```
+ view 中使用Paginator：假设已经引入类Contacts模型。
  ```
  from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

  def listing(request):
      contact_list = Contacts.objects.all()
      paginator = Paginator(contact_list, 25) # Show 25 contacts per page

      page = request.GET.get('page')
      try:
          contacts = paginator.page(page)
      except PageNotAnInteger:
          # If page is not an integer, deliver first page.
          contacts = paginator.page(1)
      except EmptyPage:
          # If page is out of range (e.g. 9999), deliver last page of results.
          contacts = paginator.page(paginator.num_pages)

      return render_to_response('list.html', {"contacts": contacts})
  ```
+ 模板中使用Paginator:
  ```
  <div class="pagination">
    <span class="step-links">
        {% if contacts.has_previous %}
            <a href="?page={{ contacts.previous_page_number }}">previous</a>
        {% endif %}

        <span class="current">
            Page {{ contacts.number }} of {{ contacts.paginator.num_pages }}.
        </span>

        {% if contacts.has_next %}
            <a href="?page={{ contacts.next_page_number }}">next</a>
        {% endif %}
    </span>
</div>
  ```
+ Paginator 构造器：
  `class Paginator(object_list, per_page, orphans=0, allow_empty_first_page=True)[source]`
  + orphans: 最后一页的最小元素个数。如果少于这个，最后一页的元素会被合并到之前一页。
  + allow_empty_first: 允许第一页为空，否则报错。
+ 异常：
  + InvalidPage：调用Paginator.page()方法时，如果page_num存在异常，会抛出InvalidPage.
  + PageNotAnIngeter: InvalidPage的子类，page_num不是个整数
  + EmptyPage：page_num是整数，但是请求页面为空
