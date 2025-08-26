import unittest #importamos el módulo de pruebas unitarias
class mi_clase_test_uni(unittest.TestCase): #creamos una clase que hereda de unittest.TestCase
        #Haz todas sus pruebas unitarias dentro, llamadas test_algo
        def test_igualdad(self):
            self.assertEqual(1,1) #* a == b
        
        def test_verdad(self):
            self.assertTrue(3 > 2) #* consion verdad
        
        def test_tipo_dato(self):
            self.assertIsInstance(1, str)
            self.assertIsInstance((1 , 2, 3), tuple)
       
        def test_mismo_obj(self): 
            a = [1, 2, 3]
            b = a
            self.assertIs(a, b)  #* mismo obj
            
        def test_esta_en(self):
            self.assertIn(5, [1, 2, 3]) #* 3 en la lista

if __name__ == '__main__':
    unittest.main() #ejecuta las pruebas unitarias
            
            