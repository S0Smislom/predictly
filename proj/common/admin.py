from django.contrib import admin


# Register your models here.
@admin.action(description="Publish")
def publish(modeladmin, request, queryset):
    queryset.update(published=True)


@admin.action(description="Unpublish")
def unpublish(modeladmin, request, queryset):
    queryset.update(published=False)


@admin.action(description="Create predictions")
def create_predictions(modeladmin, request, queryset):
    from app_prediction.models import Prediction

    predictions = []
    for _ in queryset:
        predictions.append(Prediction(content_object=_, published=False))
    if predictions:
        Prediction.objects.bulk_create(predictions, batch_size=100)
