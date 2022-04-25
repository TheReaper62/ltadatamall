from ltadatamall import BusManager

import asyncio

async def main():
    driver = BusManager('APIKEY')
    res = await driver.async_get_services([3,68])
    for i in res:
        print(vars(i),"\n\n")
asyncio.run(main())

