# Модуль 1: Шифрование данных (lab02_1.py)
# =========================================

from cryptography.fernet import Fernet
import os
import sys

def generate_key():
    """
    Функция генерации криптографического ключа
    Возвращает:
        bytes: сгенерированный ключ
    """
    try:
        return Fernet.generate_key()
    except Exception as e:
        print(f"Ошибка генерации ключа: {str(e)}")
        sys.exit(1)

def encrypt_file(input_file, output_file, key):
    """
    Функция шифрования файла
    Параметры:
        input_file (str): путь к исходному файлу
        output_file (str): путь для сохранения зашифрованного файла
        key (bytes): ключ шифрования
    """
    try:
        cipher = Fernet(key)
        with open(input_file, 'rb') as f:
            data = f.read()
        encrypted_data = cipher.encrypt(data)
        with open(output_file, 'wb') as f:
            f.write(encrypted_data)
    except FileNotFoundError:
        print("Ошибка: исходный файл не найден")
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка шифрования: {str(e)}")
        sys.exit(1)

def main_encrypt():
    """
    Основная функция модуля шифрования
    """
    print("=== Модуль шифрования данных ===")
    print("1. Генерация ключа...")
    key = generate_key()
    
    print("2. Шифрование файла secret.txt...")
    encrypt_file('secret.txt', 'secret_encrypted.txt', key)
    
    print("3. Сохранение ключа в файл key.key...")
    with open('key.key', 'wb') as f:
        f.write(key)
    
    print("Шифрование завершено успешно!")
    print(f"Зашифрованный файл: secret_encrypted.txt")
    print(f"Ключ сохранен в: key.key")

if __name__ == "__main__":
    main_encrypt()
