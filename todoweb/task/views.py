from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Alltask


def Home(request):
    myproject = 'เตรียมตัวไปต่างประเทศ'

    # projectlist = ['ศึกษาเรื่องการเงิน','ศึกษาเรื่องการเขียนโปรแกรม','ฝึกเขียนเวปไซค์','ซื้อรถใหม่']
    projectlist = Project.objects.all().order_by('id').reverse()
    # ใน projectlist เป็น Query set จะหาค่าข้างในต้องแตกออกมาก่อน
    for pj in projectlist:
        task_in_pj = Alltask.objects.filter(project=pj)
        # ทำให้เป็น dict โดยการ add ทีละตัว
        pj.alltask = task_in_pj
        # เช็ค pj.alltask
        # print(pj.alltask)

    context = {'myproject': myproject, 'projectlist': projectlist}
    return render(request, 'home.html', context)


def Contact(request):
    return HttpResponse('<h1>TEL : 080-244-5777</h1>')


def About(request):
    return render(request, 'about.html')


def Addproject(request):
    context = {}
    if request.method == "POST":
        data = request.POST.copy()
        # print('DATA', data)
        project_name = data.get('project_name')
        project_desc = data.get('project_desc')

        newprofect = Project()
        newprofect.project_name = project_name
        newprofect.project_desc = project_desc
        newprofect.save()
        context['alert'] = 'บันทึกข้อมูลเรียบร้อยแล้ว'

    return render(request, 'addproject.html', context)


def Addtask(request):
    context = {}
    allproject = Project.objects.all()
    context['allproject'] = allproject
    if request.method == "POST":
        data = request.POST.copy()
        # print('DATA', data)
        projectid = data.get('projectid')
        # เอา projectid ใสหาชื่อ project ใน model เพราะ task ผูกค่ากับ project อยู่
        project = Project.objects.get(id=int(projectid))
        task_name = data.get('task_name')
        task_desc = data.get('task_desc')

        newtask = Alltask()
        newtask.project = project
        newtask.task_name = task_name
        newtask.task_desc = task_desc
        newtask.save()
        context['alert'] = 'บันทึกข้อมูลเรียบร้อยแล้ว'

    return render(request, 'addtask.html', context)
