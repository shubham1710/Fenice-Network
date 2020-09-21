from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def login(request):
    return render(request, 'users/login.html')


@login_required
def account(request):
    context = {
        'account_page': "active",
    }
    return render(request, 'users/account.html', context)
