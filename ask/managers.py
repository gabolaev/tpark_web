from django.db import models


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
