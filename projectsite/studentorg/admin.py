from django.contrib import admin

from .models import College, Program, Organization, Student, OrgMember

@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ("college",)
    search_fields = ("college")

@admin.register(Program)
class ProgamAdmin(admin.ModelAdmin):
    list_display = ("program", "get_college",)
    search_fields = ("program")

    @admin.display(description="College")
    def get_college(self, obj):
        try:
            college_name = College.objects.get(id=obj.college)
            return college_name.college
        except College.DoesNotExist:
            return None

@admin.register(Organization)
class Organization(admin.ModelAdmin):
    list_display = ("organization", "get_college",)
    search_fields = ("organization")

    @admin.display(description="College")
    def get_college(self, obj):
        try:
            college_name = College.objects.get(id=obj.college)
            return college_name.college
        except College.DoesNotExist:
            return None
    
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_id", "lastname", "firstname", "middlename", "program")
    search_fields = ("lastname", "firstname",)

@admin.register(OrgMember)
class OrgMemberAdmin(admin.ModelAdmin):
    list_display = ("student", "get_member_program", "organization", "date_joined",)
    search_fields = ("student__lastname", "student__firstname",)

    @admin.display(description='Member Program')
    def get_member_program(self, obj):
        try:
            member = Student.objects.get(id=obj.student_id)
            return member.program
        except Student.DoesNotExist:
            return None
