import unittest
from Evidencia_4 import ProyectorDeRealidadVirtual

class TestProyectorDeRealidadVirtual(unittest.TestCase):
    def setUp(self):
        self.proyector = ProyectorDeRealidadVirtual(resoluciones_disponibles=[720, 1080, 1440], dispositivos_disponibles=["Celular","PC","Notebook"])

        #Primera prueba: Conexion de Dispositivo
        def test_conectar_dispositivo(self):
            resultado = self.proyector.conectar_dispositivo("Celular")
            self.assertEqual(resultado, "Celular conectado")
            self.assertIn("Celular", self.proyector.dispositivos_conectados)

        #Segunda prueba: No conectar dispositivos conectados
        def test_dispositivos_ya_conectados(self):
            self.proyector.conectar_dispositivos("Celular")
            resultado = self.proyector.conectar_dispositivos("Celular")
            self.assertEqual(resultado,"El dispositivo ya está conectado")

        #Tercer prueba: Conectar dispositivo no admitido
        def test_dispositivo_no_admitido(self):
            resultado = self.proyector.conectar_dispositivo("Tablet")
            self.assertEqual(resultado, "Dispositivo no admitido")

        #Cuarta prueba: Cambio de resolucion
        def test_visualizar_imagen(self):
            resultado = self.proyector.visualizar_imagen(720)
            self.assertEqual(resultado, "Visualizando en 720p")
            self.assertEqual(self.proyector.resolucion_actual, 720)

        #Quinta prueba: Cambio a resolucion no admitida
        def test_resolucion_no_admitida(self):
            resultado = self.proyector.visualizar_imagen(4000)
            self.assertEqual(resultado, "Resolucion no admitida")
            
        #Sexta prueba: Activar conexion Inalambrica
        def test_activar_conexion_inalambrica(self):
            resultado = self.proyector.activar_conexion_inalambrica(True)
            self.assertEqual(resultado, "Conexion inalambrica activa")
            self.assertTrue(self.proyector.conexion_inalambrica)

        #Septima prueba: Desactivar conexion inalambrica
        def test_desactivar_conexion_inalambrica(self):
            self.proyector.activar_conexion_inalambrica(True)
            resultado = self.proyector.activar_conexion_inalambrica(False)
            self.assertEqual(resultado, "Conexion inalamabrica descativada")
            self.assertEqual(self.proyector.conexion_inalambrica)

        # Ejecutar pruebas
        if __name__ == '__main__':
            unittest.main()


        