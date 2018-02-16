from django.contrib.auth.models import UserManager as AbstractUserManager
from django.db import models


class UserManager(AbstractUserManager):
    def by_username(self, username):
        return self.all().filter(username=username).first()


class QuestionManager(models.Manager):
    def hottest(self):
        return self.all().order_by('rate')

    def newest(self):
        return self.all().order_by('date').reverse()

    def by_id(self, qid):
        return self.all().filter(id=qid)

    # def by_username(self, uid):
    #     return self.all().filter(author=uid)


class TagManager(models.Manager):
    def by_tag(self, tag_str):
        return self.filter(title=tag_str).first().questions.all().order_by('date').reverse()
