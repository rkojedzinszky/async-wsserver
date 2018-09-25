#!/usr/bin/env python

from aiohttp import web


async def ws_handler(request):

    ws = web.WebSocketResponse()
    await ws.prepare(request)

    async for msg in ws:
        await ws.send_str(msg.data)

    return ws

if __name__ == '__main__':
    app = web.Application()
    app.add_routes([web.get('/', ws_handler)])

    web.run_app(app)
