from io import BytesIO
import urllib.parse
import asyncio
import argparse
import random
import json
import time
import re

from PIL import Image
import websockets
import requests

import utils.board as board
import utils.template as template
import utils.image as image



class Client():

    def __init__(self, origin_art, art, xylist):
        self.cd = 1
        self.origin_art = origin_art
        self.art = art
        self.xylist = xylist
 

    async def run(self, token, user_agent, pattern):

            wsurl = f"wss://pxls.space/ws"

            print(f"{len(self.art)}/{len(self.origin_art)} [{round(((len(self.origin_art) - len(self.art))/len(self.origin_art))*100, 2)}%], Pixel done")

            async with websockets.connect(
                wsurl,
                extra_headers=(
                    [
                        ("Cookie", f"pxls-token={token}"),
                        (
                            "User-Agent",
                            user_agent,
                        ),
                    ]
                ),
            ) as ws:

                    watch = asyncio.create_task(self.watch(ws))
                    send = asyncio.create_task(self.send(ws))
                    sort = asyncio.create_task(self.sort(pattern))

                    await asyncio.gather(watch, send, sort)


    async def sort(self, pattern):
        while True:
            self.art = sorted(self.art, key = pattern)
            await asyncio.sleep(0.5)


    async def send(self, ws):
        while True:
            await asyncio.sleep(10)
            for pixel in self.art:          
                
                message = json.dumps(
                            {
                                "type": "pixel",
                                "x": pixel[0],
                                "y": pixel[1],
                                "color": pixel[2],
                            }
                        ) 

                await ws.send(message) 
                print(f"Place on x:{pixel[0]}, y:{pixel[1]}. Wait {self.cd}")  
                await asyncio.sleep(self.cd)


    async def watch(self, ws):
        async for message in ws:
            try:
                message = json.loads(message)
            except json.decoder.JSONDecodeError:
                pass
            if message["type"] == "pixel":
                await self.on_pixel(message)
                
            elif message["type"] == "cooldown":
                await self.on_cooldown(message)
                
            elif message["type"] == "chat_message":
                await self.on_chat_message(message)

            elif message["type"] == "userinfo":
                await self.on_user_info(message)

            elif message["type"] == "alert":
                await self.on_alert(message)
    

    async def on_pixel(self, message):
        for px in range(len(message["pixels"])):
            x = message["pixels"][px]["x"]
            y = message["pixels"][px]["y"]
            c = message["pixels"][px]["color"]

            if (x, y, c) in self.art:
                await self.on_good_pixel(x, y, c)
                print(f"good pixel x:{x} y:{y}")

            if (x, y) in self.xylist and not (x, y, c) in self.origin_art:
                await self.on_bad_pixel(x, y, c) 
                print(f"bad pixel x:{x} y:{y}")


    async def on_good_pixel(self, x, y, c):
        self.art.remove((x, y, c))


    async def on_bad_pixel(self, x, y, c):
        self.art.append(
            self.origin_art[self.xylist.index((x, y))]
            )


    async def on_chat_message(self, message):
        if self.nickname in message["message"]["message_raw"]:
            print("Chat ping!")
            answer = input("Return? y/n: ")
            if answer == "y":
                return
            elif answer == "n":
                quit()
            else:
                quit()


    async def on_user_info(self, message):
        self.nickname = message["username"].lower()


    async def on_cooldown(self,message):                  
        self.cd = float(message["wait"]) + random.uniform(2.0, 3.0)


    async def on_alert(self, message):
        print(f"Admin alert!!! message: {message['message']}, sender: {message['sender']}")
        quit()

        


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Pxls.space bot')

    parser.add_argument('-t',action="store", dest="token", required=True)
    parser.add_argument('-file',action="store", dest="file")
    parser.add_argument('-x',action="store", dest="x",type=int)
    parser.add_argument('-y',action="store", dest="y",type=int)
    parser.add_argument('-p',action="store", dest="pattern", default="lbl_top")
    parser.add_argument('-ua',action="store", dest="ua", default="Mozilla/5.0 (Windows NT 7.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0 OWASMIME/4.0500")
    parser.add_argument('-link',action="store", dest="template")

    args = parser.parse_args()

    x = args.x
    y = args.y

    if not args.template == None:

        fragment = urllib.parse.urlparse(args.template).fragment
        params = dict(urllib.parse.parse_qsl(fragment))
        
        temp_image = Image.open(
            BytesIO(
                requests.get(params["template"]).content
            )
        ).convert("RGBA")
        scale = template.scale_detect(temp_image)

        if scale >= 3 and scale <= 13:
            file = template.detemplatize(temp_image, scale)
        else:
            file = temp_image
        
        x = int(params["ox"])
        y = int(params["oy"])

    if not args.file == None:
        file = Image.open(args.file)
    
    
    info = json.loads(board.get_board_info())
    origin_art = image.art2list(file, info["palette"], x, y)
    board_ = board.get_board_data()
    board_ = board.board2list(board_, info["width"], file.size, x, y)
    art = image.get_diff(origin_art, board_)
    xylist = image.art2xy(origin_art)

    module = __import__('utils.pattern', fromlist=["object"])
    class_ = getattr(module, f"Pattern")(file.size, x, y)
    mode = getattr(class_, args.pattern)

    client = Client(origin_art, art, xylist)

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(client.run(args.token, args.ua, mode))

