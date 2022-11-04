from typing import Union, Callable, Any

from .base import DataFrame

__all__ = (
    'BusStop',
)

class BusStop:
    def __init__(self,**kwargs):
        self.bus_stop_code = kwargs.get("BusStopCode",'Not Avaialble')
        self.road_name = kwargs.get("RoadName",'Not Available')
        self.description = kwargs.get("Description",'Not Available')
        self.latitude = float(kwargs.get("Latitude",0))
        self.longitude = float(kwargs.get("Longitude",0))
