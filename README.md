# nekosrewrite
Python module that uses Nekos API via aiohttp
# Install:
```
>>> pip install nekosrewrite
```
# Requirements
- aiohttp

# Example:
```py
from nekosrewrite import NekosRewrite

async def main():
    result = await NekosRewrite.get_image("feet")
    print(result)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

# Get arguments
```py
from nekosrewrite import NekosRewrite

async def main():
    result = await NekosRewrite.get_arguments()
    print(result)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

# Get endpoints
```py
from nekosrewrite import NekosRewrite

async def main():
    result = await NekosRewrite.get_endpoints()
    print(result)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```