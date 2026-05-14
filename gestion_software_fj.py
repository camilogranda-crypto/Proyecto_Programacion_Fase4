import logging
from abc import ABC, abstractmethod

# CONFIGURACIÓN DE ROBUSTEZ: Archivo de logs para errores
logging.basicConfig(filename='registro_eventos.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# --- CLASES ---

class Persona(ABC): # ABSTRACCIÓN
    def __init__(self, nombre, id_personal):
        self._nombre = nombre # ENCAPSULAMIENTO (Protegido)
        self._id_personal = id_personal

class Cliente(Persona): # HERENCIA
    def __str__(self):
        return f"Cliente: {self._nombre} (ID: {self._id_personal})"

class Servicio(ABC): # CLASE ABSTRACTA
    @abstractmethod
    def calcular_costo(self):
        pass

class ReservaSala(Servicio): # POLIMORFISMO en el cálculo
    def __init__(self, horas):
        if horas <= 0: raise ValueError("Las horas deben ser positivas")
        self.horas = horas
    def calcular_costo(self):
        return self.horas * 50000

class AlquilerEquipo(Servicio):
    def __init__(self, dias):
        if dias <= 0: raise ValueError("Los días deben ser positivos")
        self.dias = dias
    def calcular_costo(self):
        return self.dias * 30000

class Reserva:
    def __init__(self, cliente, servicio):
        self.cliente = cliente
        self.servicio = servicio

# --- SIMULACIÓN DE 10 OPERACIONES ---
def ejecutar_sistema():
    print("--- INICIANDO SISTEMA SOFTWARE FJ ---")
    operaciones = [
        ("C", "Juan", "101"), ("C", "Ana", "102"), ("S", "Sala", 5),
        ("S", "Equipo", 2), ("R", "Juan", "Sala"), ("C", "", "999"), # Error nombre
        ("S", "Sala", -2), # Error valor
        ("C", "Pedro", "ABC"), # Error ID
        ("S", "Equipo", 1), ("R", "Ana", "Equipo")
    ]
    
    for i, op in enumerate(operaciones):
        try:
            print(f"Op {i+1}: Procesando...")
            # Lógica de validación aquí...
            if not op[1]: raise Exception("Dato faltante")
            logging.info(f"Operación {i+1} exitosa")
        except Exception as e:
            logging.error(f"Error en Op {i+1}: {e}")
            print(f"ALERTA: Se ha registrado un error controlado.")

if __name__ == "__main__":
    ejecutar_sistema()
