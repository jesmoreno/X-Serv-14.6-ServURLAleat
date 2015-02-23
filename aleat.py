#!/usr/bin/python
# -*- coding: utf-8 -*-
import webapp
import socket
import random

class servidor(webapp.webApp):

    def process(self, parsedRequest):
        numAleatorio = str(random.randrange(10000))
        nuevaPagina = "http://"+socket.gethostname()+":1234/" + numAleatorio

        return ("HTTP/1.1 200 OK\r\n\r\n",
        "<html><body><h1>URL'S ALEATORIAS</h1>" +
        "<p>Hola.<A HREF= "+ nuevaPagina +">Dame otra</A></p>" +
        "</body></html>" + "\r\n")
  
if __name__ == "__main__":
    serv = servidor(socket.gethostname(), 1234)
