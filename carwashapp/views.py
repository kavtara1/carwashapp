from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from carwashapp.models import Branches, CompanyName, Employee


def branch_listing(request):
    branches = Branches.objects.all()
    return render(request, "home.html", context={
        "branches": branches
    })


def branch_detail_view(request, pk):
    branch = get_object_or_404(Branches, pk=pk)
    emp = branch.branch_employees.all()
    return render(request, "detail.html", context={
        "branch": branch,
        "emp": emp

    })


