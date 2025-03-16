import asyncio
import os
import json

class JSONManager():

    def __init__(self, servers):
        self.locks = {}
        
        # prevent race conditions
        for server in servers:
            self.locks[server] = asyncio.Lock()
    
    #TODO: Idk do something with this ig
    async def create_json_file(self, server: int):
        async with self.locks[server]:
            pass

    async def get_json_file(self, server: int):
        # check if the file exists yet
        if json_file_exists(build_json_filename(server)):
            with open(build_json_filename(server), "r", encoding="utf-8") as f:
                return json.load(f)
        else:
            # make sure directories exist
            os.makedirs(os.path.dirname(build_json_filename(server)), exist_ok=True)
            await self.modify_json_file(server, {})
            return {}
    
    # provided a python dictionary convert and save it to provided file 
    async def modify_json_file(self, server: int, data: dict):
        async with self.locks[server]:
            with open(build_json_filename(server), "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
    
# check if the servers json file exists
def json_file_exists(server: int) -> bool:
    return os.path.exists(f"data/{server}.json")

# build json file name
def build_json_filename(server: int) -> str: 
    return f"data/{server}.json"
