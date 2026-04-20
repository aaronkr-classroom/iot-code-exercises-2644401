from room_sensor import RoomSensor

sensor1 = RoomSensor("Kitchen", 31, 72, 180)
sensor2 = RoomSensor("Bedroom", 24, 50, 300)
sensor3 = RoomSensor("Balcony", 18, 65, 150)

sensors = [sensor1, sensor2, sensor3]

comfortable_count = 0
normal_count = 0
warning_count = 0

for sensor in sensors:
    sensor.show_info()
    
    comfort = sensor.comfort_level()
    light = sensor.light_status()
    
    print("Comfort Level:", comfort)
    print("Light Status:", light)
    print()
    
    if comfort == "Comfortable":
        comfortable_count += 1
    elif comfort == "Warning":
        warning_count += 1
    else:
        normal_count += 1
        
print("Comfortable:", comfortable_count)
print("Normal:", normal_count)
print("Warning:", warning_count)