from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from studentorg.models import Organization, OrgMember, Student, College, Program
from studentorg.forms import OrganizationForm, OrgMemberForm, StudentForm, CollegeForm, ProgramForm
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from typing import Any
from django.db.models.query import QuerySet
from django.db.models import Q
from django.db import connection
from django.http import JsonResponse
from django.db.models.functions import ExtractMonth
from django.db.models import Count, Avg
from datetime import datetime

@method_decorator(login_required, name='dispatch')
class HomePageView(ListView):
    model = Organization
    context_object_name = 'home'
    template_name = "home.html"

class OrganizationList(ListView):
    model = Organization
    context_object_name = 'organization'
    template_name = 'org_list.html'
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
        qa = super(OrganizationList, self).get_queryset(*args, **kwargs)
        if self.request.GET.get("q") !=None:
            query = self.request.GET.get('q')
            qa = qa.filter(Q(name__icontains=query) | 
                           Q(description__icontains=query) | 
                           Q(college__college_name__icontains=query))
        return qa

class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_add.html'
    success_url = reverse_lazy('organization-list')

class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_edit.html'
    success_url = reverse_lazy('organization-list')

class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = 'org_del.html'
    success_url = reverse_lazy('organization-list')

class OrgMemberList(ListView):
    model = OrgMember
    context_object_name = 'orgmember'
    template_name = 'orgmember_list.html'
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
        qa = super(OrgMemberList, self).get_queryset(*args, **kwargs)
        if self.request.GET.get("q"):
            query = self.request.GET.get('q')
            qa = qa.filter(Q(student__firstname__icontains=query) | 
                           Q(student__lastname__icontains=query) | 
                           Q(student__middlename__icontains=query) | 
                           Q(student__program__prog_name__icontains=query) | 
                           Q(organization__name__icontains=query) |
                           Q(date_joined__icontains=query))

        return qa
    
class OrgMemberCreateView(CreateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'orgmember_add.html'
    success_url = reverse_lazy('orgmember-list')

class OrgMemberUpdateView(UpdateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'orgmember_edit.html'
    success_url = reverse_lazy('orgmember-list')

class OrgMemberDeleteView(DeleteView):
    model = OrgMember
    template_name = 'orgmember_del.html'
    success_url = reverse_lazy('orgmember-list')

class StudentList (ListView):
    model = Student
    context_object_name = 'student'
    template_name = 'student_list.html'
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
        qa = super(StudentList, self).get_queryset(*args, **kwargs)
        if self.request.GET.get("q") !=None:
            query = self.request.GET.get('q')
            qa = qa.filter(Q(student_id__icontains=query) | 
                           Q(firstname__icontains=query) | 
                           Q(lastname__icontains=query) | 
                           Q(middlename__icontains=query) | 
                           Q(program__prog_name__icontains=query))
        return qa

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_add.html'
    success_url = reverse_lazy('student-list')

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_edit.html'
    success_url = reverse_lazy('student-list')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_del.html'
    success_url = reverse_lazy('student-list')

class CollegeList(ListView):
    model = College
    context_object_name = 'college'
    template_name = 'college_list.html'
    paginate_by = 5

    
    def get_queryset(self, *args, **kwargs):
        qa = super(CollegeList, self).get_queryset(*args, **kwargs)
        if self.request.GET.get("q") !=None:
            query = self.request.GET.get('q')
            qa = qa.filter(Q(college_name__icontains=query))
        return qa


class CollegeCreateView(CreateView):
    model = College
    form_class = CollegeForm
    template_name = 'college_add.html'
    success_url = reverse_lazy('college-list')

class CollegeUpdateView(UpdateView):
    model = College
    form_class = CollegeForm
    template_name = 'college_edit.html'
    success_url = reverse_lazy('college-list')

class CollegeDeleteView(DeleteView):
    model = College
    template_name = 'college_del.html'
    success_url = reverse_lazy('college-list')

class ProgramList(ListView):
    model = Program
    context_object_name = 'program'
    template_name = 'program_list.html'
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
        qa = super(ProgramList, self).get_queryset(*args, **kwargs)
        if self.request.GET.get("q") !=None:
            query = self.request.GET.get('q')
            qa = qa.filter(Q(college__college_name__icontains=query) | 
                           Q(prog_name__icontains=query))
        return qa

class ProgramCreateView(CreateView):
    model = Program
    form_class = ProgramForm
    template_name = 'program_add.html'
    success_url = reverse_lazy('program-list')

class ProgramUpdateView(UpdateView):
    model = Program
    form_class = ProgramForm
    template_name = 'program_edit.html'
    success_url = reverse_lazy('program-list')

class ProgramDeleteView(DeleteView):
    model = Program
    template_name = 'program_del.html'
    success_url = reverse_lazy('program-list')

class ChartView(ListView):
    template_name = 'chart.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self, *args, **kwargs):
        pass

def LineCountbyMonth2024(request):
    data = (
        OrgMember.objects.filter(date_joined__year=2024)
        .annotate(month=ExtractMonth('date_joined'))
        .values('month')
        .annotate(count=Count('id'))
        .order_by('month')
    )

    activity_data = {item['month']: item['count'] for item in data}

    all_months = range(1, 13) 
    complete_data = {month: activity_data.get(month, 0) for month in all_months}

    chart_data = {
        'labels': [datetime(2024, month, 1).strftime('%b') for month in complete_data.keys()],
        'series': [[count for count in complete_data.values()]],
    }

    return JsonResponse(chart_data)


def PieStudentCountbyOrg(request):
    data = (
        Student.objects.values('program__prog_name')
        .annotate(count=Count('id'))
        .order_by('-count')
    )

    chart_data = {
        'labels': [item['program__prog_name'] for item in data],
        'series': [item['count'] for item in data],
    }

    return JsonResponse(chart_data)

def HorOrgCountByCollege(request):
    data = (
        Organization.objects.values('college__college_name')
        .annotate(count=Count('id'))
        .order_by('-count')
    )

    chart_data = {
        'labels': [item['college__college_name'] for item in data],
        'series': [item['count'] for item in data],
    }

    return JsonResponse(chart_data)

def program_frequency_chart(request):
    college_program_count = College.objects.annotate(num_programs=Count('program'))

    colleges = [college.college_name for college in college_program_count]
    program_counts = [college.num_programs for college in college_program_count]

    data = {
        'colleges': colleges,
        'program_counts': program_counts,
    }
    
    return JsonResponse(data)

def student_enrollment_by_year(request):
    students_by_year = Student.objects.annotate(enrollment_year=Count('student_id'))

    years = set([student.student_id[:4] for student in students_by_year]) 
    year_counts = {year: 0 for year in years}

    for student in students_by_year:
        year = student.student_id[:4]
        year_counts[year] += 1

    data = {
        'years': list(year_counts.keys()), 
        'student_counts': list(year_counts.values()),
    }

    return JsonResponse(data)