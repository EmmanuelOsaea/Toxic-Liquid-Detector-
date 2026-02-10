import random

def read_sensor_data():
 # This simulates sensor reading with noise and occasional stomp indicating toxity
  base = 7
  noise = random.uniform (-0.7, 0.7)
  stomp = random.choice([0, 0, 0, 7]) # Occasional stomp
  return base_value+noise+stomp


