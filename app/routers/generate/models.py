from pydantic import BaseModel, Field
from bson import ObjectId

class PredictedDataModel(BaseModel):
    """GenerateRequest model."""

    """
    {
    _id: objectId
    "stock": ITC,
    "predictions" : [
                {
                "date": "221225",
                "previous_close" : 2323.232,
                "day1" : {
                        "prediction" : 2323.412,
                        "profit/loss" : "profit",
                        "diff" : 0.18,
                        },
                "day2" : {
                        "prediction" : 2323.412,
                        "profit/loss" : "profit",
                        "diff" : 0.18,
                        },
                "day3" : {
                        "prediction" : 2323.412,
                        "profit/loss" : "profit",
                        "diff" : 0.18,
                        },
                "day4" : {
                        "prediction" : 2323.412,
                        "profit/loss" : "profit",
                        "diff" : 0.18,
                        },
                "day5" : {
                        "prediction" : 2323.412,
                        "profit/loss" : "profit",
                        "diff" : 0.18,
                        },
                "day6" : {
                        "prediction" : 2323.412,
                        "profit/loss" : "profit",
                        "diff" : 0.18,
                        },
                }
            ]
		}
    """
    _id: ObjectId = Field(default_factory=ObjectId)
    stock: str = Field(...)
    predictions: list = Field(...)

    
    class Config:
        """Config for PredictedDataModel."""

        schema_extra = {
            "example": {
                "_id": "60d9c9a9f4b0f4b4b4b4b4b4",
                "stock": "ITC",
                "predictions": [
                    {
                        "date": "221225",
                        "previous_close": 2323.232,
                        "day1": {
                            "prediction": 2323.412,
                            "profit/loss": "profit",
                            "diff": 0.18,
                        },
                        "day2": {
                            "prediction": 2323.412,
                            "profit/loss": "profit",
                            "diff": 0.18,
                        },
                        "day3": {
                            "prediction": 2323.412,
                            "profit/loss": "profit",
                            "diff": 0.18,
                        },
                        "day4": {
                            "prediction": 2323.412,
                            "profit/loss": "profit",
                            "diff": 0.18,
                        },
                        "day5": {
                            "prediction": 2323.412,
                            "profit/loss": "profit",
                            "diff": 0.18,
                        },
                        "day6": {
                            "prediction": 2323.412,
                            "profit/loss": "profit",
                            "diff": 0.18,
                        },
                    }
                ],
            }
        }


    