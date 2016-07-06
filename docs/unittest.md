```python
from django.test import TestCase

class WhateverTest(TestCase):
  def test_what_you_want_to_test(self):
    pass
    self.assertEqual(p1,p2)
```
```python
from django.core.urlresolvers import reverse

class QuestionViewTests(TestCase):
    def test_index_view_with_no_questions(self):
        """
        If no questions exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

```