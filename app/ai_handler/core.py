import google.generativeai as genai
from typing import Union
from google.generativeai.types.generation_types import AsyncGenerateContentResponse as response_ai
import asyncio
from ..utils import youtube_handler
from rich.console import Console
from rich.markdown import Markdown

class AIHandler:

    def __init__(self,
                 gemini_api_key: str):
        genai.configure(api_key=gemini_api_key)
        try:
            self._model = genai.GenerativeModel('gemini-1.5-pro')
        except ValueError as e:
            print('Будет использоваться gemini-pro')
    
    async def retell_the_text(self,
                query: str) -> Union[response_ai, str]:
        try:
            response = await self._model.generate_content_async(contents=f"Тебе будет дана транскрипция текста, перескажи как можно подробнее это человеку, так же дай в конце 100 вопросов по тексту делай на русском все даже если дано на другом языке\n----------------------------- {query}")
            return response
        except Exception as e:
            return f"Error while proccesing {e}"


