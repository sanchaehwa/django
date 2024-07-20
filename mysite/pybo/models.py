from django.db import models
class Question(models.Model):
    subject = models.CharField(max_length=200) #글자수제한이 있는건 charField
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject #id 값대신 제목 표시
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()








