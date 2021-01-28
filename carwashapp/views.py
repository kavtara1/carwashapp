from django.shortcuts import render, get_object_or_404
from datetime import datetime, timedelta
from carwashapp.models import Branches, CompanyName,  Discount, Orders


def branch_listing(request):
    branches = Branches.objects.all()
    disc = Discount.objects.all()
    name = CompanyName.objects.get()

    return render(request, "home.html", context={
        "branches": branches,
        "disc": disc,
        "name": name
    })


def branch_detail_view(request, pk):
    branch = get_object_or_404(Branches, pk=pk)
    emp = branch.branch_employees.all()

    return render(request, "detail.html", context={
        "branch": branch,
        "emp": emp
    })


def washers_view(request, pk):
    now = datetime.today()
    current_month = now.month
    current_year = now.year
    one_week_ago = datetime.today() - timedelta(days=7)
    order_per_washer_month = Orders.objects.all().filter(washer_id=pk, order_date__month=current_month)
    order_per_washer_week = Orders.objects.all().filter(washer_id=pk, order_date__gte=one_week_ago)
    order_per_washer_year = Orders.objects.all().filter(washer_id=pk, order_date__year=current_year)

    return render(request, "washer.html", context={
        "month": order_per_washer_month,
        "week": order_per_washer_week,
        "year": order_per_washer_year,
    })
