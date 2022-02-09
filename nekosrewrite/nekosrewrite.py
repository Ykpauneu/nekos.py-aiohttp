import asyncio
import aiohttp

class NekosRewrite():
	def __init__(self):
		self.BASE_URL = "https://nekos.life/api/v2/img/"
		self.BASE_ENDPOINTS = "https://nekos.life/api/v2/endpoints"
		self.POSSIBLE_NSFW = ['solog', 'smug', 'feet', 'smallboobs', 'lewdkemo', 'woof', 'gasm', 'solo', '8ball', 'goose', 'cuddle', 'avatar', 'cum', 'slap', 'les', 'v3', 'erokemo', 'bj', 'pwankg', 'nekoapi_v3.1', 'ero', 'hololewd', 'pat', 'gecg', 'holo', 'poke', 'feed', 'fox_girl', 'tits', 'nsfw_neko_gif', 'eroyuri', 'holoero', 'pussy', 'Random_hentai_gif', 'lizard', 'yuri', 'keta', 'neko', 'hentai', 'feetg', 'eron', 'erok', 'baka', 'kemonomimi', 'hug', 'cum_jpg', 'nsfw_avatar', 'erofeet', 'meow', 'kiss', 'wallpaper', 'tickle', 'blowjob', 'spank', 'kuni', 'classic', 'waifu', 'femdom', 'boobs', 'trap', 'lewd', 'pussy_jpg', 'anal', 'futanari', 'ngif', 'lewdk']

	async def get_arguments(self):
		return self.POSSIBLE_NSFW

	async def get_image(self, image_arg:str=None):
		try:
			async with aiohttp.ClientSession() as session:
				async with session.get(f"{self.BASE_URL}{image_arg.lower()}") as response:
					result = await response.json()
						
				return(result["url"])
		except:
			return "nekosrewrite: API problem."    

	async def get_endpoints(self):
		try:
			async with aiohttp.ClientSession() as session:
				async with session.get(f"{self.BASE_ENDPOINTS}") as response:
					result = await response.json()
				
				return(result)
		except:
			return "nekosrewrite: API problem."    