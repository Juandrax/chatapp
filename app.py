from g4f.client import Client
import nest_asyncio
import asyncio
from asyncio import WindowsSelectorEventLoopPolicy

# Configura el event loop para evitar warnings en Windows
asyncio.set_event_loop_policy(WindowsSelectorEventLoopPolicy())
nest_asyncio.apply()

client = Client()

def get_response(messages):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response.choices[0].message.content

def main():
    messages = [{"role": "user", "content": "Hola, ¿cómo te llamas?"}]
    user_name = get_response(messages)
    print(f"Chatbot: {user_name}")

    # Asumimos que el usuario ingresa su nombre aquí, por simplicidad
    user_name = input("Tu nombre: ")

    messages = [
        {"role": "user", "content": f"Hola, {user_name}. Me gustaría aprender inglés. ¿Puedes darme tres preguntas para practicar?"}
    ]
    course_content = get_response(messages)
    print(f"Chatbot: {course_content}")

if __name__ == "__main__":
    main()
