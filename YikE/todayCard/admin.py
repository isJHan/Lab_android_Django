# from YikE.todayCard.models import QnjrCard, TodayCard
from .models import TodayCard, QnjrCard
from django.contrib import admin
# from django.utils.safestring import mark_safe
# Register your models here.


class TodayCardAdmin(admin.ModelAdmin):
    readonly_fields = ('pictuer_preview',)

    # fields = ( 'picture', )

admin.site.register(TodayCard, TodayCardAdmin)
admin.site.register(QnjrCard)

# @admin.register(TodayCard)
# class HeroAdmin(admin.ModelAdmin):

#     readonly_fields = ['picture', "headshot_image"]

#     def headshot_image(self, obj):
#         return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
#             url = obj.headshot.url,
#             width=obj.headshot.width,
#             height=obj.headshot.height,
#             )
#     )
