import time
import machine
import ssd1306

i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4), freq=100000)
display = ssd1306.SSD1306_I2C(64, 48, i2c)

display.fill(0)
display.text('Start', 0, 0, 1)
display.show()

seconds = 0
while True:
    time.sleep(1)
    seconds += 1
    display.fill(0)
    display.text(f'Sekunden: {seconds}', 0, 0, 1)
    display.show()