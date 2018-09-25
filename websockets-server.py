#!/usr/bin/env python

import asyncio
import websockets


async def ws_handler(ws, path):
    while True:
        try:
            msg = await ws.recv()
        except websockets.exceptions.ConnectionClosed:
            break

        await ws.send(msg)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    server = websockets.serve(ws_handler, '127.0.0.1', 8080)
    loop.run_until_complete(server)
    loop.run_forever()
    loop.close()
