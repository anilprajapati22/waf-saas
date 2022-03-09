from django.db import models

# Create your models here.


class sgn(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
class iptableRules(models.Model):
    project_name = models.CharField(max_length=200)
    rule = models.CharField(max_length=200)
    ipaddr = models.CharField(max_length=200)

class wafdetails(models.Model):
    container_id =  models.CharField(max_length=200)
    container_name = models.CharField(max_length=200)
    container_port = models.CharField(max_length=200)
    container_ip = models.CharField(max_length=200)
    public_ip = models.CharField(max_length=200)
    project_name = models.CharField(max_length=200)

class ons(models.Model):
    question = models.ForeignKey(sgn, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)