from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm

from django.contrib.gis import admin

from .models import User, Area


def update_fieldsets(fieldsets, custom_fielsets):
    new_fieldsets = []
    for key, value in fieldsets:
        if key in custom_fielsets:
            new_value = {'fields': value['fields'] + custom_fielsets[key]['fields']}
            new_fieldsets.append((key, new_value))
        else:
            new_fieldsets.append((key, value))

    return tuple(new_fieldsets)


class ProvidersUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User

class ProvidersUserAdmin(UserAdmin):
    form = ProvidersUserChangeForm
    custom_fielsets = {'Personal info': {'fields': ('phone', 'language', 'currency')}}

    fieldsets = update_fieldsets(UserAdmin.fieldsets, custom_fielsets)


class AreaAdmin(admin.OSMGeoAdmin):
    search_fields = ['name']


admin.site.register(User, ProvidersUserAdmin)
admin.site.register(Area, AreaAdmin)
