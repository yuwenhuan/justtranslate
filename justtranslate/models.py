from django.db import models

class Article(models.Model):
    article_name = models.CharField(max_length=200)

class Sentence(models.Model):
    article = models.ForeignKey(Article)
    num = models.PositiveIntegerField()
    pnum = models.PositiveIntegerField() # paragraph number
    sentence = models.TextField()

class Translation(models.Model):
    sentence = models.ForeignKey(Sentence)
    translation = models.TextField()
    rating = models.PositiveIntegerField(default=0)