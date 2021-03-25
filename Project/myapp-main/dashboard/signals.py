from django.dispatch import Signal,receiver
from django.shortcuts import render,redirect

notification = Signal(providing_args=["request", "user"])