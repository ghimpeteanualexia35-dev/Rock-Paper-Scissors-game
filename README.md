# Rock-Paper-Scissors-game
# Rock-Paper-Scissors-Game
  
Aplicația implementează jocul „Piatra – Hârtie – Foarfecă” cu interfață grafică, în care utilizatorul joacă împotriva calculatorului.


## 1. Cerințe și rulare

### 1.1 Tehnologii folosite
Proiectul a fost implementat și testat folosind **IDLE (Python 3.10, 64-bit)** și utilizează doar module standard din Python:
- `random` – pentru alegerea aleatoare a opțiunii calculatorului
- `tkinter` – pentru realizarea interfeței grafice (GUI)

### 1.2 Structura proiectului
Proiectul este împărțit în trei fișiere Python, care trebuie să se afle în același folder:

- `game_logic.py` – conține logica jocului  
- `gui.py` – conține interfața grafică  
- `main.py` – fișierul principal de rulare  

### 1.3 Cum se rulează
Pentru a rula aplicația folosind IDLE:

1. Se deschide **IDLE (Python 3.10, 64-bit)**  
2. Se alege **File → Open…** și se selectează fișierul `main.py`  
3. Se apasă **F5** sau **Run → Run Module**

Aplicația va deschide o fereastră grafică în care utilizatorul poate juca „Piatra – Hârtie – Foarfecă” împotriva calculatorului.


## 2. Descrierea proiectului

Scopul proiectului este realizarea unui joc simplu „Piatra – Hârtie – Foarfecă”, cu interfață grafică, în care:
- utilizatorul alege o opțiune
- calculatorul alege aleator o opțiune
- programul decide rezultatul: câștig, pierdere sau egalitate

Pentru o organizare mai clară a codului:
- logica jocului este separată de interfața grafică
- aplicația este pornită dintr-un fișier principal (`main.py`)


## 2.1 game_logic.py

- Modulul `random` este folosit pentru a alege o opțiune aleatorie pentru calculator  
- Lista `choices` conține toate opțiunile posibile din joc  
- Funcția `get_computer_choice()` returnează o alegere aleatoare pentru calculator  
- Funcția `determine_winner(user, computer)` primește opțiunea utilizatorului și a calculatorului și determină rezultatul jocului (câștig, pierdere sau egalitate)


## 2.2 gui.py

- Modulul `tkinter` este folosit pentru interfața grafică  
- Funcțiile din `game_logic.py` sunt importate și utilizate  
- Clasa `RPSApp` definește aplicația principală și gestionează interfața și interacțiunea cu utilizatorul  

În constructorul `__init__`:
- se creează fereastra principală  
- se afișează un label cu instrucțiuni  
- se creează butoanele pentru „Piatra”, „Hârtie” și „Foarfecă”  
- se creează un label care afișează rezultatul  

Metoda `play()` este apelată atunci când utilizatorul apasă un buton și actualizează rezultatul afișat în fereastră.


## 2.3 main.py

- Este punctul de pornire al aplicației  
- Funcția `main()` creează fereastra principală și pornește aplicația  
- Instrucțiunea  
  `if __name__ == "__main__":`  
  asigură că aplicația pornește doar atunci când fișierul este rulat direct  


## Bibliografie

- https://chatgpt.com/share/695befca-d304-8011-9050-3173191687a4  
- https://www.w3schools.com/python/ref_module_tkinter.asp  
- https://www.w3schools.com/python/ref_random_choices.asp  
- https://docs.python.org/3/library/tkinter.html  
- https://www.w3schools.com/python/python_classes.asp  
- https://www.w3schools.com/python/python_class_init.asp
