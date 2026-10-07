import statistics

class Sensor:
    def __init__(self, sensor_id):
        self.sensor_id = sensor_id
        self._readings = []

    def add_reading(self, value):
        self._readings.append(value) 
        
    def average(self):
        readings = self._readings

        
        if not readings:
            raise EmptySensorError("Cannot retrieve an item because the private list is empty")
        
        mean = statistics.mean(self._readings)
        return mean
    
    def __str__(self):
        TempSensor = [self.sensor_id, self._readings]
        return (f"TemperatureSensor(id= {TempSensor[0],},  readings= {TempSensor[1]})")

    def __len__(self):
        return len(self._readings)
    
    def __eq__(self, other):
        if not isinstance(other, Sensor):
            return NotImplemented
        return self.sensor_id == other.sensor_id
    
    @classmethod
    def from_ids(cls, id_list):
        return [cls(id) for id in id_list]


class TemperatureSensor(Sensor):
    def __init__(self, sensor_id, unit):
        super().__init__(sensor_id)

        if unit not in ["C", "F", "f", "c"]:
            raise ValueError("Wrong unit!!! Enter C or F: ")
        
        self.unit = unit.upper()

    def add_reading(self, value):
        Unit = self.unit
        
        if Unit == "F":
                value = (value - 32)*5/9
                super().add_reading(value)
        else:
            super().add_reading(value)   
    
class HumiditySensor(Sensor):
    def __init__(self, sensor_id):
        super().__init__(sensor_id)

        #self.value = value

    def add_reading (self, value):
        clamped_value = value

        if clamped_value > 100:
            clamped_value = 100

        if clamped_value < 0:
            clamped_value = 0
    
                
        super().add_reading(clamped_value)

class EmptySensorError (Exception):
    pass       

class SensorFleet:
    def __init__(self):
        self._sensors = []

    def add_sensor(self, sensor):
        self._sensors.append(sensor)    

    def fleet_average(self):
        all_readings = []
        for sensor in self._sensors:
            try:
                sensor.average()
                all_readings.extend(sensor._readings)

            except EmptySensorError as e: 
                print(f"Caught expected error: {e}")   

        return statistics.mean(all_readings)

    def find(self, sensor_id):

        for sensor in self._sensors:
            if sensor.sensor_id == sensor_id :
                return sensor
            
        return None    
            
    def __iter__(self):
        return iter(self._sensors)        

fleet = SensorFleet()

t1 = TemperatureSensor("T1", "C")
t2= TemperatureSensor("T2", "F")
h1 = HumiditySensor("H1")

fleet.add_sensor(t1)
fleet.add_sensor(t2)
fleet.add_sensor(h1)

t1.add_reading(20)
t1.add_reading(30)

t2.add_reading(77)
t2.add_reading(99)

h1.add_reading(45)
h1.add_reading(105)
h1.add_reading(-10)

empty_sensor = TemperatureSensor("T3", "C")

try:
    empty_sensor.average()
except EmptySensorError as e:
    print(f"Caught expected error: {e}")

print(fleet.fleet_average())
print(Sensor("T1"))

print(h1.__len__())

            

                
        
                    

