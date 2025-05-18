# 📝 Test Plan – Aplikacja Logowania

**Projekt:** System logowania do aplikacji webowej  
**Autor:** Szymon Jeż  
**Data utworzenia:** 2024-05-15  
**Wersja dokumentu:** 1.0

---

## 🎯 Cel testów

Celem testów jest weryfikacja poprawności działania formularza logowania, walidacji danych wejściowych, komunikatów o błędach oraz scenariuszy logowania poprawnego i niepoprawnego.

---

## 📦 Zakres testów

### W zakresie:
- Logowanie z poprawnymi danymi
- Logowanie z błędnymi danymi
- Walidacja pustych pól
- Spójność komunikatów błędów
- Przekierowanie po poprawnym logowaniu

### Poza zakresem:
- Proces rejestracji
- Zmiana hasła
- Panel użytkownika po zalogowaniu

---

## 🔧 Środowisko testowe

- Przeglądarki: Chrome 124.0, Firefox 115.0
- System operacyjny: Windows 10, Android 13
- Adres testowy: `https://example.com/login`

---

## 🧪 Typy testów

- Testy funkcjonalne
- Testy eksploracyjne
- Testy regresyjne
- Testy negatywne

---

## 🗃️ Dane testowe

| Scenariusz                | Login                 | Hasło       | Oczekiwany rezultat                 |
|---------------------------|-----------------------|-------------|-------------------------------------|
| Poprawne dane             | test@example.com      | Test1234!   | Przekierowanie na /dashboard       |
| Puste hasło               | test@example.com      | (puste)     | Komunikat „Hasło jest wymagane”    |
| Zły email                 | test@                | Test1234!   | Komunikat „Nieprawidłowy email”    |
| Złe hasło                 | test@example.com      | abc         | Komunikat „Nieprawidłowe dane”     |

---

## 📅 Harmonogram

| Etap                    | Data rozpoczęcia | Data zakończenia |
|-------------------------|------------------|------------------|
| Przygotowanie testów    | 2024-05-13        | 2024-05-14        |
| Wykonanie testów        | 2024-05-15        | 2024-05-16        |
| Retesty / poprawki      | 2024-05-17        | 2024-05-18        |

---

## 📈 Metryki i kryteria zakończenia

- Wszystkie testy krytyczne zakończone sukcesem
- Nie więcej niż 2 błędy średniego priorytetu
- 100% przypadków testowych wykonanych

---

## 🧾 Dokumenty powiązane

- TC-001: Logowanie poprawne
- TC-002: Logowanie bez hasła
- BR-001: Logowanie bez hasła pozwala przejść dalej
