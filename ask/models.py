from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
from django.utils import timezone

from ask.managers import *


class User(AbstractUser):
    upload = models.ImageField(default="avatars/emptyUser.png", upload_to='uploads/%Y/%m/%d/')
    register_date = models.DateTimeField(default=timezone.now, verbose_name='Profile creation date')
    rank = models.IntegerField(default=0, verbose_name='User rating')

    objects = UserManager()

    def __str__(self):
        return self.username


class Tag(models.Model):
    title = models.CharField(max_length=15, default='404', verbose_name='Tag')

    objects = TagManager()


class Like(models.Model):

    LIKE = 1
    DISLIKE = -1

    VOTE_TYPES = ((LIKE, 'Like'), (DISLIKE, 'Dislike'))

    user = models.ForeignKey(User, null=True, verbose_name='Like author')
    vote = models.SmallIntegerField(verbose_name='is like', default=VOTE_TYPES[0], choices=VOTE_TYPES)

    content_type = models.ForeignKey(ContentType, default=None, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField(default=-1)
    content_object = GenericForeignKey()

    objects = LikeManager()

    def __str__(self):
        return "Like from " + self.user.username
#
#
class Question(models.Model):
    author = models.ForeignKey(User, null=False, db_column="author", verbose_name='Question author')
    date = models.DateTimeField(default=timezone.now, verbose_name='Question date')

    is_active = models.BooleanField(default=True, verbose_name='Question aviability')
    title = models.CharField(max_length=70, verbose_name='Header')
    text = models.TextField(verbose_name='Question full text')

    tags = models.ManyToManyField(Tag, related_name='questions', blank=True, verbose_name='Tags')

    votes = GenericRelation(Like, related_query_name='questions')
    rate = models.IntegerField(default=0, null=False, verbose_name='Rate')

    objects = QuestionManager()

    def __str__(self):
        return self.text


class Answer(models.Model):
    author = models.ForeignKey(User, null=False, verbose_name='Answer author')
    date = models.DateTimeField(default=timezone.now, verbose_name='Answer date')

    question = models.ForeignKey(Question, related_name='answers', verbose_name='Answered question',
                                 on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Answer full text')

    votes = GenericRelation(Like, related_query_name='answers')
    rate = models.IntegerField(default=0, null=False, verbose_name='Rate')

    objects = AnswerManager()

    def __str__(self):
        return self.text

