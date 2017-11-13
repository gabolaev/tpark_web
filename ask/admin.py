from django.contrib import admin
# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

admin.site.register(User, UserAdmin)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Like)
admin.site.register(QuestionLike)
admin.site.register(AnswerLike)
admin.site.register(Tag)
