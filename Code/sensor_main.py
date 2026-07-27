from machine import Pin, ADC, time_sleep_us
import time
import dht
import network
import uart

# ============================================================
# variables
# --------------------------------

dht_Pin = 14  # DHT sensor pin
gas_Pin = 25  # Gas sensor pin
led_Pin = 2   # LED pin
# ============================================================

# ============================================================
# Initializations
# --------------------------------

# Initialize DHT sensor

dht_Sensor = dht.DHT22(Pin(dht_Pin))

# --------------------------------
# Initialize Gas sensor

gas_Sensor = ADC(Pin(gas_Pin))
gas_Sensor.atten(ADC.ATTN_11DB)  # Set attenuation level

# --------------------------------
# Initialize LED

led = Pin(led_Pin, Pin.OUT)

# --------------------------------
# Initialize Wi-Fi connection

wifi_ssid = "Your_SSID"
wifi_password = "Your_Password"
# --------------------------------

# Initialize UART for communication
uart_port = 1  # UART port number
uart = uart.UART(uart_port, baudrate=9600)  # Initialize UART with specified port and baud rate

# ============================================================
