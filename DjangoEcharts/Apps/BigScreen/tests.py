from django.test import TestCase

# Create your tests here.

"""

使用django orm如何实现这种效果， cursor.executemany 快速插入数据，使用事务的方式,不重复插入数据 目的是为了快速插入数据
from django.db import transaction
from myapp.models import MyModel

# 多条记录数据
data = [
    {'column1': 'value1', 'column2': 'value2'},
    {'column1': 'value3', 'column2': 'value4'},
    {'column1': 'value5', 'column2': 'value6'}
]

try:
    # 开始事务
    with transaction.atomic():
        # 使用bulk_create()方法批量插入多条记录
        MyModel.objects.bulk_create([MyModel(**item) for item in data], ignore_conflicts=True)
except Exception as e:
    print(f"插入失败: {str(e)}")


使用pymysql执行多条记录， cursor.executemany 快速插入数据，使用事务的方式,不重复插入数据

如果你想要使用pymysql执行多条记录的插入操作，并且在执行过程中避免重复插入数据，可以结合使用INSERT IGNORE语句和cursor.executemany()方法来实现。

下面是一个示例代码，演示如何使用pymysql执行多条记录的插入操作，并在插入过程中避免重复插入数据：

python
import pymysql

# 建立与数据库的连接
conn = pymysql.connect(
    host='localhost',
    user='username',
    password='password',
    database='database_name'
)

# 创建游标对象
cursor = conn.cursor()

try:
    # 开始事务
    conn.begin()

    # SQL插入语句
    sql = "INSERT IGNORE INTO table_name (column1, column2) VALUES (%s, %s)"

    # 多条记录数据
    data = [
        ('value1', 'value2'),
        ('value3', 'value4'),
        ('value5', 'value6')
    ]

    # 执行多条记录插入
    cursor.executemany(sql, data)

    # 提交事务
    conn.commit()

    print("插入成功")
except Exception as e:
    # 发生错误时回滚事务
    conn.rollback()
    print(f"插入失败: {str(e)}")
finally:
    # 关闭游标和连接
    cursor.close()
    conn.close()
在这个示例代码中，我们使用了INSERT IGNORE语句来执行插入操作。它会尝试将数据插入到表中，但如果插入的记录与表中的现有记录重复，它会忽略这些重复的记录，不会引发错误。

请注意，你需要根据你的实际情况修改主机名、用户名、密码、数据库名、表名、列名和要插入的数据。

希望这个示例代码对你有所帮助！
"""
