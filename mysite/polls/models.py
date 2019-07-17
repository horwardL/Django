import datetime

from django.db import models
from django.utils import timezone

# python manage.py makemigrations polls
# telling Django that you've made some changes to your models
# can also do 'py manage.py sqlmigrate polls 0001' to see the SQL
# finally 'python manage.py migrate' to create these model tables in your db


# Create your models here.
# create a database (table, columns, ...)
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    # 'choice'_set is default name for this inverse relationship
    # can change with kwarg 'related_name'
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
