from typing import Union, Callable, Any

from .base import DataFrame

__all__ = (
    'BusRoute',
)

class BusRoute:
    def __init__(self, **kwargs):
        operator_map = {"SBST": "SBS Transit",
                        "SMRT": "SMRT Corporation",
                        "TTS": "Tower Transit Singapore",
                        "GAS": "Go Ahead Singapore"}
        self.service_no = kwargs.get('ServiceNo',None)
        self.operator = kwargs.get('Operator',None)
        self.direction = kwargs.get('Direction',None)
        self.stop_sequence = kwargs.get('StopSequence',None)
        self.bus_stop_code = kwargs.get('BusStopCode',None)
        self.distance = kwargs.get('Distance',None)
        self.wd_firstbus = kwargs.get('WD_FirstBus',None)
        self.wd_lastbus = kwargs.get('WD_LastBus',None)
        self.sat_firstbus = kwargs.get('SAT_FirstBus',None)
        self.sat_lastbus = kwargs.get('SAT_LastBus',None)
        self.sun_firstbus = kwargs.get('SUN_FirstBus',None)
        self.sun_lastbus = kwargs.get('SUN_LastBus',None)
