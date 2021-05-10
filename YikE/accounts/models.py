from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.

class myUser(models.Model):
    """ User 内置:

            username：用户名
    
            email: 电子邮件

            password：密码

            first_name：名

            last_name：姓

            is_active: 是否为活跃用户。默认是True

            is_staff: 是否为员工。默认是False

            is_superuser: 是否为管理员。默认是False

            date_joined: 加入日期。系统自动生成。
    """
    # 账号, 关联自带User表
    uid = models.OneToOneField(User, on_delete=CASCADE)
    
    # 用户名继承自username
    username = models.CharField(max_length=10)

    # 收藏卡片id, 外键
    collectID = models.ForeignKey() 

    # 投稿卡片id, 外键
    contributeID = models.ForeignKey()

    # 头像
    photo = models.ImageField('static/img/photoes/')
