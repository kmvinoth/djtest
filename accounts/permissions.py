from rolepermissions.permissions import register_object_checker
from djtest.roles import Father, Mother, Son, Daughter


@register_object_checker()
def access_office(role, user, home_obj):
    if role == Father:
        return True


@register_object_checker()
def access_kitchen(role, user, home_obj):
    if role == Mother:
        return True


@register_object_checker()
def access_playground(role, user, home_obj):
    if role == Son:
        return True


@register_object_checker()
def access_dance_room(role, user, home_obj):
    if role == Daughter:
        return True

