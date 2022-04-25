from typing import Any

from aiohttp import ClientSession, ClientConnectorError
from requests import Session, exceptions

class DataFrame:
    def __init__(self, API_KEY:str):
        self.BASE_URL = "http://datamall2.mytransport.sg/ltaodataservice"
        self.HEADERS = {"Accept": "application/json", "AccountKey": API_KEY}

    def send(self, path, params:dict[str,Any]={}, json:dict[str,Any]={}):
        with Session() as session:
            try:
                response = session.get(self.BASE_URL+"/"+path, params=params, headers=self.HEADERS,json=json)
                if response.status_code == 200:
                    return response.json()
                else:
                    raise Exception(f"An Error Occured: {response.reason}")
            except exceptions.RequestException as error:
                raise Exception(str(error)) from None

    async def async_send(self, path, params:dict[str,Any]={}, json:dict[str,Any]={}):
        async with ClientSession() as session:
            try:
                async with session.get(self.BASE_URL+"/"+path, params=params, headers=self.HEADERS, json=json) as response:
                    if response.status == 200:
                        return await response.json()
                    else:
                        raise Exception(f"An Error Occured: {response.reason}")
            except ClientConnectorError as error:
                raise Exception(str(error)) from None
    
