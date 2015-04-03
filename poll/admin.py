from django.contrib import admin
from poll.models import Item, Poll
from poll.templatetags.poll_tags import percentage
from django.utils.translation import gettext as _


class PollItemInline(admin.TabularInline):
    model = Item
    extra = 0
    max_num = 15
    fields = ('value', 'pos', 'percentage', 'votes')
    readonly_fields = ('percentage', 'votes')

    def percentage(self, obj):
        "display percentage result for each answer"
        return percentage(obj.poll, obj)

    def votes(self, obj):
        "return votes for answer"
        return obj.get_vote_count()    


class PollAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'vote_count', 'is_published')
    inlines = [PollItemInline]


admin.site.register(Poll, PollAdmin)


# class VoteAdmin(admin.ModelAdmin):
#     list_display = ('poll', 'ip', 'user', 'datetime')
#     list_filter = ('poll', 'datetime')
# 
# admin.site.register(Vote, VoteAdmin)

