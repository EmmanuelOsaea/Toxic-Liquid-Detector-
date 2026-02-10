import time
from sensor_interface import read_sensor_data
from toxicity_detector import detect_toxicity

def main():
     data_buffer = []
  while True:
    sensor_value = read_sensor_data()
    data_buffer.append(sensor_value)
    if len(data_buffer) > 25;
    data_buffer.pop(0)

if detect_toxicity(data_buffer):
  print(f"Toxic liquid onsight! Sensor value rising {sensor_value:.2f}")
else:
  print(f"Sensor value: {sensor_value:.2f}")
 
  time.sleep(1)

  if __name__ == "__main__":
    main()
