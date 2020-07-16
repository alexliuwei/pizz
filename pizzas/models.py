from django.db import models

# Create your models here.
'''编写一个Pizza的模块来存储披萨的名称'''
class Pizza(models.Model):
    name = models.CharField(max_length=200)#一个文本框变量来接受
    date_added = models.DateTimeField(auto_now_add=True)#获取当前时间

    def __str__(self):
        return self.name#把值返回给函数

class Topping(models.Model):
    pizza = models.ForeignKey(Pizza,on_delete=models.CASCADE)#通过一个外键把披萨的名称取回来
    name = models.TextField()#文本框
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'#显示多条记录

    def __str__(self):
        return self.name