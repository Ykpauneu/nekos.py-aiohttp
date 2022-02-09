# nekosrewrite
Python module that uses Nekos API via aiohttp
# Install:
```
>>> pip install nekosrewrite
```
# Requirements
- asyncio
- aiohttp

# Example:
```py
from nekosrewrite import NekosRewrite

nekos = NekosRewrite()

async def main():
    result = await nekos.get_image("feet")
    print(result)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

# Get arguments
```py
from nekosrewrite import NekosRewrite

nekos = NekosRewrite()

async def main():
    result = await nekos.get_arguments()
    print(result)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

# Get endpoints
```py
from nekosrewrite import NekosRewrite

nekos = NekosRewrite()

async def main():
    result = await nekos.get_endpoints()
    print(result)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

I made this library like the original nekos.py uses requests and this can cause problems for asynchronous bots/programs, etc..
I have been programming not so long ago, if you see any shortcomings or problems, please write me, thanks :)
