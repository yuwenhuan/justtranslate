from django.db import models

class Sentence(models.Model):
    article_name = models.CharField(max_length=200)
	num = models.PositiveIntegerField()
	pnum = models.PositiveIntegerField() # paragraph number
	sentence = models.CharField()
	author = models.ForeignKey(User, blank=True, null=True)
