from django.db import models

# 웹사이트 본문에 해당하는 DB모델
# Create your models here.
class MainContent(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    pub_date=models.DateTimeField('date published')