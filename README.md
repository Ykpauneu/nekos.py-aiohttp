# nekosrewrite
Python module that uses Nekos API via aiohttp

# Requirements
- asyncio
- aiohttp

# NSFW example:
```py
import nekosrewrite
async def main():
    result = await nekosrewrite.main("feet")
    print(result)
```
# NSFW example with args
```py
import nekosrewrite
async def main(arg1):
    result = await nekosrewrite.main(arg1)
    print(result)
```
# If you need to get list of possible NSFW args, use:
```py
import nekosrewrite
async def main():
    await nekosrewrite.possible_args()
>>> returns list
```
I made this library like the original nekos.py uses requests and this can cause problems for asynchronous bots/programs, etc..
I have been programming not so long ago, if you see any shortcomings or problems, please write me, thanks :)
