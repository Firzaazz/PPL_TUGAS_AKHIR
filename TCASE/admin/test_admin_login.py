from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Inisialisasi WebDriver (Chrome)
driver = webdriver.Chrome()

# Buka halaman login
driver.get("https://opensource-demo.orangehrmlive.com/")

# Tunggu hingga elemen "txtUsername" muncul (maksimal 10 detik)
username_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "txtUsername"))
)
password_field = driver.find_element(By.ID, "txtPassword")
login_button = driver.find_element(By.ID, "btnLogin")

username_field.send_keys("Admin")
password_field.send_keys("admin123")
login_button.click()

# Tunggu beberapa saat untuk proses login
time.sleep(2)

# Verifikasi login berhasil
assert "Dashboard" in driver.page_source

# Jika berhasil, cetak pesan sukses
print("Login berhasil!")

# Tutup browser
driver.quit()
