from django.db import models

# Create your models here.
class Small(models.Model):
    s1 = models.TextField()
    s2 = models.TextField()

class Cal(models.Model):
    s_id_asdf = models.ForeignKey("Small", related_name="small", on_delete=models.CASCADE, db_column="s_id")
    var1 = models.TextField()
    var2 = models.TextField()
    var3 = models.TextField()