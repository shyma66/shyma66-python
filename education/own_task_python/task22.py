import openai

# Установите свой API-ключ
openai.api_key = 'asst_h5ANRhtMbRqXUlHT1UIJgo5I'

# Пример запроса к GPT-3
response = openai.Completion.create(
  engine="text-davinci-002",
  prompt="Translate the following English text to French: '{}'",
  max_tokens=60
)

# Выведите результат
print(response.choices[0].text.strip())