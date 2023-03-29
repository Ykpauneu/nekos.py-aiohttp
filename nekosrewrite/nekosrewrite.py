import aiohttp
from .consts import BASE_URL, BASE_ENDPOINTS, POSSIBLE_NSFW
from .exceptions import NoResponse


class NekosRewrite:
    @classmethod
    async def get_arguments(cls):
        return self.POSSIBLE_NSFW

    @classmethod
    async def get_image(self, image_arg: str = None):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(
                    f"{self.BASE_URL}{image_arg.lower()}"
                ) as response:
                    result = await response.json()

                return result["url"]
        except:
            return NoResponse("nekosrewrite: Couldn't get a response")

    async def get_endpoints(self):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"{self.BASE_ENDPOINTS}") as response:
                    result = await response.json()

                return result
        except:
            return NoResponse("nekosrewrite: Couldn't get a response")
