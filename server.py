import asyncio
from fastapi import FastAPI
from dotenv import load_dotenv

from app.ai_handler import core
from app.utils import youtube_handler as yh

from rich.console import Console
from rich.markdown import Markdown

app = FastAPI()

@app.post('/retell-text/')
async def retell_text(url: str):
    import os
    load_dotenv()

    yHandler: yh.YoutubeHandler = yh.YoutubeHandler(url)
    subtitles = yHandler.get_subtitles()
    

    aiHandler = core.AIHandler(os.getenv("GOOGLE_API_KEY"))
    response = await aiHandler.retell_the_text(subtitles)

    return {"result": response.text}

async def main():
    import os
    load_dotenv()

    yHandler: yh.YoutubeHandler = yh.YoutubeHandler("https://www.youtube.com/watch?v=y7169jEvb-Y&ab_channel=ErrichtoAlgorithms")
    subtitles = yHandler.get_subtitles()
    

    aiHandler = core.AIHandler(os.getenv("GOOGLE_API_KEY"))
    response = await aiHandler.retell_the_text(subtitles)


    console = Console()
    md = Markdown(response.text)

    console.print(md)
if __name__ == '__main__':
    asyncio.run(main())