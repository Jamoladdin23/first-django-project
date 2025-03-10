from django.http import JsonResponse
import openai
from django.shortcuts import render
from dotenv import load_dotenv
import os


load_dotenv()

def chat_with_gpt(request):
    user_input = request.GET.get('user_input')

    if not user_input:
        return JsonResponse({"response": "request cannot be empty"})

    openai.api_key = os.getenv('OPENAI_API_KEY')

    messages = [{'role': 'user', 'content': user_input}]

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                            messages=messages,
                                            temperature=0.5,
                                            max_tokens=1000
                                            )

    chat_response = response['choices'][0]['message']['content']
    return JsonResponse({'response': chat_response})


def consult(request):
    return render(request, 'consult.html')
