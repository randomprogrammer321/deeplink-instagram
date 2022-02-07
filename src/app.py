from fastapi import FastAPI, Header
from fastapi.responses import RedirectResponse
import re


from user_agents import parse 

app = FastAPI()


@app.get("/instagram/{link}")
async def read_items(link: str ,*, user_agent: str = Header(None)):
    
    agent = parse(user_agent)
    
    redi_link = agent.get_os()

    
   
    
    if (agent.is_mobile):

        if (redi_link.find("iOS") == 0):
       
            return RedirectResponse(url=f"instagram://user?username={link}")
        elif (redi_link.find("Android")== 0 ):
            return  RedirectResponse(url=f"intent://instagram.com/_u/{link}/#Intent;package=com.instagram.android;scheme=https;end")
    
    else:
        return RedirectResponse(url=f"https://instagram.com/{link}")


@app.get("/twitter/{link}")
async def read_items(link: str ,*, user_agent: str = Header(None)):
    
    agent = parse(user_agent)
    
    redi_link = agent.get_os()

    
   
    
    if (agent.is_mobile):

        if (redi_link.find("iOS") == 0):
       
            return RedirectResponse(url=f"twitter://user?screen_name={link}")
        elif (redi_link.find("Android")== 0 ):
            return  RedirectResponse(url=f"intent://twitter.com/{link}#Intent;package=com.twitter.android;scheme=https;end")
    
    else:
        return RedirectResponse(url=f"https://twitter.com/{link}")
