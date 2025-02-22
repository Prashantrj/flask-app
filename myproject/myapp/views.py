from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import os
import datetime
import subprocess

def htop(request):
    name = "Prashant"
    username = os.getenv("USER", os.getenv("USERNAME", "Unknown"))
    server_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S IST")
    top_output = subprocess.getoutput("top -b -n 1")

    response = f"""
    <h1>Name: {name}</h1>
    <h2>Username: {username}</h2>
    <h3>Server Time: {server_time}</h3>
    <pre>{top_output}</pre>
    """
    return HttpResponse(response)

