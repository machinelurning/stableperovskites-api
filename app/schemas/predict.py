from typing import Any, List, Optional
import numpy as np

from pydantic import BaseModel
from regression_model.processing.validation import PerovskiteOxideSchema


class PredictionResults(BaseModel):
    errors: Optional[Any]
    version: str
    predictions: Optional[List[float]]


class MultiplePerovskiteOxideSchema(BaseModel):
    inputs: List[PerovskiteOxideSchema]

    class Config:
        schema_extra = {
            "example": {
                "inputs": [
                    {
                        "COMPOSITION": "Ba1Sr7V8O24",
                        "A_SITE_1": "Ba",
                        "A_SITE_2": "Sr",
                        "A_SITE_3": None,
                        "B_SITE_1": "V",
                        "B_SITE_2": None,
                        "B_SITE_3": None,
                        "NUM_ELEMS": 4,
                    }
                ]
            }
        }
