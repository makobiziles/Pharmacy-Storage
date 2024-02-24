from django.views import View
from django.shortcuts import render, redirect
from .models import Image
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm


class IndexView(View):
  def get(self, request):
    # Get all images from the database 
    # and sort them by uploaded_date
    images = Image.objects.order_by("uploaded_date")
    return render(
      request,
      # render giffy_app/index.html and return it in the response
      "Pharmapics/index.html",
      # pass images we fetched earlier to the template
      {
        "images": images,
      },
    )
  

class SignUpView(View):
  def get(self, request):
    # Render giffy_app/signup.html with 
    # UserCreationForm upon page load
    return render(
      request,
      "Pharmapics/signup.html",
      {
        "form": UserCreationForm(),
      },
    )

  def post(self, request):
    # Validate form, create user, and login 
    # upon sign-up form submission
    form = UserCreationForm(request.POST)

    # If user credentials are valid
    if form.is_valid():
      # create a new user in the database
      form.save()

      # get username and password from form
      username = form.data["username"]
      password = form.data["password1"]

      # authenticate user using credentials
      # submited in the UserCreationForm
      user = authenticate(
        request,
        username=username,
        password=password,
      )

      if user:
        # login user
        login(request, user)

      # redirect user to index page
      return redirect("/")

    # if form is not valid, re-render the template
    # showing the validation error messages
    return render(
      request,
      "Pharmapics/signup.html",
      {
        "form": form,
      },
    )