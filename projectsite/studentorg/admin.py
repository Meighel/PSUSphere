from django.contrib import admin
from .models import College, Program, Organization, Student, OrgMember

@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ("college_name",)
    search_fields = ("college_name",)

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ("prog_name", "get_college")
    search_fields = ("prog_name",)

    @admin.display(description="College")
    def get_college(self, obj):
        return obj.college.college_name

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("name", "get_college")
    search_fields = ("name",)

    @admin.display(description="College")
    def get_college(self, obj):
        return obj.college.college_name if obj.college else None

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_id", "lastname", "firstname", "middlename", "get_program")
    search_fields = ("lastname", "firstname")

    @admin.display(description="Program")
    def get_program(self, obj):
        return obj.program.prog_name

@admin.register(OrgMember)
class OrgMemberAdmin(admin.ModelAdmin):
    list_display = ("student", "get_member_program", "organization", "date_joined")
    search_fields = ("student__lastname", "student__firstname")

    @admin.display(description="Member Program")
    def get_member_program(self, obj):
        return obj.student.program.prog_name
