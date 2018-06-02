from django.urls import path
from basket import views

urlpatterns = [
	path('',views.index, name='index'),
	
	path('add_player',views.add_player, name="add_player"),
	path('list_player',views.list_player, name="list_player"),
	path('edit_player/<int:player_id>',views.edit_player, name="edit_player"),
	path('delete_player/<int:player_id>',views.delete_player, name= "delete_player"),

	path('add_team',views.add_team, name= "add_team"),
	path('list_team',views.list_team, name= "list_team"),
	path('edit_team/<int:team_id>',views.edit_team, name= "edit_team"),
	path('delete_team/<int:team_id>',views.delete_team, name= "delete_team"),

	path('add_coach',views.add_coach, name= "add_coach"),
	path('list_coach',views.list_coach, name= "list_coach"),
	path('edit_coach/<int:coach_id>',views.edit_coach, name= "edit_coach"),
	path('delete_coach/<int:coach_id>',views.delete_coach, name= "delete_coach"),

	path('add_nomina',views.add_nomina, name= "add_nomina"),
	path('list_nomina',views.list_nomina, name= "list_nomina"),
	path('edit_nomina/<int:coach_id>',views.edit_nomina, name= "edit_nomina"),
	path('delete_nomina/<int:coach_id>',views.delete_nomina, name= "delete_nomina"),
]