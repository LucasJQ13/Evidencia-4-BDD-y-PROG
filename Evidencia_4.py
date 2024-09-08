class ProyectorDeRealidadVirtual:
     def __init__(self, resoluciones_disponibles, dispositivos_disponibles, conexion_inalambrica,):
        # Comportamientos claves del objeto
        self.resoluciones_disponibles = resoluciones_disponibles
        self._resolucion_actual = None
        self.dispositivos_conectados = []
        self.dispositivos_disponibles = dispositivos_disponibles
        self._conexion_inalambrica = False

        def get_resolucion_actual(self):
                return self._resolucion_actual
            
        def set_resolucion_actual(self, resolucion):
            if resolucion in self.resoluciones_disponibles:
                self._resolucion_actual = resolucion
            else:
                raise ValueError("Resolucion no disponible")
            
        def get_conexion_inalambrica(self):
            return self._conexion_inalambrica
        
        def set_conexion_inalambrica(self, estado):
            self._conexion_inalambrica = estado

        #Conexion con Dispositivos
        def conectar_dispositivo (self, dispositivo):
            if dispositivo in self.dispositivos_disponibles and dispositivo not in self.dispositivos_conectados:
                self.dispositivos_conectados.append(dispositivo)
                return f"{dispositivo} conectado"
            elif dispositivo in self.dispositivo_conectados:
                return f"{dispositivo} ya esta enlazado"
            else:
                return f"{dispositivo} no esta disponible"
            

    
        #Visualizacion de Imagen
        def visualizar_imagen(self, resolucion):
            if resolucion in self.resolucion_disponible:
                self.resolucion_actual = resolucion
                return f"Calidad en {resolucion}p"
            else:
                return "Resolucion no disponible"
            
        #Conexion inalambrica
        def activar_conexion_inalambrica(self, estado):
            if estado:
                self.conexion_inalambrica = True
                return "conexion inalambrica activada"
            else:
                self.conexion_inalambrica = False
                return "conexion inalambrica desactivada"
            
        #Estado del Proyector
        def __str__(self):
            return (f"Proyector de Realidad Virutal"), "Resolucion Actual: {self.resolucion_actual}", "Dispositivos Conectados: {', '.join(self.dispositivos_conectados) if self.dispositivos_conectados else 'Ninguno'}", "Conexion inalambrica: {'Activada' if self.conexion_inalambrica else 'Desactivada'}"

            