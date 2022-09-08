"""
myproxy = lazy_import('proxy_private')

proxies = {
"http://": myproxy.HTTP_PROXY,
"https://": myproxy.HTTPS_PROXY,
}

async with httpx.AsyncClient(proxies=proxies):

    print(proxies)
    # {'http://': 'http://proxy-web.micron.com:80', 
    #  'https://': 'http://proxy-web.micron.com:80'}    
"""

import httpx
import os
import sys
import importlib


def lazy_import(name, relative_path="../../../private/"):
    """lazy import """
    dirname = os.path.dirname(__file__)
    module_path = os.path.realpath(os.path.join(dirname, relative_path))
    spec = importlib.util.spec_from_file_location(name, module_path+'/'+name+'.py')
    loader = importlib.util.LazyLoader(spec.loader)
    spec.loader = loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    loader.exec_module(module)
    return module

async def get_movie(title_subtext: str):
    
    # this does not work with https
    url=f'https://movieservice.talkpython.fm/api/search/{title_subtext}'
    

    async with httpx.AsyncClient() as client:
        resp: httpx.Response = await client.get(url)

        print(resp, resp.text)
