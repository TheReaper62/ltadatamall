from typing import Union, Optional, Any

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
    def get_bus_arrival(self, bus_stop_code: Union[str, int, BusStop], service_no: Optional[Union[str, int]] = None) -> list[BusArrivalService]:
        params = {'BusStopCode': bus_stop_code} if not isinstance(bus_stop_code,BusStop) else {'BusStopCode': bus_stop_code.bus_stop_code}
        if service_no != None:
            params['ServiceNo'] = service_no
        response = self.send("BusArrivalv2", params=params)
        if response.get('Services', False):
            return [BusArrivalService(**i) for i in response['Services']]
        raise Exception('API Returned None')

    async def async_get_bus_arrival(self, bus_stop_code: Union[str, int, BusStop], service_no: Optional[Union[str, int]] = None) -> list[BusArrivalService]:
        params = {'BusStopCode': bus_stop_code} if not isinstance(bus_stop_code,BusStop) else {'BusStopCode': bus_stop_code.bus_stop_code}
        if service_no != None:
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

    def get_all_services(self) -> list[BusService]:
        services = []
        while len(services)%500 == 0:
            response = self.send('BusServices',params={"$skip":len(services)})
            if response.get('value', False):
                services.extend([BusService(**i) for i in response['value']])
                continue
            elif len(services) == 0:
                raise Exception('API Returned None')
            break
        return services

    def async_get_all_services(self) -> list[BusService]:
        services = []
        while len(services)%500 == 0:
            response = self.async_send('BuServices',params={"$skip":len(services)})
            if response.get('value', False):
                services.extend([BusService(**i) for i in response['value']])
                continue
            elif len(services) == 0:
                raise Exception('API Returned None')
            break
        return services

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

    def get_all_routes(self) -> list[BusRoute]:
        routes = []
        while len(routes)%500 == 0:
            response = self.send('BusRoutes',params={"$skip":len(routes)})
            if response.get('value', False):
                routes.extend([BusRoute(**i) for i in response['value']])
                continue
            elif len(routes) == 0:
                raise Exception('API Returned None')
            break
        return routes

    def async_get_all_routes(self) -> list[BusRoute]:
        routes = []
        while len(routes)%500 == 0:
            response = self.async_send('BusRoutes',params={"$skip":len(routes)})
            if response.get('value', False):
                routes.extend([BusRoute(**i) for i in response['value']])
                continue
            elif len(routes) == 0:
                raise Exception('API Returned None')
            break
        return routes

    # Bus Stops
    def get_stops(self,bus_stop_codes:Union[int,list[int],str,list[str]]) -> list[BusStop]:
        all_stops = self.async_get_all_stops()

        # Query single bus stop either as str or int
        if isinstance(bus_stop_codes, int) or isinstance(bus_stop_codes, str):
            return [BusStop(**i) for i in all_stops if str(i['BusStopCode']) == str(bus_stop_codes)][0]
        # Query list of stops 
        elif iter(bus_stop_codes):
            return [BusStop(**i) for i in all_stops if str(i['BusStopCode']) in list(map(str, bus_stop_codes))]

    async def async_get_stops(self,bus_stop_codes:Union[int,list[int],str,list[str]]) -> list[BusStop]:
        all_stops = self.async_get_all_stops()
        # Query single bus stop either as str or int
        if isinstance(bus_stop_codes, int) or isinstance(bus_stop_codes, str):
            return [BusStop(**i) for i in all_stops if str(i['BusStopCode']) == str(bus_stop_codes)][0]
        # Query list of stops 
        elif iter(bus_stop_codes):
            return [BusStop(**i) for i in all_stops if str(i['BusStopCode']) in list(map(str,bus_stop_codes))]

    def get_all_stops(self) -> list[BusStop]:
        stops = []
        while len(stops)%500 == 0:
            response = self.send('BusStops',params={"$skip":len(stops)})
            if response.get('value', False):
                stops.extend([BusStop(**i) for i in response['value']])
                continue
            elif len(stops) == 0:
                raise Exception('API Returned None')
            break
        return stops

    def async_get_all_stops(self) -> list[BusStop]:
        stops = []
        while len(stops)%500 == 0:
            response = self.async_send('BusStops',params={"$skip":len(stops)})
            if response.get('value', False):
                stops.extend([BusStop(**i) for i in response['value']])
                continue
            elif len(stops) == 0:
                raise Exception('API Returned None')
            break
        return stops