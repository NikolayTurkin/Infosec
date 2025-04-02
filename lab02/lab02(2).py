# Модуль 2: Дешифрование данных (lab02_2.py)
# ===========================================

from cryptography.fernet import Fernet
import os
import sys

def load_key(key_file):
    """
    Функция загрузки ключа из файла
    Параметры:
        key_file (str): путь к файлу с ключом
    Возвращает:
        bytes: загруженный ключ
    """
    try:
        with open(key_file, 'rb') as f:
            return f.read()
    except FileNotFoundError:
        print("Ошибка: файл с ключом не найден")
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка загрузки ключа: {str(e)}")
        sys.exit(1)

def decrypt_file(input_file, output_file, key):
    """
    Функция дешифрования файла
    Параметры:
        input_file (str): путь к зашифрованному файлу
        output_file (str): путь для сохранения дешифрованного файла
        key (bytes): ключ дешифрования
    """
    try:
        cipher = Fernet(key)
        with open(input_file, 'rb') as f:
            encrypted_data = f.read()
        decrypted_data = cipher.decrypt(encrypted_data)
        with open(output_file, 'wb') as f:
            f.write(decrypted_data)
    except FileNotFoundError:
        print("Ошибка: зашифрованный файл не найден")
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка дешифрования: {str(e)}")
        sys.exit(1)

def main_decrypt():
    """
    Основная функция модуля дешифрования
    """
    print("=== Модуль дешифрования данных ===")
    print("1. Загрузка ключа из файла key.key...")
    key = load_key('key.key')
    
    print("2. Дешифрование файла secret_encrypted.txt...")
    decrypt_file('secret_encrypted.txt', 'secret_decrypted.txt', key)
    
    print("Дешифрование завершено успешно!")
    print(f"Дешифрованный файл: secret_decrypted.txt")

if __name__ == "__main__":
    main_decrypt()
