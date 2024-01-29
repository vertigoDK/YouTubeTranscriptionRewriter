import os
from openai import OpenAI


class TextParaphraser:
    __answerLong = 700

    
    def __init__(self) -> None:
        self.__OPENAI_API = os.getenv('API_KEY')

        

    @property
    def answerLong(cls):
        return cls.__answerLong
    
    @answerLong.setter
    def answerLong(cls, value: int):
        if value <= 50 or value >= 300:
            print("Значение должно быть больше 50 и меньше 300")
            return
        cls.__answerLong = value

    def gpt_paraphraser(self, paraphrase_sentence: list[str]):
        all_part_paraphrase = []
        
        for sentence in paraphrase_sentence:
            result_paraphrase = self.__gpt_paraphraser_part(sentence_part=sentence)
            all_part_paraphrase.append(result_paraphrase)
            print(f"текущий общий парт: {all_part_paraphrase}")
        result = self.__combine_paraphrases(all_part_paraphrase)
        return result
        
    def __gpt_paraphraser_part(self, sentence_part: str):
        try:
            client = OpenAI(api_key=self.__OPENAI_API)
            print(f'Началась обработка парта: {sentence_part}\n\n\n\n\n\n')
            response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{
                
                "role": "system", "content": f"Ты делаешь пересказ видео на ютубе от 3 лица НА ЯЗЫКЕ РУССКИЙ ДО {self.answerLong} СЛОВ вот как это будет выглядеть:"
                "user: {Тут текст}"
                "assistant: {Твой краткий пересказ}",
                "role": "assistant", "content": "Я понял.",
                "role": "user", "content": f"Вот текст: {sentence_part}",
                
                }],
            )
            print('Закончилась обработка парта\n\n\n\n\n\n')
            a = response.choices[0].message
            response = a.content
            return response
        except Exception as e:
            print(f'Возникла ошибка при попытке получить доступ к CHATGPT, попробуйте позднее. Ошибка: {e}') 
            return 

    def __combine_paraphrases(self, all_part_paraphrase: list[str]):
        try:
            client = OpenAI(api_key=self.__OPENAI_API)
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Объединяй по смыслу весь текст, который тебе передадут"},
                    {"role": "user", "content": f"Вот текст: {all_part_paraphrase}"},
                ]
            )
            combined_text = response.choices[0].message.content
            return combined_text
        except Exception as e:
            print(f'Возникла ошибка при попытке получить доступ к CHATGPT, попробуйте позднее. Ошибка: {e}') 
            return None