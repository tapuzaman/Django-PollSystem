from django.db import models

# Create your models here.
#how question model will work
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

#how question model will work
    class Answer(models.Model):
#making the relation with the question model using foreign key
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)