import matplotlib.pyplot as plt

class Sensor:
    def __init__(self, name):
        self.name = name
        self.working = True

    def activate(self):
        if self.working:
            print(f"{self.name} sensor is activated.")
            return True
        else:
            print(f"{self.name} sensor is not working.")
            return False

def main():
    sensors = [Sensor("Sensor1"), Sensor("Sensor2"), Sensor("Sensor3"), Sensor("Sensor4")]

    # Моделюємо умови роботи кожного сенсора по черзі
    for sensor in sensors:
        sensor.activate()

    # Моделюємо несправність всіх сенсорів
    for sensor in sensors:
        sensor.working = False

    # Відобразимо результати на графіку
    draw_graph(sensors)

def draw_graph(sensors):
    names = [sensor.name for sensor in sensors]
    status = [1 if sensor.working else 0 for sensor in sensors]

    plt.bar(names, status, color=['green' if s else 'red' for s in status])
    plt.xlabel('Sensors')
    plt.ylabel('Status (1: Working, 0: Not Working)')
    plt.title('Sensor Status')
    plt.show()

if __name__ == "__main__":
    main()
