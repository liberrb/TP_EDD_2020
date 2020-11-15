import menu
from menu import QuiereSalirException
import unittest
from unittest.mock import patch

class TestMenu(unittest.TestCase):
    
    menu_t = menu.Menu()
    
    # Test para formato '1'
    @patch("builtins.input", return_value="1")
    def test_pedir_formato_1(self, mock_input):
        self.assertEqual(self.menu_t._Menu__pedir_formato(), "1")
        
    # Test para input '0' (Quiere salir)
    @patch("builtins.input", return_value="0")
    def test_pedir_formato_0(self, mock_input):
        with self.assertRaises(QuiereSalirException):
            self.menu_t._Menu__pedir_formato()
            
    # Test para formato pedir pagina
    @patch("builtins.input", return_value="3")
    def test_pedir_pagina_3(self, mock_input):
        self.assertEqual(self.menu_t._Menu__pedir_pagina(), ["3"])
        
    # Test para formato pedir varias paginas
    @patch("builtins.input", return_value="3,1,2")
    def test_pedir_paginas(self, mock_input):
        self.assertEqual(self.menu_t._Menu__pedir_pagina(), ["3", '1', '2'])
        
    # Test para input '0' (Quiere salir)
    @patch("builtins.input", return_value="0")
    def test_pedir_pagina_0(self, mock_input):
        with self.assertRaises(QuiereSalirException):
            self.menu_t._Menu__pedir_pagina()
    
    # Test para formato pedir tipo busqueda
    @patch("builtins.input", return_value="2")
    def test_pedir_tipo_busqueda(self, mock_input):
        self.assertEqual(self.menu_t._Menu__tipo_busqueda(), '2')
        
    # Test para input '0' (Quiere salir)
    @patch("builtins.input", return_value="0")
    def test_pedir_tipo_busqueda_0(self, mock_input):
        with self.assertRaises(QuiereSalirException):
            self.menu_t._Menu__tipo_busqueda()
            
    # Test para formato pedir extras
    @patch("builtins.input", return_value="2")
    def test_pedir_extra_2(self, mock_input):
        self.assertEqual(self.menu_t._Menu__pedir_extras(), '2')
        
    # Test para input '0' (Quiere salir)
    @patch("builtins.input", return_value="0")
    def test_pedir_extra_0(self, mock_input):
        with self.assertRaises(QuiereSalirException):
            self.menu_t._Menu__pedir_extras()
        