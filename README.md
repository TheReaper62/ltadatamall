## LTA Datamall API Wrapper (Python)
> This is an Unoffical Wrapper and this repo has no relation nor endorsement with/from LTA
####v0.0.7
**Library Features:**
- Sync/Async
- Lightweight
- Easy to Use
- Open Source


### Setup
**********

##### Windows
```shell
>>> pip install LTADatamall
```

##### MacOS
```shell
>>> pip3 install LTADatamall
```

### Services/Information Provided
**********************************
1. Bus Related
    - Bus Arrival
    - Bus Stop
    - Bus Route

2. Passenger Volume
    - Train Station
    - Bus Stop

3. Taxi
    - Taxi Stop/Stand
    - Avaliable Taxis

4. Train Service Alert
    - Train Service Alert Messages

### Simple Usage
*****************
1. Asynchronous
```py
from LTADatamall import BusManager
import asyncio
async def main():
    client = BusManager('APIKEY')
    fav = await client.async_get_services([3,68])
    print(fav)
asyncio.run(main())
```
2. Synchronous (Normal)
```py
from LTADatamall import BusManager
client = BusManager('APIKEY')
fav_timings = client.get_bus_arrival(12345,[3,68])
print(fav_timings)
```