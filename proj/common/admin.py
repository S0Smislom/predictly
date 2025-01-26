from django.contrib import admin


# Register your models here.
@admin.action(description="Publish")
def publish(modeladmin, request, queryset):
    queryset.update(published=True)


@admin.action(description="Unpublish")
def unpublish(modeladmin, request, queryset):
    queryset.update(published=False)
