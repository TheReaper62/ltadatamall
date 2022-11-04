from typing import Union, Callable, Any

from .base import DataFrame

from .bus_stop import BusStop
from .bus_service import BusService
from .bus_route import BusRoute
from .bus_arrival import NextBus, BusArrivalService

__all__ = (
    'BusManager',
)

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
    def get_routes(self, **filters) -> list[BusRoute]:
        response = self.send('BusRoute')

        def processed_filter(raw_dict: dict[str, Any]) -> bool:
            for key, value in filters.items():
                if raw_dict.get(key, None) != value:
                    return False
            return True
        if response.get('value', False):
            return [BusRoute(**i) for i in response['value'] if processed_filter(i)]
        raise Exception('API Returned None')

    async def async_get_routes(self, **filters) -> list[BusRoute]:
        response = await self.async_send('BusRoute')

        def processed_filter(raw_dict: dict[str, Any]) -> bool:
            for key, value in filters.items():
                if raw_dict.get(key, None) != value:
                    return False
            return True
        if response.get('value', False):
            return [BusRoute(**i) for i in response['value'] if processed_filter(i)]
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
