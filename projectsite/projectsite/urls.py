"""
URL configuration for projectsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from studentorg.views import HomePageView, OrganizationList, OrganizationCreateView, OrganizationUpdateView, OrganizationDeleteView, OrgMemberList, OrgMemberCreateView, OrgMemberUpdateView, OrgMemberDeleteView, StudentList, StudentCreateView, StudentUpdateView, StudentDeleteView, CollegeList, CollegeCreateView, CollegeUpdateView, CollegeDeleteView, ProgramList, ProgramCreateView, ProgramUpdateView, ProgramDeleteView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.HomePageView.as_view(), name='home'),
    path('organization_list', OrganizationList.as_view(), name='organization-list'),
    path('organization_list/add', OrganizationCreateView.as_view(), name='organization-add'),
    path('organization_list/<pk>', OrganizationUpdateView.as_view(), name='organization-322 update'),
    path('organization_list/<pk>/delete', OrganizationDeleteView.as_view(), name='organization-391 delete'),
    re_path(r'^login/$', auth_views.LoginView.as_view(
      template name='login.html'), name='login'),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(), name='logout')
    path('orgmember_list', OrgMemberList.as_view(), name='orgmember-list'),
    path('orgmember_list/add', OrgMemberCreateView.as_view(), name='orgmember-add'),
    path('orgmember_list/<pk>/edit/', OrgMemberUpdateView.as_view(), name='orgmember-edit'),
    path('orgmember_list/<pk>/delete', OrgMemberDeleteView.as_view(), name='orgmember-delete'),
    re_path(r'^login/$', auth_views.LoginView.as_view(
      template name='login.html'), name='login'),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(), name='logout')
    path('student_list', StudentList.as_view(), name='student-list'),
    path('student_list/add', StudentCreateView.as_view(), name='student-add'),
    path('student_list/<pk>/edit/', StudentUpdateView.as_view(), name='student-edit'),
    path('student_list/<pk>/delete', StudentDeleteView.as_view(), name='student-delete'),
    re_path(r'^login/$', auth_views.LoginView.as_view(
      template name='login.html'), name='login'),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(), name='logout')
    path('college_list', CollegeList.as_view(), name='college-list'),
    path('college_list/add', CollegeCreateView.as_view(), name='college-add'),
    path('college_list/<pk>/edit/', CollegeUpdateView.as_view(), name='college-edit'),
    path('college_list/<pk>/delete', CollegeDeleteView.as_view(), name='college-delete'),
    re_path(r'^login/$', auth_views.LoginView.as_view(
      template name='login.html'), name='login'),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(), name='logout')
    path('program_list', ProgramList.as_view(), name='program-list'),
    path('program_list/add', ProgramCreateView.as_view(), name="program-add"),
    path('program_list/<pk>/edit/', ProgramUpdateView.as_view(), name="program-edit"),
    path('program_list/<pk>/delete', ProgramDeleteView.as_view(), name="program-delete"),
    re_path(r'^login/$', auth_views.LoginView.as_view(
      template name='login.html'), name='login'),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(), name='logout')
]
