from rolepermissions.roles import AbstractUserRole


class SysAdmin(AbstractUserRole):
    available_permissions = {'Assign_role_users': True}


class Father(AbstractUserRole):
    available_permissions = {'Work': True, 'Manage_Expenses': True}


class Mother(AbstractUserRole):
    available_permissions = {'Cook': True, 'Take_care_kids': True, 'Shopping': True}


class Son(AbstractUserRole):
    available_permissions = {'Study': True, 'Work_partime': True, 'Play': True}


class Daughter(AbstractUserRole):
    available_permissions = {'Study': True, 'Go_to_dance_class': True, 'Play': True}

