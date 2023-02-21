# Напишіть програму, щоб отримати назву, платформу та інформацію про випуск операційної системи.
# Використайте імпорт модулів platform і os.
import os
import platform


def main():


    print(os.name)
print(platform.system())
print(platform.release())

if __name__ == "__main__":
    main()
