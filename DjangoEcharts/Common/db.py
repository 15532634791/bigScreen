from django.db import models


class BaseModel(models.Model):
    """
    抽象的模型类：定义一些公共的模型字段
    """
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    is_delete = models.BooleanField(default=False, verbose_name="删除标记")

    class Meta:
        abstract = True     # 声明这是一个抽象的模型，在执行迁移文件时，不会在数据中生成表
        verbose_name_plural = "公共字段"
        db_table = "BaseTable"


"""
在 Django 中，abstract = True 是 Model 中一个特殊的字段参数，
在声明一个 Model 类时使用。它用于指定当前 Model 类是否为抽象类。

抽象类是一个不可以实例化的 Model 类，它通常是用来为其它 Model 类提供公共的属性和方法。
当一个 Model 类声明为抽象类时，它将不能用来创建数据库表，
而只能被其它 Model 类继承使用。

具体来说，如果一个 Model 类中设置 abstract=True，则该类将不会被映射到数据库中，
也不会在数据库中创建对应的表。相反，它定义了一个基础类，
可以被其他具体的 Model 类继承，并且这些子类会从父类继承一些共同的字段和方法，
以便减少代码重复和提高代码的复用性。

"""
