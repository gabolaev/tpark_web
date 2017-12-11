from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager as AbstractUserManager

class UserManager(AbstractUserManager):
    def by_username(self, findUname):
        return self.all().filter(username=findUname)

class QuestionManager(models.Manager):
    def hottest(self):
        return self.all().order_by('rate')

    def newest(self):
        return self.all().order_by('date')

    def by_id(self, qid):
        return self.all().filter(id=qid)


class TagManager(models.Manager):
    def by_tag(self, tag_str):
        return self.filter(title=tag_str).first().questions.all()
