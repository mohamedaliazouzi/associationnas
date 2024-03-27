from django.contrib import admin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from django import forms
from django.urls import path
from import_export.admin import ImportExportModelAdmin
# Register your models here.
from versements.models import Versements


class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()


class VersementAdmin(ImportExportModelAdmin):
    list_display = ('agriculteur', 'date_versement', 'num_versement', 'montant_versement')

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('upload-csv/', self.import_csv, name='upload-csv'),
        ]
        return custom_urls + urls

    def import_csv(self, request):

        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]

            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'The wrong file type was uploaded')
                return HttpResponseRedirect(request.path_info)

            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")

            for x in csv_data:
                fields = x.split(",")
                created = Versements.objects.create(
                    agriculteur=fields[0],
                    date_versement=fields[1],
                    num_versement=fields[2],
                    montant_versement=fields[3]
                )
            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "templates/html/import_csv.html", data)


admin.site.register(Versements, VersementAdmin)
