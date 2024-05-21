# -*- coding: utf-8 -*-

import pyautogui, webbrowser
import pygetwindow as gw
import pyperclip #Para copiar y pegar mensaje
from time import sleep
import socket

def buscar_ventana_whatsapp():
	webbrowser.open_new_tab("https://web.whatsapp.com/")
	# Buscar la ventana de WhatsApp por su título
	for ventana in gw.getAllTitles():
		print(ventana)
		if "WhatsApp" in ventana:
			return ventana
	return None

def enviarMensaje(numero, mensaje):
	ventana_whatsapp = buscar_ventana_whatsapp()
	if ventana_whatsapp:
		# Enfocar la ventana de WhatsApp Web
		pyautogui.getWindowsWithTitle(ventana_whatsapp)[0].activate()
		sleep(2)
		buscar_user = pyautogui.locateCenterOnScreen('buscarusuario.png', confidence=0.8)
		if buscar_user is not None:
			pyautogui.click(buscar_user)
			sleep(1)
			pyautogui.typewrite(numero)
			pyautogui.press("enter")
			print("MENSAJE:", mensaje)
			entrada_texto = pyautogui.locateCenterOnScreen('entradatexto.png', confidence=0.8)
			if entrada_texto is not None:
				pyautogui.click(entrada_texto)
				sleep(1)
				pyperclip.copy(mensaje)
				pyautogui.hotkey("ctrl", "v")
				sleep(1)
				pyautogui.press("enter")
			else:
				print("No se encontró la barra de entrada de texto.")
		else:
			print("No se encontro la barra para buscar usuarios")
	else:
		print("No se encontró la ventana de WhatsApp Web.")

def esperar_inputs(host, port):
    # Crear un socket TCP/IP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
        # Enlazar el socket a la dirección y puerto especificados
        servidor.bind((host, port))
        # Escuchar por conexiones entrantes
        servidor.listen()

        print(f"Servidor escuchando en {host}:{port}")
        while True:  # Bucle infinito para seguir aceptando conexiones
            conexion, direccion = servidor.accept()
            print(f"Conexión entrante desde {direccion}")

            while True:  # Bucle infinito para recibir múltiples mensajes de un cliente
                datos = conexion.recv(1024)
                if not datos:
                    break  # Salir del bucle interno si no hay más datos
                # Decodificar los datos y procesarlos
                numero, mensaje = datos.decode().split("|")
                print("Número recibido:", numero)
                print("Mensaje recibido:", mensaje)
                sleep(3)
                enviarMensaje(numero, mensaje)

            print("Cliente desconectado")
        # Aceptar conexiones entrantes
    
            
    
if __name__ == "__main__":
    # Configurar la dirección y puerto en el que el servidor escuchará
    HOST = '127.0.0.1'  # localhost
    PORT = 65432  # Puerto no privilegiado (> 1023)

    esperar_inputs(HOST, PORT)
