from openai import OpenAI
from config import API_KEY

client = OpenAI(api_key=API_KEY)


completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Объединяй по смыслу весь текст, который тебе передадут в виде:"},
        {"role": "user", "content": f"part1: {all_part_paraphrase} part2: {all_part_paraphrase}"},
        {"role": "assistant", "content": "Я понял."}
    ]
)

a = completion.choices[0].message
print(a.content)
