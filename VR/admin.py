from django.contrib import admin
from .models import Curso, Aula, Reserva, Gafa
# Register your models here.

class CursoAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'clase')
class AulaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'num_gafas', 'aforo')
class ReservaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'num_personas', 'num_gafas', 'get_aula', 'fecha_hora', 'incio_hora', 'final_hora')
	def get_aula(self, obj):
		return obj.aula.nombre
class GafaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'get_aula')
	def get_aula(self, obj):
		return obj.aula.nombre

admin.site.register(Curso, CursoAdmin)
admin.site.register(Aula, AulaAdmin)
admin.site.register(Reserva, ReservaAdmin)
admin.site.register(Gafa, GafaAdmin)
