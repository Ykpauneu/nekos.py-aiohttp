# nekosrewrite
Python module that uses Nekos API via aiohttp
# Install:
```
pip install nekosrewrite
```
# Requirements
- asyncio
- aiohttp
# NSFW example:
```py
import nekosrewrite
async def main():
    result = await nekosrewrite.main("feet")
    print(result)
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```
# NSFW example with args
```py
import nekosrewrite
async def main(arg1):
    result = await nekosrewrite.main(arg1)
    print(result)
loop = asyncio.get_event_loop()
loop.run_until_complete(main(arg1))
```
# If you need to get list of possible NSFW args, use:
```py
import nekosrewrite
async def main():
    await nekosrewrite.possible_args()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```
I made this library like the original nekos.py uses requests and this can cause problems for asynchronous bots/programs, etc..
I have been programming not so long ago, if you see any shortcomings or problems, please write me, thanks :)
