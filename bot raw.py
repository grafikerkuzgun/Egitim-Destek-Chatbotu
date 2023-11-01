import openai

# Kullanıcıdan OpenAI API anahtarını al
api_key = input("Lütfen OpenAI API anahtarınızı girin: ")

# OpenAI API anahtarını ayarla
openai.api_key = api_key

while True:
    soru = input("Soru: ")

    # OpenAI API'sini kullanarak soruya cevap al
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=soru + "\n",
        max_tokens=150  # Chatbot yanıtının maksimum uzunluğu
    )
    cevap = response.choices[0].text.strip()

    print("Cevap: " + cevap)

    devam_et = input("Başka bir soru sormak istiyor musunuz? (Evet/Hayır): ")
    if devam_et.lower() != "evet":
        break

