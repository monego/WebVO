from django.contrib import admin
from .models import UsuarioFriends


class UsuarioFriendsAdmin(admin.ModelAdmin):
        fields = ['nickname', 'usuario', 'resultsPerPage']
        list_display = ('nickname',
                        'usuario',
                        'date_register',
                        'last_access',
                        'resultsPerPage')

admin.site.register(UsuarioFriends, UsuarioFriendsAdmin)
