from django.db import models

# Create your models here.

class TodayCard(models.Model):

    class checkState(models.IntegerChoices):
        ing_check = 0 # 审核中
        ed_check = 1 # 审核完成

    # tcid = models.CharField(max_length=20) # pk
    carrddate = models.DateField()
    type = models.CharField(max_length=10)
    title = models.CharField(max_length=20)
    text = models.CharField(max_length=64)
    text_author = models.CharField(max_length=20)
    picture = models.ImageField(upload_to = 'media/todayCard/img/')
    dzcount = models.IntegerField()
    collectcount = models.IntegerField()
    commentcount = models.IntegerField()
    state = models.IntegerField(choices=checkState.choices) # 从0和1中选择

    # 迭代器
    def __iter__(self):
        return [ 
            str(self.carrddate),
            str(self.type),
            str(self.title),
            str(self.text),
            str(self.text_author),
            str(self.picture),
            str(self.dzcount),
            str(self.collectcount),
            str(self.commentcount),
            str(self.state)
        ]

class QnjrCard(models.Model):
    # qcid = models.CharField(max_length=20) # pk
    craddate = models.DateField() # 日期
    text = models.CharField(max_length = 64) # 内容
    picture = models.ImageField(upload_to = 'media/qnjrCard/img/') # 图片
    state = models.IntegerField() # 状态
