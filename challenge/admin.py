from django.contrib import admin
from challenge.models import Challenge, Attachment, DockerConfig, Category, Tag


class AttachmentInline(admin.StackedInline):
    model = Attachment
    fk_name = 'challenge_one'


class DockerConfigInline(admin.StackedInline):
    model = DockerConfig
    fk_name = 'challenge_two'


@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    list_display = ['title', 'environment_type', 'category','state', 'score',  'is_fixed_flag', 'have_attachment', 'tag']
    readonly_fields = ['mark_total', 'mark_count']
    inlines = [AttachmentInline, DockerConfigInline]

    def tag(self, obj):
        return [Tag.name for Tag in obj.tag.all()]


@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    list_display = ['file']


@admin.register(DockerConfig)
class DockerConfigAdmin(admin.ModelAdmin):
    list_display = ['name', 'port', 'memory_limit', 'cpu_limit']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
