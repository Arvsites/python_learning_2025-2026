import tkinter as tk  # Для окон
import serial  # Для связи с Arduino
import serial.tools.list_ports  # Для поиска порта
import time  # Для задержек

# Функция поиска порта Arduino
def find_arduino_port():
    ports = serial.tools.list_ports.comports()
    for port in ports:
        if 'Arduino' in port.description or 'Arduino' in port.manufacturer:
            return port.device
    return None

# Подключаемся к Arduino
arduino_port = find_arduino_port()
if arduino_port:
    ser = serial.Serial(arduino_port, 9600, timeout=1)
    time.sleep(2)  # Ждём стабилизации связи
    print(f"Подключено к {arduino_port}")
else:
    print("Arduino не найден! Подключи плату.")
    exit()

# Функция включения LED
def led_on():
    ser.write(b'1')  # Отправляем '1'
    print("LED ВКЛЮЧЁН")

# Функция выключения LED
def led_off():
    ser.write(b'0')  # Отправляем '0'
    print("LED ВЫКЛЮЧЁН")

# Создаём окно
root = tk.Tk()
root.title("Управление LED на Arduino")
root.geometry("300x150")

# Кнопки
btn_on = tk.Button(root, text="ВКЛЮЧИТЬ LED", command=led_on,
                   bg="green", fg="white", font=("Arial", 12))
btn_on.pack(pady=20)

btn_off = tk.Button(root, text="ВЫКЛЮЧИТЬ LED", command=led_off,
                    bg="red", fg="white", font=("Arial", 12))
btn_off.pack(pady=10)

# Запуск приложения
root.mainloop()

# Закрываем порт при выходе
ser.close()




# -------------------
// Светодиод
на
пине
13(встроенный
LED)
int
ledPin = 13;

void
setup()
{
    Serial.begin(9600); // Скорость
связи
с
Python
pinMode(ledPin, OUTPUT); // Настраиваем
пин
как
выход
digitalWrite(ledPin, LOW); // Выключаем
LED
в
начале
}

void
loop()
{
if (Serial.available() > 0)
{ // Ждём
команду
от
Python
char
command = Serial.read(); // Читаем
символ

if (command == '1')
{ // '1' = включить
digitalWrite(ledPin, HIGH);
}
else if (command == '0') {// '0' = выключить
digitalWrite(ledPin, LOW);
}
}
}
