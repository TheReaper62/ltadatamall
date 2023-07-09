from LTADatamall import BusManager

import asyncio

async def main():
    driver = BusManager('APIKEY')
    # Print all bus timings for bus top (code: 95129)
    results = await driver.async_get_bus_arrival(95129)
    print([results[i].next_1.estimated_arrival for i in results])
asyncio.run(main())
