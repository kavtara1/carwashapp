from django.shortcuts import render
from carwashapp.models import Branches


def branch_listing(request):
    branches = Branches.objects.select_related("employee")
    return render(request, "home.html", context={
        "branches": branches
    })


