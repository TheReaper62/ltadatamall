from .base import DataFrame

__all = (
    'TrainServiceAlertManager',
    'TrainServiceAlert'
)

class TrainServiceAlert:
    def __init__(self,**kwargs):
        self.status = kwargs.get('Status','Not Available')
        self.line = kwargs.get('Line','Not Available')
        self.direction = kwargs.get('Direction','Not Available')
        self.stations = kwargs.get('Stations',None)
        self.free_public_bus = kwargs.get('FreePublicBus',None)
        self.free_mrt_shuttle = kwargs.get('FreeMRTShuttle',None)
        self.mrt_shuttle_direction = kwargs.get('MRTShuttleDirection','Not Available')
        self.message = kwargs.get('Message','No Message')

        self.stations = self.stations.split(',') if self.stations!=None else "Not Available"
        self.free_public_bus = self.free_public_bus.split(',') if self.free_public_bus!=None else "Not Available"
        self.free_mrt_shuttle = self.free_mrt_shuttle.split(',') if self.free_mrt_shuttle!=None else "Not Available"

class TrainServiceAlertManager(DataFrame):
    def __init__(self, api_key: str):
        super().__init__(api_key)

    # Get Alerts 
    def get_alerts(self) -> str:
        response = self.send('TrainServiceAlerts')
        if response.get('value', False):
            return [TrainServiceAlert(**alert) for alert in response['value']]
        raise Exception('API Returned None')

    async def async_get_alerts(self) -> str:
        response = self.async_send('TrainServiceAlerts')
        if response.get('value', False):
            return [TrainServiceAlert(**alert) for alert in response['value']]
        raise Exception('API Returned None')
