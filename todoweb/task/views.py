from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Alltask


def Home(request):
    myproject = 'เตรียมตัวไปต่างประเทศ'

    # projectlist = ['ศึกษาเรื่องการเงิน','ศึกษาเรื่องการเขียนโปรแกรม','ฝึกเขียนเวปไซค์','ซื้อรถใหม่']
    projectlist = Project.objects.all()
    # ใน projectlist เป็น Query set จะหาค่าข้างในต้องแตกออกมาก่อน
    for pj in projectlist:
        task_in_pj = Alltask.objects.filter(project=pj)
        # ทำให้เป็น dict โดยการ add ทีละตัว
        pj.alltask = task_in_pj
        # print(pj.alltask)

    context = {'myproject': myproject, 'projectlist': projectlist}
    return render(request, 'home.html', context)


def Contact(request):
    return HttpResponse('<h1>TEL : 080-244-5777</h1>')
