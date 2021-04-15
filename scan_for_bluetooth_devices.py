import asyncio
from bleak import BleakScanner

def scan():
    async def run():
        devices = await BleakScanner.discover()
        # for d in devices:
        #     print(d)
        return devices

    loop = asyncio.get_event_loop()
    return loop.run_until_complete(run())

print(scan())

