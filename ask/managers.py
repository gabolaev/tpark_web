from django.contrib.auth.models import UserManager as AbstractUserManager
from django.db import models
from django.db.models import Sum


class UserManager(AbstractUserManager):
    def by_username(self, username):
        return self.all().filter(username=username).first()


class QuestionManager(models.Manager):
    def hottest(self):
        return self.all().order_by('rate').reverse()

    def newest(self):
        return self.all().order_by('date').reverse()

    def by_id(self, qid):
        return self.all().filter(id=qid)


class AnswerManager(models.Manager):
    def hottest(self):
        return self.all().order_by('rate').reverse()


class TagManager(models.Manager):
    def by_tag(self, tag_str):
        return self.filter(title=tag_str).first().questions.all().order_by('date').reverse()


class LikeManager(models.Manager):
    use_for_related_fields = True

    def likes(self):
        # We take the queryset with records greater than 0
        return self.get_queryset().filter(vote__gt=0)

    def dislikes(self):
        # We take the queryset with records less than 0
        return self.get_queryset().filter(vote__lt=0)

    def sum_rating(self):
        # We take the total rating
        return self.get_queryset().aggregate(Sum('vote')).get('vote__sum') or 0
