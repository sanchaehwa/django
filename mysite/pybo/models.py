from django.db import models
from django.contrib.auth.models import User
class Question(models.Model):
    #계정이 삭제되면 계정에 따른 글도 삭제
    subject = models.CharField(max_length=200) #글자수제한이 있는건 charField
    content = models.TextField()
    create_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions')


    def __str__(self):
        return self.subject #id 값대신 제목 표시
class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()








