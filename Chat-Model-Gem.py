from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model

model = init_chat_model(
    "gemini-3.5-flash-lite",
    model_provider="google_genai"
)

user_input = input("You: ")

response = model.invoke(user_input)

print("AI:", response.content)