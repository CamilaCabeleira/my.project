from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/tables")

# la tabla en la página (se utiliza XPath en este caso)
table = driver.find_element(By.XPATH, "//table[@id='table1']")

# las filas de la tabla
rows = table.find_elements(By.TAG_NAME, "tr")

# Recorre las filas (omitimos la primera fila que contiene los encabezados)
for row in rows[1:]:
    # Obtiene las celdas de cada fila
    cells = row.find_elements(By.TAG_NAME, "td")

    # Obtiene el nombre y el valor de la columna correspondiente
    name = cells[0].text
    value = float(cells[3].text.replace("$", ""))

    # Verifica si el valor es mayor que $50
    if value > 50:
        print(name)

# Cierra el navegador
driver.quit()
