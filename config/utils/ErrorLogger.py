import logging
import os
import sys

class ErrorLogger:
    """ 
    Sistema centralizado de Logs para capturar errores de la aplicación.
    Patrón Singleton para asegurar un único archivo y manejador.
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.__setup_logger()
        return cls._instance

    def __setup_logger(self):
        """ Configura el manejador de logs y el archivo de salida """
        # Crea directorio de logs si no existe
        if not os.path.exists('logs'):
            os.makedirs('logs')

        # Configura el logger principal
        self.logger = logging.getLogger("SGIC_Logger")
        self.logger.setLevel(logging.ERROR) # Solo capturar ERROR y CRITICAL

        # Configura el archivo de salida
        log_file = os.path.join('logs', 'app_errors.log')
        file_handler = logging.FileHandler(log_file, encoding='utf-8')

        # Define el formato del log (Fecha - Nivel - Mensaje - Archivo/Línea)
        formato = logging.Formatter(
            '%(asctime)s | %(levelname)s | Archivo: %(filename)s (Línea %(lineno)d) | %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        file_handler.setFormatter(formato)

        # Añade el manejador al logger
        # Evita duplicar handlers si la instancia se recarga
        if not self.logger.hasHandlers():
            self.logger.addHandler(file_handler)

    def log_error(self, mensaje: str, exception: Exception = None):
        """
        Método para registrar un error explícito.
        :param mensaje: Descripción personalizada del error.
        :param exception: Objeto de la excepción (para imprimir el traceback).
        """
        if exception:
            # exc_info=True adjunta toda la traza del error (el bloque rojo de consola) al archivo log
            self.logger.error(mensaje, exc_info=True)
        else:
            self.logger.error(mensaje)

# ==========================================
# MANEJADOR GLOBAL DE EXCEPCIONES
# ==========================================
def global_exception_handler(exc_type, exc_value, exc_traceback):
    """
    Captura cualquier error no manejado (unhandled exception) que cerraría la app
    y lo registra en el archivo de logs antes de que la consola se cierre.
    """
    # Evitar capturar interrupciones manuales del teclado (Ctrl+C)
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    logger = ErrorLogger()
    logger.logger.error("Error crítico no controlado", exc_info=(exc_type, exc_value, exc_traceback))

# Sobrescribe el manejador de errores de Python por el nuestro
sys.excepthook = global_exception_handler