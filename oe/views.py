from django.contrib.auth.models import User
from django.views.generic import ListView
from django.shortcuts import render

# Create your views here.


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

            if request.POST['password'] == request.POST['repeated-password']:

                password = request.POST['password']

                user = User.objects.create_user(username, username, password)
                user.save()

            return render(request, "success.html")

        except Exception as e:
            print(e)

    return render(request, 'create.html')


def dashboard(request):
    return render(request, 'dashboard.html', {
        'title': 'Inicio'
    })
