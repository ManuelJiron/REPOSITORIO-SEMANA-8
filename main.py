from controllers.controlador_camiones import ControladorCamiones
import speech_recognition as sr

def reconocer_voz():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

        try:
            texto = r.recognize_google(audio, language="es-ES")
            print(f"Reconocido: {texto}")
            return texto.lower()
        except sr.UnknownValueError:
            print("No se entendió el audio.")
            return ""
        except sr.RequestError as e:
            print(f"Error del servicio de reconocimiento: {e}")
            return ""

def main():
    controlador = ControladorCamiones()
    
    while True:
        print("\nSistema de Gestión de Camiones")
        print("Diga una opción:")
        print("1. Registrar camión")
        print("2. Mostrar cola")
        print("3. Descargar camión")
        print("4. Salir")

        opcion = reconocer_voz()

        if "uno" in opcion or "1" in opcion:
            print("Diga el número de placa:")
            numero_placa = reconocer_voz()

            print("Diga el nombre del conductor:")
            nombre_conductor = reconocer_voz()

            print("Diga la empresa de origen:")
            empresa = reconocer_voz()

            print(controlador.registrar_camion(numero_placa, nombre_conductor, empresa))

        elif "dos" in opcion or "2" in opcion:
            print("\nCola de camiones:")
            print(controlador.mostrar_cola())

        elif "tres" in opcion or "3" in opcion:
            print(controlador.descargar_camion())

        elif "cuatro" in opcion or "4" in opcion or "salir" in opcion:
            print("Saliendo del sistema...")
            break

        else:
            print("No se reconoció una opción válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
