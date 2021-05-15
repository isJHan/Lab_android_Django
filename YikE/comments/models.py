from django.db import models
from django.db.models.deletion import CASCADE
from todayCard.models import TodayCard
from accounts.models import user
# Create your models here.
class comment(models.Model):
    tcid = models.ForeignKey(TodayCard, on_delete=CASCADE)
    ctext = models.CharField(max_length=50)
    uid = models.ForeignKey(user, on_delete=CASCADE)