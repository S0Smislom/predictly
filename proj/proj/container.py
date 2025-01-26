import os

from adapters.prediction.gigachat import GigachatPredictionService

from proj.port.prediction import IPredictionService


class Container:
    def __init__(self):
        self.GIGACHAT_API_KEY = os.environ.get("GIGACHAT_API_KEY")

    def prediction_service(self) -> IPredictionService:
        return GigachatPredictionService(self.GIGACHAT_API_KEY)
