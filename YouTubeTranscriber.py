from youtube_transcript_api import YouTubeTranscriptApi
from SentenceDivider import SentenceDivider
from TextParaphraser import TextParaphraser
class YouTubeTranscriber:
    def __init__(self, language=['ru']) -> None:
        self.__language = language
        self.__max_lenght = 30000

    def __extract_id_from_url(self, url):
        if "=" in url:
            video_id = url.split("=")[-1]
            return video_id
        else:
            return None

    def __extract_text_from_id(self, id: str):
        try:
            srt = YouTubeTranscriptApi.get_transcript(id, 
                languages=self.__language)
            text_combined = ' '.join(item.get('text', '') for item in srt)
            print(len(f"Длина видео {text_combined}"))
            if len(text_combined) > self.__max_lenght:
                print('Слишком много слов в видео')
                return None
            return text_combined
        except Exception as e:
            print(f'Возникла ошибка {e}')
            return None

    def paraphrase_sentences(self, url: str):
        url_id = self.__extract_id_from_url(url)
        if url_id == None:
            return None
        video_text = self.__extract_text_from_id(url_id)
        sDriver = SentenceDivider()
        video_spliter_text = sDriver.split_sentence(video_text)
        tParaphraser = TextParaphraser()

        result = tParaphraser.gpt_paraphraser(video_spliter_text)
        return result
        


        
        

    
a = YouTubeTranscriber()
result = a.paraphrase_sentences("https://www.youtube.com/watch?v=kwS7HupJhYo")
print(result)