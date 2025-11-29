import google.generativeai as genai

key = "" #enter your Key.
print(key)
genai.configure(api_key=key)
Model = genai.GenerativeModel("gemini-2.5-pro")
while True:
    user = input("What do you want To Search\nType '.' to close: ")

    if user.lower() == ".":
        print("Byyyy!")
        break

    response = Model.generate_content(user)
    print("bot:", response.text)