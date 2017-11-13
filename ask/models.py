from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    upload = models.ImageField(default="/ask/static/avatars/emptyUser.png", upload_to='uploads/%Y/%m/%d/')
    register_date = models.DateTimeField(default=timezone.now, verbose_name='Время создания профилях')
    rank = models.IntegerField(default=0, verbose_name='rate of user')

    def __str__(self):
        return self.username


class Tag(models.Model):
    title = models.CharField(max_length=50, verbose_name='Тэг')

class Question(models.Model):
    author = models.ForeignKey(User, null=False, verbose_name='Автор вопроса')
    date = models.DateTimeField(default=timezone.now, verbose_name='Время создания вопроса')

    is_active = models.BooleanField(default=True, verbose_name='Доступность вопроса')
    title = models.CharField(max_length=70, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Полный текст вопроса')

    tags = models.ManyToManyField(Tag, blank=True, verbose_name='Тэги')
    rate = models.IntegerField(default=0, null=False, verbose_name='Рейтинг')

    def __str__(self):
        return self.text

class Answer(models.Model):
    author = models.ForeignKey(User, null=False, verbose_name='Автор ответа')
    date = models.DateTimeField(default=timezone.now, verbose_name='Время ответа')

    question = models.ForeignKey(Question, verbose_name='Вопрос, на который выполняется ответ')
    text = models.TextField(verbose_name='Полный текст вопроса')
    rate = models.IntegerField(default=0, null=False, verbose_name='Рейтинг')

    def __str__(self):
        return self.text


class Like(models.Model):
    from_user = models.ForeignKey(User, null=False, verbose_name='Автор лайка')
    is_like = models.BooleanField(blank=True, default=True, verbose_name='Лайк')
    # objects = LikeManager()

    def __str__(self):
        return "Лайк пользователя " + self.from_user.username



class QuestionLike(Like):
    question = models.ForeignKey(Question, null=False, verbose_name="вопрос")

    def __str__(self):
        return "Лайк от " + self.from_user.username + " под вопросом: " + self.question.title


class AnswerLike(Like):
    answer = models.ForeignKey(Answer, null=False, verbose_name="ответ")

    def __str__(self):
        return "Лайк от " + self.from_user.username + " под ответом:  " + self.answer.text
