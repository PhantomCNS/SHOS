from machine import Pin, ADC, time_sleep_us
import time
import dht
import network
import uart

# ================================
# variables
dht_Pin = 4  # DHT sensor pin
gas_Pin = 34  # Gas sensor pin
# ================================

# ================================
# Initialize DHT sensor
dht_Sensor = dht.DHT22(Pin(dht_Pin))

# ================================
# Initialize Gas sensor
gas_Sensor = ADC(Pin(gas_Pin))
gas_Sensor.atten(ADC.ATTN_11DB)  # Set attenuation level
# ================================
