from typing import Union, Callable, Any

from dateutil import parser

from .base import DataFrame

__all__ = (
    'BusManager',
    'NextBus',
    'BusArrivalService',
    'BusService',
    'BusRoutes',
    'BusStop'
)

class NextBus:
    def __init__(self, **kwargs):
        load_map = {"SEA":"Seats Available", "SDA":"Standing Avaialble", "LSD":"Limited Standing"}
        type_map = {"SD":"Single Decker", "DD":"Double Decker", "BD":"Bendy"}
        self.orgin_code = kwargs.get('OrginCode','Not Available')
        self.destination_code = kwargs.get('DestinationCode','Not Available')
        self.estimated_arrival = parser.parse(kwargs['EstimatedArrival']) if kwargs.get('EstimatedArrival',False) else "No Estimated Time"
        self.latitude = kwargs.get('Latitude',0.0)
        self.longitude = kwargs.get('Longitude',0.0)
        self.visit_number = int(kwargs['VisitNumber']) if kwargs.get('VisitNumber','')!='' else 'Not Available'
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
        self.next_1 = [NextBus(**kwargs.get('NextBus',{}))]
        self.next_2 = [NextBus(**kwargs.get('NextBus2',{}))]
        self.next_3 = [NextBus(**kwargs.get('NextBus3',{}))]

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

class BusRoutes:
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

class BusStop:
    def __init__(self,**kwargs):
        self.bus_stop_code = kwargs.get("BusStopCode",'Not Avaialble')
        self.road_name = kwargs.get("RoadName",'Not Available')
        self.description = kwargs.get("Description",'Not Available')
        self.latitude = float(kwargs.get("Latitude",0))
        self.longitude = float(kwargs.get("Longitude",0))

class BusManager(DataFrame):
    def __init__(self, API_KEY: str):
        super().__init__(API_KEY)

    # Bus Arrival
    def get_bus_arrival(self, bus_stop_code: Union[str, int, BusStop], service_no: Union[str, int] = 0) -> list[BusArrivalService]:
        params = {'BusStopCode': bus_stop_code} if not isinstance(bus_stop_code,BusStop) else {'BusStopCode': bus_stop_code.bus_stop_code}
        if service_no != 0:
            params['ServiceNo'] = service_no
        response = self.send("BusArrivalv2", params=params)
        if response.get('Services', False):
            return [BusArrivalService(**i) for i in response['Services']]
        raise Exception('API Returned None')

    async def async_get_bus_arrival(self, bus_stop_code: Union[str, int, BusStop], service_no: Union[str, int] = 0) -> list[BusArrivalService]:
        params = {'BusStopCode': bus_stop_code} if not isinstance(bus_stop_code,BusStop) else {'BusStopCode': bus_stop_code.bus_stop_code}
        if service_no != 0:
            params['ServiceNo'] = service_no
        response = await self.async_send("BusArrivalv2", params=params)
        if response.get('Services', False):
            return [BusArrivalService(**i) for i in response['Services']]
        raise Exception('API Returned None')

    # Bus Services
    def get_services(self, services: list[Union[str, int]] = []) -> list[BusService]:
        response = self.send("BusServices")
        if response.get('value', False):
            return [BusService(**i) for i in response['value'] if i['ServiceNo'] in list(map(str, services))]
        raise Exception('API Returned None')

    async def async_get_services(self, services: list[Union[str, int]] = []) -> list[BusService]:
        response = await self.async_send("BusServices")
        if response.get('value', False):
            return [BusService(**i) for i in response['value'] if i['ServiceNo'] in list(map(str, services))]
        raise Exception('API Returned None')

    # Bus Routes
    def get_routes(self, **filters) -> list[BusRoutes]:
        response = self.send('BusRoutes')

        def processed_filter(raw_dict: dict[str, Any]) -> bool:
            for key, value in filters.items():
                if raw_dict.get(key, None) != value:
                    return False
            return True
        if response.get('value', False):
            return [BusRoutes(**i) for i in response['value'] if processed_filter(i)]
        raise Exception('API Returned None')

    async def async_get_routes(self, **filters) -> list[BusRoutes]:
        response = await self.async_send('BusRoutes')

        def processed_filter(raw_dict: dict[str, Any]) -> bool:
            for key, value in filters.items():
                if raw_dict.get(key, None) != value:
                    return False
            return True
        if response.get('value', False):
            return [BusRoutes(**i) for i in response['value'] if processed_filter(i)]
        raise Exception('API Returned None')

    # Bus Stops
    def get_stops(self,bus_stop_codes:Union[int,list[int],str,list[str]]=[]):
        response = self.send('BusStops')
        if response.get('value', False):
            return [BusStop(**i) for i in response['value'] if str(i['BusStopCode']) in list(map(str, bus_stop_codes))]
        raise Exception('API Returned None')

    async def async_get_stops(self,bus_stop_codes:Union[int,list[int],str,list[str]]=[]):
        response = await self.async_send('BusStops')
        if response.get('value', False):
            return [BusStop(**i) for i in response['value'] if str(i['BusStopCode']) in list(map(str,bus_stop_codes))]
        raise Exception('API Returned None')

    