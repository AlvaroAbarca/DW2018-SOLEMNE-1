from django.shortcuts import render, redirect
from basket.models import *
from basket.forms import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/auth/login')
def index(request):
    data = {}
    us = request.user
    #profile = User.objects.get(user = us)
    data['inicio'] = 'Bienvenidos a la plataforma DW-2018'
    #if profile.is_staff :
    template_name = 'index.html'
    #else: 
        #template_name = 'index_coach.html'
    return render(request,template_name,data)

def list_player(request):
    data = {}

    data['inicio'] = 'Lista de Jugadores'

    # SELECT * FROM player
    data['object_list'] = Player.objects.all()
    
    template_name = 'player/list_player.html'
    return render(request, template_name, data)

def add_player(request):
    data = {}
    data['titulo'] = 'Añadir player'
    if request.method == "POST":
        data['form'] = PlayerForm(request.POST, request.FILES)
        if data['form'].is_valid():
            data ['form'].save()
    else:
        data['form'] = PlayerForm()
    template_name = 'add.html'

    return render (request, template_name, data)

def  edit_player(request,player_id):
    data = {}
    template_name = 'add.html'
    data['titulo'] = 'Editar Player'
    instance = Player.objects.get(pk=player_id)
    if request.method == "POST":
        data['form'] = PlayerForm(request.POST, instance = instance)
        if data['form'].is_valid():
            data ['form'].save()
            return redirect('list_player')
    else:
        data['form'] = PlayerForm(instance = instance)
    return render(request,template_name,data)

def delete_player(request,player_id):
    data = {}
    template_name = 'add.html'
    data['titulo'] = 'Eliminar Player'
    instance = Player.objects.get(pk=asignatura_id).delete()   
    #return render(request,template_name,data)
    return redirect('list_player')

def list_team(request):
    data = {}

    data['inicio'] = 'Lista de Team'

    # SELECT * FROM player
    data['object_list'] = Team.objects.all()
    
    template_name = 'team/list_team.html'
    return render(request, template_name, data)

def add_team(request):
    data = {}
    data['titulo'] = 'Añadir team'
    if request.method == "POST":
        data['form'] = TeamForm(request.POST, request.FILES)
        if data['form'].is_valid():
            data ['form'].save()
    else:
        data['form'] = TeamForm()
    template_name = 'add.html'

    return render (request, template_name, data)

def  edit_team(request,team_id):
    data = {}
    template_name = 'add.html'
    data['titulo'] = 'Editar team'
    instance = Team.objects.get(pk=team_id)
    if request.method == "POST":
        data['form'] = TeamForm(request.POST, instance = instance)
        if data['form'].is_valid():
            data ['form'].save()
            return redirect('list_team')
    else:
        data['form'] = TeamForm(instance = instance)
    return render(request,template_name,data)

def delete_team(request,team_id):
    data = {}
    template_name = 'add.html'
    data['titulo'] = 'Eliminar Team'
    instance = Team.objects.get(pk=team_id).delete()   
    #return render(request,template_name,data)
    return redirect('list_team')

def list_coach(request):
    data = {}

    data['inicio'] = 'Lista de Coach'

    # SELECT * FROM player
    data['object_list'] = Coach.objects.all()
    
    template_name = 'coach/list_coach.html'
    return render(request, template_name, data)

def add_coach(request):
    data = {}
    data['titulo'] = 'Añadir Coach'
    if request.method == "POST":
        data['form'] = CoachForm(request.POST)
        if data['form'].is_valid():
            data ['form'].save()
    else:
        data['form'] = CoachForm()
    template_name = 'add.html'

    return render (request, template_name, data)

def  edit_coach(request,coach_id):
    data = {}
    template_name = 'add.html'
    data['titulo'] = 'Editar Coach'
    instance = Coach.objects.get(pk=coach_id)
    if request.method == "POST":
        data['form'] = CoachForm(request.POST, instance = instance)
        if data['form'].is_valid():
            data ['form'].save()
            return redirect('list_coach')
    else:
        data['form'] = CoachForm(instance = instance)
    return render(request,template_name,data)

def delete_coach(request,Coach_id):
    data = {}
    template_name = 'add.html'
    data['titulo'] = 'Eliminar Coach'
    instance = Coach.objects.get(pk=coach_id).delete()   
    #return render(request,template_name,data)
    return redirect('list_coach')

def add_nomina(request):
    data = {}
    data['titulo'] = 'Crear Nomina'
    if request.method == "POST":
        data['form'] = PayrollForm(request.POST)
        if data['form'].is_valid():
            data ['form'].save()
    else:
        data['form'] = PayrollForm()
    template_name = 'add.html'

    return render (request, template_name, data)

def list_nomina(request):
    data = {}

    data['inicio'] = 'Lista Nominas'

    # SELECT * FROM player
    data['object_list'] = Payroll.objects.all()
    
    template_name = 'list_payroll.html'
    return render(request, template_name, data)

def  edit_nomina(request,nomina_id):
    data = {}
    template_name = 'add.html'
    data['titulo'] = 'Editar Coach'
    instance = Payroll.objects.get(pk=nomina_id)
    if request.method == "POST":
        data['form'] = PayrollForm(request.POST, instance = instance)
        if data['form'].is_valid():
            data ['form'].save()
            return redirect('list_nomina')
    else:
        data['form'] = PayrollForm(instance = instance)
    return render(request,template_name,data)

def delete_nomina(request,nomina_id):
    data = {}
    template_name = 'add.html'
    data['titulo'] = 'Eliminar Nomina'
    instance = Payroll.objects.get(pk=nomina_id).delete()   
    #return render(request,template_name,data)
    return redirect('list_nomina')