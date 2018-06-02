from django.contrib import admin
from basket.models import Team, Player, Coach
from django.utils.safestring import mark_safe


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
	list_display = ('name','description','thumb','code')
	list_filter = ('name','description','logo','code',)
	search_fields = ['name','description','logo','code',]
	
	def thumb(self, obj):
		return mark_safe(u'<img src="%s" style="width:10px;height:10px;"/>' \
			% (obj.picture.url))

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
	list_display = ('name','nickname','birthday','age','rut','email','height','weight','thumb','position')
	list_filter = ('name','nickname','birthday','age','rut','email','height','weight','picture','position')
	search_fields = ['name','nickname','birthday','age','rut','email','height','weight','picture','position']
	
	def thumb(self, obj):
		return mark_safe(u'<img src="%s" style="width:100px;height:100px;"/>' \
			% (obj.picture.url))

@admin.register(Coach)
class Coach_admin(admin.ModelAdmin):
	list_display = ('name','age','email','rut','nickname','team')
	list_filter = ('name','age','email','rut','nickname','team')
	search_fields = ['name','age','email','rut','nickname','team']

