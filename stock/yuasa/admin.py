from django.contrib import admin

from yuasa.models import PaletteSauron, PalettePicard


@admin.register(PaletteSauron)
class PaletteSauronAdmin(admin.ModelAdmin):
    list_display = ['reference',
                    'date_code',
                    'dateTransfert',
                    'voltage',
                    'number_of_palettes',
                    'quantity_per_palette',
                    'type',
                    'date_limite',
                    ]


@admin.register(PalettePicard)
class PalettePicardAdmin(admin.ModelAdmin):
    list_display = ['reference',
                    'date_code',
                    'dateTransfert',
                    'voltage',
                    'number_of_palettes',
                    'quantity_per_palette',
                    'type',
                    'date_limite',
                    ]
