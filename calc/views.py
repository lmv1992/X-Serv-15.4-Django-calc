from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def sumar(request, num1, num2):
	suma = int(num1) + int(num2)
	return HttpResponse("<b><h1>La suma de "
						+ str(num1) + " + "
						+ str(num2) + " es "
						+ '<font color="blue">' + str(suma) + '</font>'
						+"</h1></b>")
						
def restar(request, num1, num2):
	resta = int(num1) - int(num2)
	return HttpResponse("<b><h1>La suma de "
						+ str(num1) + " - "
						+ str(num2) + " es "
						+ '<font color="blue">' + str(resta) + '</font>'
						+"</h1></b>")

def multiplicar(request, num1, num2):
	multiplicacion = int(num1) * int(num2)
	return HttpResponse("<b><h1>La multiplicacion de "
						+ str(num1) + " * "
						+ str(num2) + " es "
						+ '<font color="blue">' + str(multiplicacion) + '</font>'
						+"</h1></b>")

def dividir(request, num1, num2):
	division = int(num1) / int(num2)
	return HttpResponse("<b><h1>La division de "
						+ str(num1) + " / "
						+ str(num2) + " es "
						+ '<font color="blue">' + str(division) + '</font>'
						+"</h1></b>")

def error(request):
	return HttpResponse('<b><h1><font color="yellow">Pagina no encontrada</font></h1></b>')
