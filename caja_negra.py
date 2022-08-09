import unittest

def suma(num_1, num_2):
    # Si hacemos un cambio en el return donde queremos obtener el numero absoluto abs(num1) esto provocara un error en el test para sumar negativos, al hacer un cambio y tener casos de prueba para validar el funcionamiento correcto esto provoca que lo solucionemos inmediatamente conjunto a prever el desconocimiento de donde ocurre o ocurra este error
    return num_1 + num_2

class CajaNegraTest(unittest.TestCase):

    # Esta creacion del objeto crea automaticamente los testeo dentro del modulo de python
    def test_suma_do_psoitivos(self):
         
        num_1 = 10
        num_2 = 5

        resultado = suma(num_1, num_2)
        # Esto funciona asi:
        # (valor, valorQuerido) = valor == valorQuerido (Nos devuelve un true o false)
        self.assertEqual(resultado, 15)

    def test_suma_dos_negativos(self):
        num_1 = -10
        num_2 = -7

        resultado = suma(num_1, num_2)
        self.assertEqual(resultado, -17)


if __name__ == "__main__":
    unittest.main()