from datetime import date
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from.models import CreateAssignment, SubmitAssignment
# Create your views here.


@login_required
def index(request):
    ass_list = CreateAssignment.objects.filter().order_by('-id')
    today_date = date.today()
    return render(request, 'app/index.html', {'ass_list': ass_list, 'today_date': today_date})


@login_required
def detail(request, pk):
    current_user = request.user
    assignment = CreateAssignment.objects.get(pk=pk)
    if request.POST or request.FILES:
        file = request.FILES['file']
        description = request.POST.get('description')
        submit_assignment = SubmitAssignment()
        assignment.submit_status = True
        assignment.save()
        submit_assignment.assignment = assignment
        submit_assignment.description = description
        submit_assignment.file = file
        submit_assignment.submit_by = current_user
        submit_assignment.submit_date = date.today()
        submit_assignment.save()

        ass_list = CreateAssignment.objects.filter().order_by('-id')
        today_date = date.today()
        return render(request, 'app/index.html', {'ass_list': ass_list, 'today_date': today_date})

    else:
        today_date = date.today()
        return render(request, 'app/detail.html', {'assignment': assignment, 'today_date': today_date})
