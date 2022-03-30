import django.contrib.auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

# Create your views here.
from oe.forms import UserForm, CareerForm, StudentForm
from oe.models import Career, Student


def login(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])

        if user is not None:
            django.contrib.auth.login(request, user)
            return HttpResponseRedirect(reverse_lazy('dashboard'))

    return render(request, 'login.html')


class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'users/read.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de usuarios'

        return context


class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('list_users')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear usuarios'

        return context


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name_suffix = '_update_form'
    template_name = 'users/update.html'
    success_url = reverse_lazy('list_users')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar usuarios'

        return context


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('list_users')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar usuarios'

        return context


class CareerListView(ListView):
    model = Career
    template_name = 'careers/read.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de usuarios'

        return context


class CareerCreateView(CreateView):
    model = Career
    form_class = CareerForm
    template_name = 'careers/create.html'
    success_url = reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear usuarios'

        return context


class CareerUpdateView(LoginRequiredMixin, UpdateView):
    model = Career
    form_class = CareerForm
    template_name_suffix = '_update_form'
    template_name = 'careers/update.html'
    success_url = reverse_lazy('list_careers')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar carreras'

        return context


class CareerDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'careers/delete.html'
    success_url = reverse_lazy('list_careers')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar carreras'

        return context


class StudentListView(ListView):
    model = Student
    template_name = 'students/read.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de estudiantes'

        return context


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/create.html'
    success_url = reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear estudiantes'

        return context


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    form_class = CareerForm
    template_name_suffix = '_update_form'
    template_name = 'students/update.html'
    success_url = reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar estudiantes'

        return context


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    template_name = 'students/delete.html'
    success_url = reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar estudiantes'

        return context


@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {
        'title': 'Inicio'
    })


@login_required
def logout(request):
    django.contrib.auth.logout(request)

    return HttpResponseRedirect(reverse_lazy('login'))
