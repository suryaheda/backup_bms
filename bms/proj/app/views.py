import os
from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from .forms import QuestionForm
from .rag_model import create_rag_app

# Replace with your PDF path
pdf_path = "app/co.pdf"  # Ensure this path is correct

# Initialize the RAG application with the specified PDF document
rag_app = create_rag_app(pdf_path)

def chat_view(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.cleaned_data["question"]
            # Use the RAG app to get an answer
            answer = rag_app.run(question)
            return JsonResponse({"answer": answer})
    else:
        form = QuestionForm()

    return render(request, "chat.html", {"form": form})

def home(request):
    return render(request, "home.html")