from django.contrib import admin
import csv
from django.http import HttpResponse
from arboverse_updated.models import *
from django.urls import path
from django.http import HttpResponse
from django.contrib import admin
from django.utils.html import format_html
from django.apps import apps
import csv

def download_all_data(request):
    app_label = 'arboverse_updated'  # your app name here

    all_models = [m for m in apps.get_models() if m._meta.app_label == app_label]

    # Collect all fields from these models
    field_set = set()
    model_field_map = {}

    for model in all_models:
        field_names = [f.name for f in model._meta.fields]
        model_field_map[model] = field_names
        field_set.update(field_names)

    all_fields = sorted(field_set)
    columns = ['app_label', 'model_name'] + all_fields

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=arboverse_all_data.csv'
    writer = csv.writer(response)
    writer.writerow(columns)

    for model in all_models:
        model_name = model._meta.model_name
        app_label = model._meta.app_label
        field_names = model_field_map[model]

        for obj in model.objects.all():
            row = [app_label, model_name]
            for field in all_fields:
                # If model has field, get value, else empty string
                row.append(str(getattr(obj, field, '')) if field in field_names else '')
            writer.writerow(row)

    return response


def download_virus_vector_data(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="virus_vector_data.csv"'

    writer = csv.writer(response)

    # Write header
    writer.writerow([
        "Virus Name",
        "Virus Family",
        "Virus Genus",
        "Vector Species",
        "Vector Genus",
        "Vector Family",
        "Main Vector",
    ])

    queryset = VirusVector.objects.select_related(
        'virus', 'virus__virusfamily', 'virus__virusgenus',
        'vector', 'vector__vectorgenus', 'vector__vectorfamily'
    )

    for obj in queryset:
        writer.writerow([
            obj.virus.name if obj.virus else '',
            obj.virus.virusfamily.name if obj.virus and obj.virus.virusfamily else '',
            obj.virus.virusgenus.name if obj.virus and obj.virus.virusgenus else '',
            obj.vector.name if obj.vector else '',
            obj.vector.vectorgenus.name if obj.vector and obj.vector.vectorgenus else '',
            obj.vector.vectorfamily.name if obj.vector and obj.vector.vectorfamily else '',
            obj.main_vector,
        ])

    return response


# This method is for the ability to download on a row by row basis.
def export_as_csv(modeladmin, request, queryset):
    """
    Generic CSV export admin action.
    """
    meta = modeladmin.model._meta
    field_names = [field.name for field in meta.fields]

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename={meta.app_label}_{meta.model_name}.csv'
    writer = csv.writer(response)

    writer.writerow(field_names)
    for obj in queryset:
        writer.writerow([getattr(obj, field) for field in field_names])

    return response


export_as_csv.short_description = "Export selected as CSV"


class ExportCsvAdmin(admin.ModelAdmin):
    actions = [export_as_csv]
    change_list_template = "admin/change_list.html"

# Import records. The second in the register allows you to do record downloading.
admin.site.register(BloodMeal, ExportCsvAdmin)
admin.site.register(Borning, ExportCsvAdmin)
admin.site.register(Country, ExportCsvAdmin)
admin.site.register(Disease, ExportCsvAdmin)
admin.site.register(FeedingPeriod, ExportCsvAdmin)
admin.site.register(Habitat, ExportCsvAdmin)
admin.site.register(Landscape, ExportCsvAdmin)
admin.site.register(Location, ExportCsvAdmin)
admin.site.register(VectorFamily, ExportCsvAdmin)
admin.site.register(VectorGenus, ExportCsvAdmin)
admin.site.register(VectorOrder, ExportCsvAdmin)
admin.site.register(VectorSpecies, ExportCsvAdmin)
admin.site.register(VectorSpeciesHabitat, ExportCsvAdmin)
admin.site.register(VectorSpeciesLocation, ExportCsvAdmin)
admin.site.register(VectorSpeciesLandscape, ExportCsvAdmin)
admin.site.register(VectorSpeciesBloodMeal, ExportCsvAdmin)
admin.site.register(VectorSpeciesFeedingPeriod, ExportCsvAdmin)
admin.site.register(VectorSubFamily, ExportCsvAdmin)
admin.site.register(Virus, ExportCsvAdmin)
admin.site.register(VirusFamily, ExportCsvAdmin)
admin.site.register(VirusGenus, ExportCsvAdmin)
admin.site.register(VirusVector, ExportCsvAdmin)
