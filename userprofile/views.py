from django.shortcuts import redirect, render,get_object_or_404
from common.models import UserInfo

def home(request):
    users = UserInfo.objects.all()
    return render(request,'home.html',{'users':users})


def search(request):
    users = UserInfo.objects.all().order_by('username')

    q = request.POST.get('q', "") 

    if q:
        variable_column = request.GET.get('fd_name')
        if variable_column=="major":
            users = users.filter(major__icontains=q)
        else :
            users = users.filter(hope_area__icontains=q)

        return render(request, 'search.html', {'users' : users, 'q' : q})
    
    else:
        return redirect(request, home)


def detail(request,id):
    users = get_object_or_404(UserInfo,pk=id)
    return render(request,'detail.html',{'users':users})
