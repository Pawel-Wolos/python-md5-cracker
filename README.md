# Łamacz Haszy MD5 (Python)

Prosty skrypt w języku Python stworzony do przeprowadzania ataków słownikowych (Dictionary Attack) na hasze MD5. Projekt zrealizowany w celach edukacyjnych, demonstrujący podstawy kryptografii oraz automatyzacji zadań w IT.

## Funkcje projektu
* **Symulacja ataku słownikowego:** Skrypt dynamicznie wczytuje potencjalne hasła z lokalnego pliku tekstowego (`slownik.txt`).
* **Optymalizacja wydajności:** Wykorzystanie instrukcji `break` pozwala na natychmiastowe zatrzymanie działania programu po znalezieniu dopasowania, co oszczędza zasoby procesora.
* **Bezpieczne operacje na plikach:** Użycie menedżera kontekstu (`with open`) zapobiega wyciekom pamięci w systemie.

## Jak to działa?
1. Program ładuje zdefiniowany hasz MD5 jako cel.
2. Odczytuje słowa z pliku `slownik.txt` linia po linii, oczyszczając je z ukrytych znaków końca linii (`.strip()`).
3. Konwertuje tekst na bajty (`.encode()`), a następnie generuje z niego hasz przy użyciu biblioteki `hashlib`.
4. W przypadku wykrycia identycznego hasza, program wyświetla złamane hasło i kończy działanie.

## Użyte technologie
* **Język:** Python 3.x
* **Biblioteki standardowe:** `hashlib`

---
*Projekt stworzony w ramach budowania fundamentów pod pracę w obszarze Wsparcia IT oraz Cybersecurity.*
