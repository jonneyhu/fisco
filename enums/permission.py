# !/usr/bin/python
# -*- coding:utf-8 -*-

# 权限
PERMISSION_TYPE_ORGANIZATION_MANAGEMENT = 'B01000000'  # 组织管理
PERMISSION_TYPE_USER_MANAGEMENT = 'B01010000'  # 用户管理
PERMISSION_TYPE_ROLE_MANAGEMENT = 'B01020000'  # 角色管理


# 其他
PERMISSION_TYPE_SYSTEM_OTHER_MANAGEMENT = 'B900000000'  # 其他
PERMISSION_TYPE_SYSTEM_DOCKING_MANAGEMENT = 'B901000000'  # 获取接入安全信息

# 所有权限
ALL_PERMISSION_TYPE_LIST = [
    PERMISSION_TYPE_ORGANIZATION_MANAGEMENT,
    PERMISSION_TYPE_USER_MANAGEMENT,
    PERMISSION_TYPE_ROLE_MANAGEMENT,

    PERMISSION_TYPE_SYSTEM_OTHER_MANAGEMENT,
    PERMISSION_TYPE_SYSTEM_DOCKING_MANAGEMENT
]

ALL_PERMISSION_TYPE_DICT = {
    PERMISSION_TYPE_ORGANIZATION_MANAGEMENT: '组织管理',
    PERMISSION_TYPE_USER_MANAGEMENT: '用户管理',
    PERMISSION_TYPE_ROLE_MANAGEMENT: '角色管理',

    PERMISSION_TYPE_SYSTEM_OTHER_MANAGEMENT: '其他',
    PERMISSION_TYPE_SYSTEM_DOCKING_MANAGEMENT: '获取安全接入信息'
}

# 可供分配的用户权限
ALL_BACKOFFICE_ASSIGNABLE_PERMISSION_TYPE_DICT = {
    PERMISSION_TYPE_ORGANIZATION_MANAGEMENT: [
        PERMISSION_TYPE_USER_MANAGEMENT,
        PERMISSION_TYPE_ROLE_MANAGEMENT,
    ],



    PERMISSION_TYPE_SYSTEM_OTHER_MANAGEMENT: [
        PERMISSION_TYPE_SYSTEM_DOCKING_MANAGEMENT
    ]
}
