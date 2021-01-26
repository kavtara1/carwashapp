from django.shortcuts import render
from carwashapp.models import Branches, CompanyName


def branch_listing(request):
    company = CompanyName.objects.all()
    branches = Branches.objects.select_related("employee")
    return render(request, "home.html", context={
        "branches": branches,
        "company": company
    })


