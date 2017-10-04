from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from django.db import models

from django.contrib.contenttypes.admin import GenericTabularInline

# Register your models here.

from .models import QualityControl, Sentence, Recording, Source


class QualityControlInline(GenericTabularInline):
    # max_num = 1
    extra = 0
    can_delete = False
    model = QualityControl


class RecordingsInline(admin.TabularInline):
    extra = 0
    can_delete = False
    model = Recording


@admin.register(QualityControl)
class QualityControlAdmin(admin.ModelAdmin):
    list_display = ('updated', 'content_type', 'object_id')
    date_hierarchy = 'updated'


@admin.register(Sentence)
class SentenceAdmin(admin.ModelAdmin):
    list_display = ('text', 'updated', 'get_approved', 'get_approved_by',
                    'num_recordings')
    inlines = [QualityControlInline, RecordingsInline]

    def get_queryset(self, request):
        qs = super(SentenceAdmin, self).get_queryset(request)
        qs = qs.annotate(models.Count('recording'))\
            .annotate(sum_approved=models.Sum(
                models.Case(
                    models.When(
                        quality_control__approved=True,
                        then=models.Value(1)),
                    models.When(
                        quality_control__approved=False,
                        then=models.Value(0)),
                    default=models.Value(0),
                    output_field=models.IntegerField())
                ))
        return qs

    def get_approved(self, obj):
        qc = obj.quality_control
        return obj.sum_approved
    get_approved.short_description = 'Approvals'
    get_approved.admin_order_field = 'sum_approved'

    def get_approved_by(self, obj):
        qc = obj.quality_control
        results = qc.all()
        names = []
        if len(results) > 0:
            for r in results:
                if r.approved_by:
                    names.append(str(r.approved_by))
            return ', '.join(names)
        else:
            return _("None")
    get_approved_by.short_description = 'Approved By'
    get_approved_by.admin_order_field = 'quality_control__approved'

    def num_recordings(self, obj):
        return obj.recording__count
    num_recordings.short_description = '# Recordings'
    num_recordings.admin_order_field = 'recording__count'


@admin.register(Recording)
class RecordingAdmin(admin.ModelAdmin):
    readonly_fields = ('duration',)


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    pass
