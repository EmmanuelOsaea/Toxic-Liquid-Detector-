import random

def read_sensor_data():

  base = 7
  noise = random.uniform (-0.7, 0.7)
  stomp = random.choice([0, 0, 0, 7]) # Occasional stomp
  return base_value+noise+stomp
