from django.shortcuts import render, redirect
from .models import About
from .forms import CollaborateForm
from django.contrib import messages


def about_me(request):
    about = About.objects.all().order_by('-updated_on').first()

    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.success(request, "Thanks for reaching out! Your message has been sent.")
            return redirect("about")  # Reloads the page (prevents resubmitting)
    else:
        collaborate_form = CollaborateForm()

    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "collaborate_form": collaborate_form
        },
    )