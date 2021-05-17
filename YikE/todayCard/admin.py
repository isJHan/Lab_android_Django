# from YikE.todayCard.models import QnjrCard, TodayCard
from .models import TodayCard, QnjrCard
from django.contrib import admin
from comments.models import comment
# from django.utils.safestring import mark_safe
# Register your models here.

class commentInline(admin.StackedInline):
    model = comment
    extra = 0
    


class TodayCardAdmin(admin.ModelAdmin):
    readonly_fields = ('pictuer_preview',)

    inlines = [commentInline]
    # fields = ( 'picture', )

    # 主页面布局
    list_display = ('title', 'dzcount', 'collectcount', 'commentcount', 'state')

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
