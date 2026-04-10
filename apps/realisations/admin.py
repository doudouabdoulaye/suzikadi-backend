from django.contrib import admin
from .models import Realisation, RealisationImage


class RealisationImageInline(admin.TabularInline):
    model = RealisationImage
    extra = 1


@admin.register(Realisation)
class RealisationAdmin(admin.ModelAdmin):
    inlines = [RealisationImageInline]