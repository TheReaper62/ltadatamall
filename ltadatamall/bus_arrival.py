from typing import Union, Callable, Any

__all__ = (
    'NextBus',
    'BusArrivalService',
)

class NextBus:
    def __init__(self, **kwargs):
        load_map = {"SEA":"Seats Available", "SDA":"Standing Avaialble", "LSD":"Limited Standing"}
        type_map = {"SD":"Single Decker", "DD":"Double Decker", "BD":"Bendy"}
        self.orgin_code = kwargs.get('OrginCode','Not Available')
        self.destination_code = kwargs.get('DestinationCode','Not Available')
        self.estimated_arrival = kwargs.get('EstimatedArrival','No Estimated Time')
        self.latitude = kwargs.get('Latitude',0.0)
        self.longitude = kwargs.get('Longitude',0.0)
        self.visit_number = int(kwargs['VisitNumber']) if kwargs.get('VisitNumber','') != '' else 'Not Available'
        self.load = load_map.get(kwargs.get('Load',None),'Not Available')
        self.feature = "Not Wheel-chair Accessible" if kwargs.get('Feature',"") == "" else "Wheel-chair Accessible"
        self.type = type_map.get(kwargs.get('Type'),'Not Available')

class BusArrivalService:
    def __init__(self,**kwargs):
        '''
        service_no: int
        operator: str
        next_bus: list[NextBus]
        '''
        operator_map = {"SBST": "SBS Transit",
                        "SMRT": "SMRT Corporation",
                        "TTS": "Tower Transit Singapore",
                        "GAS": "Go Ahead Singapore"}
        self.service_no = kwargs.get('ServiceNo',None)
        self.operator = operator_map.get(kwargs.get('Operator',None),'Not Available')
        self.next_1 = NextBus(**kwargs.get('NextBus',{}))
        self.next_2 = NextBus(**kwargs.get('NextBus2',{}))
        self.next_3 = NextBus(**kwargs.get('NextBus3',{}))