| 名称              | 调用方法                  | 说明              |
| --------------- | --------------------- | --------------- |
| username        | tutor.username        |                 |
| name            | tutor.name            |                 |
| gender          | tutor.gender          |                 |
| birth           | tutor.birth           |                 |
| email           | tutor.email           |                 |
| phone           | tutor.phone           |                 |
| school          | tutor.school          |                 |
| wechat          | tutor.wechat          |                 |
| whatsapp        | tutor.whatsapp        |                 |
| top_teacher     | tutor.top_teacher     | 布尔变量，是否是金牌教师    |
| tutor_location1 | tutor.tutor_location1 |                 |
| tutor_location2 | tutor.tutor_location2 |                 |
| tutor_location3 | tutor.tutor_location3 |                 |
| teach_duration  | tutor.teach_duration  |                 |
| num_taught      | tutor.num_taught      |                 |
| achivement      | tutor.achivement      |                 |
| prefer_subs     |                       | 想要教的课程，见下方代码段1  |
| refer_subs      |                       | 相关课程及成绩，见下方代码段2 |

```python
# 代码段1
for sub in tutor.prefer_subs.all:
	{{sub.level}}
	{{sub.name}}
	{{sub.rank}} 
	{{sub.other}} # bool 变量，可以判断是否是other
```

```python
# 代码段2
for sub in tutor.refer_subs.all:
	{{sub.level}}
	{{sub.name}}
	{{sub.score}}
	{{sub.rank}}
	{{sub.other}} # bool 变量，可以判断是否是other
```

