| 名称                  | 调用方法                        | 说明            |
| ------------------- | --------------------------- | ------------- |
| username            | student.username            |               |
| name                | student.name                |               |
| gender              | student.gender              |               |
| email               | student.email               |               |
| phone               | student.phone               |               |
| school              | student.school              |               |
| grade               | student.grade               |               |
| wechat              | student.wechat              |               |
| whatsapp            | student.whatsapp            |               |
| location            | student.location            |               |
| loc_nego            | student.loc_nego            |               |
| time_per_lesson     | student.time_per_lesson     |               |
| lesson_per_week     | student.lesson_per_week     |               |
| start_time          | student.start_time          |               |
| start_time_other    | student.start_time_other    |               |
| prefer_tutor_gender | student.prefer_tutor_gender |               |
| remarks             | student.get_remarks         | 得到一个remarks数组 |
| weakness            | student.weakness            |               |
| wait_match          | student.wait_match          | 是否在等待匹配       |
| tutors_chosen       | 见代码段1                       | 心仪的教师         |
| prefer_subs         | 见代码段2                       | 想要学习的课程       |

```python
# 代码段1
for tutor in student.tutors_chosen.all:
    {{tutor.name}}
    {{...}}
```

```python
# 代码段2
for sub in student.prefer_subs.all:
    {{sub.level}}
    {{sub.name}}
    {{sub.rank}}
    {{sub.other}}
```

