from django.db import models

# Create your models here.
class GGJC_question(models.Model):
    id = models.AutoField(primary_key=True)
    question_title = models.CharField(max_length=225,null=False)
    q_count = models.CharField(max_length=20,null=True)
    answer = models.CharField(max_length=225,null=False)
    where = models.CharField(max_length=128,null=True,blank='')
    page = models.CharField(max_length=128,null=True,blank='')


    def __str__(self):
        return "question_title:{}".format(self.question_title)
    class Meta:
        ordering=['id']
        verbose_name_plural='公共基础知识题库'


class JTGC_question(models.Model):
    id = models.AutoField(primary_key=True)
    question_title = models.CharField(max_length=225,null=False)
    q_count = models.CharField(max_length=20,null=True)
    answer = models.CharField(max_length=225,null=False)
    where = models.CharField(max_length=128,null=True,blank='')
    page = models.CharField(max_length=128,null=True,blank='')


    def __str__(self):
        return "question_title:{}".format(self.question_title)
    class Meta:
        ordering=['id']
        verbose_name_plural='交通工程题库'


class Document(models.Model):
    type = models.CharField(max_length=50,null=False)
    content = models.TextField(null=False)

    def __str__(self):
        return "类型:{}".format(self.type)
    class Meta:
        ordering=['type']
        verbose_name_plural='说明文档'