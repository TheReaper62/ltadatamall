from typing import Union, Callable, Any

from .base import DataFrame

__all__ = (
    'BusService',
)

class BusService:
    def __init__(self, **kwargs):
        operator_map = {"SBST": "SBS Transit",
                        "SMRT": "SMRT Corporation",
                        "TTS": "Tower Transit Singapore",
                        "GAS": "Go Ahead Singapore"}
        self.service_no = kwargs.get("ServiceNo",None)
        self.operator = operator_map.get(kwargs.get("Operator",None),'Not Available')
        self.direction = kwargs.get("Direction",None)
        self.category = kwargs.get("Category",None)
        self.origin_code = kwargs.get("OriginCode",None)
        self.destination_code = kwargs.get("DestinationCode",None)
        self.am_peak_freq = kwargs.get("AM_Peak_Freq",None)
        self.am_offpeak_freq = kwargs.get("AM_Offpeak_Freq",None)
        self.pm_peak_freq = kwargs.get("PM_Peak_Freq",None)
        self.pm_offpeak_freq = kwargs.get("PM_Offpeak_Freq",None)
        self.loop_desc = kwargs.get("LoopDesc",None)
