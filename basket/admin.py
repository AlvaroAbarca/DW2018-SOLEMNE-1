from django.contrib import admin
from basket.models import Team, Player, Coach
from django.utils.safestring import mark_safe


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
	list_display = ('name','description','_thumbnail','code')
	list_filter = ('name','description','logo','code',)
	search_fields = ['name','description','logo','code',]
	def _thumbnail(self, obj):
		if obj.log:
			return mark_safe(u'<img src="/media/%s" alt="" width="50" height="50" />' % (obj.log))
		else:
			return "[No Image]"

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
	list_display = ('name','nickname','birthday','age','rut','email','height','weight','_thumbnail','position')
	list_filter = ('name','nickname','birthday','age','rut','email','height','weight','picture','position')
	search_fields = ['name','nickname','birthday','age','rut','email','height','weight','picture','position']
	def _thumbnail(self, obj):
		if obj.photo:
			return mark_safe(u'<img src="/media/%s" alt="" width="50" height="50"/>' % (obj.photo))
		else:
			return "[No Image]"

@admin.register(Coach)
class Coach_admin(admin.ModelAdmin):
	list_display = ('name','age','email','rut','nickname','team')
	list_filter = ('name','age','email','rut','nickname','team')
	search_fields = ['name','age','email','rut','nickname','team']

