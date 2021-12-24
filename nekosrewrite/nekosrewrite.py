import asyncio
import aiohttp

possible_nswf = [
'solog', 'smug', 'feet', 'smallboobs', 'lewdkemo', 'woof', 'gasm', 'solo', '8ball', 'goose', 'cuddle', 'avatar', 'cum', 'slap', 'les', 'v3', 'erokemo', 'bj', 'pwankg', 'nekoapi_v3.1', 'ero', 'hololewd', 'pat', 'gecg', 'holo', 'poke', 'feed', 'fox_girl', 'tits', 'nsfw_neko_gif', 'eroyuri', 'holoero', 'pussy', 'Random_hentai_gif', 'lizard', 'yuri', 'keta', 'neko', 'hentai', 'feetg', 'eron', 'erok', 'baka', 'kemonomimi', 'hug', 'cum_jpg', 'nsfw_avatar', 'erofeet', 'meow', 'kiss', 'wallpaper', 'tickle', 'blowjob', 'spank', 'kuni', 'classic', 'waifu', 'femdom', 'boobs', 'trap', 'lewd', 'pussy_jpg', 'anal', 'futanari', 'ngif', 'lewdk'
]

async def possible_args():
    print(f"nekosrewrite: \n{possible_nswf}")

async def main(user_req:str):
    if user_req not in possible_nswf:
        print(f"nekosrewrite: Caused an error in the function, use tags:{possible_nswf}")
    if user_req is None:
        print(f"nekosrewrite: Cause an error in the function, user_req must not be None")
    else:
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://nekos.life/api/v2/img/{user_req}") as r:
                res = await r.json()
                return(res["url"])

async def get_endpoints():
    async with aiohttp.ClientSession() as cs:
        async with cs.get(f"https://nekos.life/api/v2/endpoints") as r:
            res = await r.json()
            return(res)
