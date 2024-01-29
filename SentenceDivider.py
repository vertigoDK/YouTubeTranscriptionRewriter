class SentenceDivider:
    def __init__(self, max_length=3000) -> None:
        self.__max_lenght = max_length

    def split_sentence(self, sentence):
        """
        Разбивает предложение на подпредложения с длиной не более max_length символов.

        Args:
        - sentence (str): Исходное предложение.
        - max_length (int): Максимальная длина каждого подпредложения.

        Returns:
        - list: Список подпредложений.
        """
        if len(sentence) < self.__max_lenght:
            return [sentence]
        
        sub_sentences = []
        current_sub_sentence = ""

        for word in sentence.split():
            if len(current_sub_sentence) + len(word) + 1 <= self.__max_lenght:
                current_sub_sentence += " " + word
            else:
                sub_sentences.append(current_sub_sentence.strip())
                current_sub_sentence = word

        if current_sub_sentence:
            sub_sentences.append(current_sub_sentence.strip())
        print(f"Видео разбито на {len(sub_sentences)} частей")
        return sub_sentences
