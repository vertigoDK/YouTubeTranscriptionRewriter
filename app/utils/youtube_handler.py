import re
from youtube_transcript_api import YouTubeTranscriptApi
from rich.console import Console
from rich.markdown import Markdown
from typing import Any, List
from youtube_transcript_api.formatters import TextFormatter


class YoutubeHandler:

    def __init__(self, y_link: str, languages: List = ['ru', 'en']):
        self._y_link = y_link
        self._languages = languages
    def _get_id_from_url(self) -> str:
        pattern = r"(?<=v=)[\w-]+"
        match = re.search(pattern, self._y_link)

        return match.group(0)

    def get_subtitles(self) -> Any:
        transcript = YouTubeTranscriptApi.get_transcript(self._get_id_from_url(), self._languages)
        formatter = TextFormatter()
        text_formater = formatter.format_transcript(transcript)
        return text_formater
    

if __name__ == '__main__':
    yHandler = YoutubeHandler("https://www.youtube.com/watch?v=NNnIGh9g6fA&ab_channel=Stanford")
    console: Console = Console()

    message: str = yHandler._get_id_from_url()

    md = Markdown(message)
    console.print(md)