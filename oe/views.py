from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView


# Create your views here.


def login(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])

        if user is not None:
            return HttpResponseRedirect(reverse_lazy('dashboard'))

    return render(request, 'login.html')


# No backend authenticated the credentials


class UserListView(ListView):
    model = User
    template_name = 'users.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de usuarios'

        return context


def create_user(request):
    if request.method == 'POST':
        try:
            username = request.POST['email']
            name = request.POST['name']
            last_name = request.POST['last-name']

            if request.POST['password'] == request.POST['repeated-password']:
                password = request.POST['password']

                user = User.objects.create_user(username, username, password)
                user.last_name = last_name
                user.name = name
                user.save()

            return render(request, "success.html")

        except Exception as e:
            print(e)

    return render(request, 'create.html')


class UserUpdateView(UpdateView):
    model = User
    template_name = 'users.html'


class UserDeleteView(DeleteView):
    model = User
    template_name = 'users.html'


def dashboard(request):
    return render(request, 'dashboard.html', {
        'title': 'Inicio'
    })
