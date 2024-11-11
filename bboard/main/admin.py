from django.contrib import admin
import datetime
from .models import AdvUser
from .utilities import send_activation_notification
from .forms import SubRubricForm
from .models import SuperRubric, SubRubric
from .models import Bb, AdditionalImage


class SubRubricInline(admin.TabularInline):
    model = SubRubric

# Register your models here.

def send_activation_notifications(modeladmin, request, queryset):
    for rec in queryset:
        if not rec.is_activated:
            send_activation_notification(rec)
    modeladmin.message_user(request, 'Письма с оповещениями отправлены')


send_activation_notifications.short_description = 'Отправка писем с оповещениями об активации'


class NoactivatedFilter(admin.SimpleListFilter):
    title = 'Прошли активацию?'
    parameter_name = 'actstate'

    def lookups(self, request, model_admin):
        return (
            ('activated', 'Прошли'),
            ('threedays', 'Не прошли более 3 дней'),
            ('week', 'Не прошли более недели'),
        )

    def queryset(self, request, queryset):
        val = self.value()
        if val == 'activated':
            return queryset.filter(is_active=True, is_activated=True)
        elif val == 'threedays':
            d = datetime.date.today() - datetime.timedelta(days=3)
            return queryset.filter(is_active=False, is_activated=False,
                                   date_joined__date__lt=d)
        elif val == 'week':
            d = datetime.date.today() - datetime.timedelta(weeks=1)
            return queryset.filter(is_active=False, is_activated=False,
                                   date_joined__date__lt=d)


class AdvUserAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'is_activated', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = (NoactivatedFilter,)
    fields = (
        ('username', 'email'),
        ('first_name', 'last_name'),
        ('is_staff', 'is_superuser'),
        ('last_login', 'date_joined')
    )
    readonly_fields = ('last_login', 'date_joined',)
    actions = (send_activation_notifications,)


admin.site.register(AdvUser, AdvUserAdmin)


class SuperRubricAdmin(admin.ModelAdmin):
    form = SubRubricForm
    exclude = ('super_rubric',)
    inlines = (SubRubricInline,)
    def get_form(self, request, obj=None, **kwargs):
        form = super(SuperRubricAdmin, self).get_form(request, obj, **kwargs)
        if obj is None or isinstance(obj, SuperRubric):
            form.base_field.pop('super_rubric', None)
        return form

admin.site.register(SuperRubric, SuperRubricAdmin)

class AdditionalImageInline(admin.TabularInline):
   model = AdditionalImage


class BbAdmin(admin.ModelAdmin):
   list_display = ('rubric', 'title', 'content', 'author', 'created_at')
   fields = (('rubric', 'author'), 'title', 'content', 'price',
             'contacts', 'image', 'is_active')
   inlines = (AdditionalImageInline,)


admin.site.register(Bb, BbAdmin)