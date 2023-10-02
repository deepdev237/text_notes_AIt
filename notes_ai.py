import os
import openai

openai.organization = ""
openai.api_key = ""
openai.Model.list()

print("program started")

f = open("text1.txt", "r", encoding='utf-8')
text1 = f.read()

f = open("text2.txt", "r", encoding='utf-8')
text2 = f.read()

f = open("text3.txt", "r", encoding='utf-8')
text3 = f.read()

context = """
This is the text of an educative PDF about databases in hungarian.
Take notes like a student on the text.
Write in hungarian. Include datamodels and some examples.
"""
chat_completion = openai.ChatCompletion.create(model="gpt-4", messages=[{"role": "user", "content": f"{text1}\n \n{context}"}])

f = open("result.txt", "a", encoding='utf-8')
f.write(chat_completion.choices[0].message.content)

chat_completion = openai.ChatCompletion.create(model="gpt-4", messages=[{"role": "user", "content": f"{text2}\n \n{context}"}])

f = open("result.txt", "a", encoding='utf-8')
f.write(chat_completion.choices[0].message.content)

chat_completion = openai.ChatCompletion.create(model="gpt-4", messages=[{"role": "user", "content": f"{text3}\n \n{context}"}])

f = open("result.txt", "a", encoding='utf-8')
f.write(chat_completion.choices[0].message.content)

f.close()
