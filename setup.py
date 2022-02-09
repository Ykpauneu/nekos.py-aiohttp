from distutils.core import setup
setup(
    name='nekosrewrite',
    author='Ykpauneu',
    author_email="mestodan230@gmail.com",
    url="https://github.com/Ykpauneu/nekos.py-aiohttp",
    download_url="https://github.com/Ykpauneu/nekos.py-aiohttp/archive/refs/tags/1.0.3.tar.gz",
    version="1.0.3",
    packages=["nekosrewrite"],
    license="GNU v3",
    description="Python module that uses Nekos API via aiohttp",
    install_requires=['aiohttp', 'asyncio']
)
