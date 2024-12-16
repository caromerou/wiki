import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WikipediaSearchTest(unittest.TestCase):

    def setUp(self):
        # Configurar el driver de Selenium
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        self.url = "https://www.wikipedia.org/"

    def test_search_testing(self):
        driver = self.driver
        wait = self.wait

        # 1. Abrir la página principal de Wikipedia
        driver.get(self.url)

        # 2. Localizar el campo de búsqueda
        search_field = wait.until(EC.presence_of_element_located((By.ID, "searchInput")))

        # 3. Ingresar el término "Testing" y realizar la búsqueda
        search_field.send_keys("Testing")
        search_field.send_keys(Keys.RETURN)

        # 4. Verificar que la página de resultados se cargue
        # Esperar a que el título de la página cambie
        wait.until(EC.title_contains("Testing"))

        # 5. Imprimir el título de la página como confirmación
        print(f"Título de la página: {driver.title}")

        # Verificar que el término buscado esté en el título de la página
        self.assertIn("Testing", driver.title, "El término 'Testing' no está en el título de la página.")

    def tearDown(self):
        # Cerrar el navegador después de la prueba
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
