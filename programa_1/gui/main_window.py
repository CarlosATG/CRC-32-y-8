"""
Múdlo que define la clase MainWindow que representa la ventana principal de la
aplicación.
"""
import re
import string

from tkinter import Frame, Button, Label, Entry, StringVar, Tk
from tkinter.ttk import Combobox
from utility.functions import  CRC #calculate_crc,

class MainWindow(Frame):
    """
    Clase que represernta la ventana principal de la aplicación.
    """

    def __init__(self, master: Tk) -> None:
        """
        Constructor de la clase MainWindow.

        Args:
            master: La ventana principal de Tkinter.
        """
        super().__init__(master)
        self.master = master
        self.text = StringVar()
        self.crc_type = StringVar()
        self.init_vector = StringVar()
        self.pack()
        self.create_widgets()

    def create_widgets(self) -> None:
        """
        Crea y configura los widgets de la ventana principal.
        """
        label_string = Label(self, text="Cadena de texto(32 caracteres ASCII):")
        label_string.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        entry_string = Entry(self,
            width=35,
            textvariable=self.text,
            validate="key",
            validatecommand=(self.register(self.validate_text), "%P"),
            )
        entry_string.grid(row=0, column=1, padx=10, pady=10)

        label_crc_type = Label(self, text="Tipo de CRC:")
        label_crc_type.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        combobox_crc_type = Combobox(self,
            width=8,
            state="readonly",
            values=["CRC-8", "CRC-32"],
            textvariable=self.crc_type,
            )
        combobox_crc_type.current(0)  # Establecer el valor predeterminado
        combobox_crc_type.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        combobox_crc_type.bind("<<ComboboxSelected>>", self.update_init_vector)

        label_init_vector = Label(self, text="Vector de inicialización:")
        label_init_vector.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        entry_init_vector = Entry(self,
            width=35,
            text = "00000000",
            textvariable=self.init_vector,
            validate="key",
            validatecommand=(self.register(self.validate_init_vector), "%P"),
            )
        entry_init_vector.grid(row=2, column=1, padx=10, pady=10)

        button_calculate = Button(self, text="Calcular CRC", command=self.calculate_crc)
        button_calculate.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.label_result_crc = Label(self, text="CRC calculado:")
        self.label_result_crc.grid(row=4, column=0, padx=10, pady=10, sticky="w")

        self.label_result_encoded = Label(self, text="Mensaje codificado:")
        self.label_result_encoded.grid(row=5, column=0, padx=10, pady=10, sticky="w")

        # Establecer el valor por defecto del campo de vector de inicialización
        self.update_init_vector()

    def validate_text(self, input_text: str) -> bool:
        """Valida el texto de entrada para limitarlo a 32 caracteres ASCII"""
        if len(input_text) > 32:
            return False

        if any(char not in string.printable for char in input_text):
            return False

        return True


    def validate_init_vector(self, new_value: str) -> bool:
        """Valida el vector de inicialización"""
        crc_type = self.crc_type.get()
        init_vector = new_value

        if crc_type == "CRC-8":
            max_length = 8
        elif crc_type == "CRC-32":
            max_length = 32
        # else:
        #     return False

        # Verificar que el vector de inicialización tenga solo 1s y 0s
        if re.match(r"^[01]*$", init_vector):
            # Verificar que el vector de inicialización no exceda la longitud máxima
            if len(init_vector) <= max_length:
                return True

        return False


    def update_init_vector(self, event=None) -> None:
        """Actualiza el valor por defecto del campo de vector de inicialización"""
        crc_type = self.crc_type.get()
        if crc_type == "CRC-8":
            self.init_vector.set("0"*8)
        elif crc_type == "CRC-32":
            self.init_vector.set("0"*32)


    def calculate_crc(self) -> None:
        """Calcula el CRC y muestra los resultados."""
        c=CRC()
        text = self.text.get()
        crc_type = self.crc_type.get()
        init_vector = self.init_vector.get()
        binario = ''.join(format(i, '08b') for i in bytearray(text, encoding='utf-8'))
        if crc_type == "CRC-8":
            polinomio = "110100111"
        else:
            polinomio= "100000100110000010001110110110111"
        crc_result, encoded_result=c.encodedData(binario, polinomio, init_vector)
        # TODO: Aquí se implementa la lógica para calcular el CRC de acuerdo a
        # los parámetros ingresados. Esto debe ser implementado en otro modulo
        # de Python. Una vez completado hay que borrar este bloque TODO: FIN del bloque
        # Invocación de la lógica.
        #crc_result, encoded_result = calculate_crc(text, crc_type, init_vector)
        
        # # DEBUG:
        # print(string_var)
        # print(crc_type)
        # print(init_vector)
        # print(crc_result, encoded_result)
        # # DEBUG: FIN del bloque

        # Mostrar los resultados
        self.label_result_crc.config(text="CRC calculado: " + crc_result)
        self.label_result_encoded.config(text="Mensaje codificado: " + encoded_result)
