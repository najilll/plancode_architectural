from django.contrib import admin
from .models import Baner, Blog, Contact,Portfolio,Transformation,Employee,Testimonial,PortfolioCategory
from import_export.admin import ImportExportActionModelAdmin


# Register your models here.
@admin.register(Baner)
class BanerAdmin(ImportExportActionModelAdmin):
    list_display = ("title", "description", "background_image","is_active",)
    search_fields = ("title",)

@admin.register(PortfolioCategory)
class CategoryAdmin(ImportExportActionModelAdmin):
    list_display = ("title", "is_active",)


@admin.register(Portfolio)
class PortfolioAdmin(ImportExportActionModelAdmin):
    list_display = ("title", "sub_title", "background_image","is_active","category",)
    search_fields = ("title",)
    prepopulated_fields = {"slug": ("title",)}

@admin.register(Transformation)
class TransformationAdmin(ImportExportActionModelAdmin):
    list_display = ("before", "after",)
    search_fields = ("before", "after",)

@admin.register(Employee)
class EmployeeAdmin(ImportExportActionModelAdmin):
    list_display = ("name", "position","image","is_active",)
    search_fields = ("name",)

@admin.register(Testimonial)
class TestimonialAdmin(ImportExportActionModelAdmin):
    list_display = ("name", "description", "image","is_active",)
    search_fields = ("name",)

@admin.register(Blog)
class BlogAdmin(ImportExportActionModelAdmin):
    list_display = ("title", "date", "image","is_active","is_home",)
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("title",)}

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone_number",)
    search_fields = ("name",)