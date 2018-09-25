#!/usr/bin/env python

import asyncio
import websockets


async def run(url):
    async with websockets.client.connect(url) as ws:
        for i in range(1000):
            msg = 'message - {}'.format(i)

            await ws.send(msg)
            recvd = await ws.recv()

            # if msg != recvd:
            #     print('Invalid data received: sent={}, received={}'.format(msg, recvd))

        await ws.close()


async def main(url, ops):
    for i in range(ops):
        await run(url)


if __name__ == '__main__':
    import sys
    url = sys.argv[1]
    ops = int(sys.argv[2])
    parallel = int(sys.argv[3])

    loop = asyncio.get_event_loop()
    tasks = []
    for p in range(parallel):
        tasks.append(loop.create_task(main(url, ops)))

    loop.run_until_complete(asyncio.gather(*tasks))

    loop.close()
