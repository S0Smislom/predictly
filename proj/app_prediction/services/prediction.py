from random import choice

from app_prediction.models import Prediction


class PredictionService:
    async def get_random(self) -> Prediction:
        pks = [
            _
            async for _ in Prediction.objects.filter(published=True).values_list(
                "pk", flat=True
            )
        ]
        random_pk = choice(pks)
        random_obj = await Prediction.objects.aget(pk=random_pk)
        return random_obj
