from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Perfil

class PerfilInline(admin.StackedInline):
    model = Perfil
    can_delete = False
    verbose_name_plural = 'Perfil'

class UserAdmin(BaseUserAdmin):
    inlines = (PerfilInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'get_tipo', 'is_staff')
    list_filter = ('perfil__tipo', 'is_staff', 'is_active')
    
    def get_tipo(self, obj):
        return obj.perfil.get_tipo_display()
    get_tipo.short_description = 'Tipo'

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Perfil)
