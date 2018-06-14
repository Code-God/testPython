import django
from django.db import models

# Create your models here.
# 创建自定义manager以定制数据库访问。
# views可以通过Student.objects.select_all()查询全部等。。
class StudentManager(models.Manager):

    def create_student(self, user_name):
        # 方式一
        # student = Student(user_name = user_name)
        # # 保存到数据库
        # student.save()
        # 方式二(推荐)
        student = self.create(user_name=user_name)
        return student

    def select_all(self):
        # 查询全部
        list = self.all()
        return list

    def select_one(self, name):
        # a = []
        # # 查询单条数据
        # student = self.get(id=id)
        # a.append(student)
        # return a
        # 查询匹配条件的多条数据
        # student = self.filter(user_name=user_name)
        # 模糊查询
        student = self.filter(name__contains=user_name)
        # 根据字段内容排序后展示数据，根据字段内容逆向排序后展示数据,加一个负号order_by('-name')
        tt = student.order_by('user_name')

        # 限制数据条数, 相当于mysql limit
        tt1 = self.filter(name__contains=user_name)[0:5]  # [0]显示第一条 [0:2]会显示前两条，切片不支持负数
        return tt1

    def updata_student(self, id, user_name):
        self.get(id=id).update(user_name=user_name)  # update可多条update(name=name, bb="wahaha")


class Student(models.Model):
    # 如果没有models.AutoField，默认会创建一个id的自增列
    id = models.AutoField  #自增列
    role_id = models.CharField(max_length=8) #字符串字段
    user_name = models.CharField(max_length=225)
    password = models.CharField(max_length=225)
    create_Date = models.DateTimeField(auto_now_add=True)

    # model的字符串表现形式
    def __unicode__(self):
        return self.user_name

    objects = StudentManager()

