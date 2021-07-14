# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License

__version__ = "0.0.1"
__license__ = "MIT"


from .data_collector import CsvDataCollector, SqlDataCollector

__all__ = [
    "CsvDataCollector",
    "SqlDataCollector",
]
