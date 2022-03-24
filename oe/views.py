from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.


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
