Async websocket server bencmark
===============================

* Required packages
```
pip install -U pip aiohttp websockets
```

* Run one of the servers:
```
python aiohttp-server.py
```

Or

```
python websockets-server.py
```

And run the client:
```
python wsclient.py ws://127.0.0.1:8080/ 100 10
```
