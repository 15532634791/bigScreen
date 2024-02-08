# -*- coding:utf8 -*-
from rest_framework import permissions


class CommonPermissions(permissions.BasePermission):
    """
    1 通用权限认证
    2 管理员可以看到所有数据
    3 自定义权限只允许对象的所有者编辑它。
    """

    def has_object_permission(self, request, view, obj):
        # 读取权限允许任何请求，
        # 所以我们总是允许GET，HEAD或OPTIONS请求。
        if request.user.is_superuser:
            return True

        # 判断是否为用户视图
        if hasattr(view, 'UserUniqueIdent'):

            if str(request.user) == str(obj.username):
                return True
            else:
                return False

        # 只有该所有者才允许写权限。

        return int(obj.created_by_id) == int(request.user.id)


