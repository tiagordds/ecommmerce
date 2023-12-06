from django.contrib import admin
from . import models


class VariacaoInLine(admin.TabularInline):
    model = models.Variacao
    extra = 1


class ProdutoAdmin(admin.ModelAdmin):
    inlines = [
        VariacaoInLine
    ]


admin.site.register(models.Produto, ProdutoAdmin)
admin.site.register(models.Variacao)
