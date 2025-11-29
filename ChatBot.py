import google.generativeai as genai

key = "AIzaSyAVvHgExBe8_KtA8iLIn3F3N8NpNyo5ZlA"
print(key)
genai.configure(api_key=key)
Model = genai.GenerativeModel("gemini-2.5-pro")
while True:
    user = input("How can I help you today :\nType '.' to close: ")

    if user.lower() == ".":
        print("Byy!")
        break

    response = Model.generate_content(user)
    print("bot:", response.text)