from typing import Union, Callable, Any

from .base import DataFrame

__all__ = (
    'PassengerVolume'
)

class PassengerVolume(DataFrame):
    def __init__(self, api_key: str):
        super().__init__(api_key)
    '''
        date:str (YYYYMM)
        Example : "201912"
        Up to Last 3 Months
        '''

    # By Bus Stop
    def pv_bus_stop(self, date: str = "") -> str:
        params = {"Date": date} if date != "" else {}
        response = self.send('PV/Bus', params=params)
        if response.get('value', False):
            return response.get('Link', 'Not Available')
        raise Exception('API Returned None')

    async def async_pv_bus_stop(self, date: str ="") -> str:
        params = {"Date": date} if date != "" else {}
        response = await self.async_send('PV/Bus', params=params)
        if response.get('value', False):
            return response.get('Link', 'Not Available')
        raise Exception('API Returned None')

    # By Orgin Destination Bus Stops
    def pv_od_bus_stop(self, date: str ="") -> str:
        params = {"Date": date} if date != "" else {}
        response = self.send('PV/ODBus', params=params)
        if response.get('value', False):
            return response.get('Link', 'Not Available')
        raise Exception('API Returned None')

    async def async_pv_od_bus_stop(self, date: str ="") -> str:
        params = {"Date": date} if date != "" else {}
        response = await self.async_send('PV/ODBus', params=params)
        if response.get('value', False):
            return response.get('Link', 'Not Available')
        raise Exception('API Returned None')

    # By Orgin Destination Train Stations
    def pv_od_train_destination(self, date: str ="") -> str:
        params = {"Date": date} if date != "" else {}
        response = self.send('PV/ODTrain', params=params)
        if response.get('value', False):
            return response.get('Link', 'Not Available')
        raise Exception('API Returned None')

    async def async_pv_od_train_destination(self, date: str ="") -> str:
        params = {"Date": date} if date != "" else {}
        response = await self.async_send('PV/ODTrain', params=params)
        if response.get('value', False):
            return response.get('Link', 'Not Available')
        raise Exception('API Returned None')

    # By Train Stations
    def pv_od_train_destination(self, date: str ="") -> str:
        params = {"Date": date} if date != "" else {}
        response = self.send('PV/Train', params=params)
        if response.get('value', False):
            return response.get('Link', 'Not Available')
        raise Exception('API Returned None')

    async def async_pv_od_train_destination(self, date: str ="") -> str:
        params = {"Date": date} if date != "" else {}
        response = await self.async_send('PV/Train', params=params)
        if response.get('value', False):
            return response.get('Link', 'Not Available')
        raise Exception('API Returned None')
