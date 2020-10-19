# UAIC_FII_AI_LAB_2

## Rulare

In directorul curent:
```
python.exe main.py
```

## Cerinta

Etape de rezolvare:

  * (0.2) Alegeți o reprezentare a unei stări a problemei. Reprezentarea trebuie să fie suficient de explicită pentru a conține toate informaţiile necesare pentru continuarea găsirii unei soluții dar trebuie să fie și suficient de formalizată pentru a fi ușor de prelucrat/memorat.
  * (0.2) Identificați stările speciale (inițială și finală) și implementați funcția de inițializare (primește ca parametrii instanța problemei, întoarce starea inițială) și funcția booleană care verifică dacă o stare primită ca parametru este finală.
  * (0.2) Implementați tranzițiile ca o funcție care primește ca parametri o stare și parametrii tranziției și întoarce starea rezultată în urma aplicării tranziției. Validarea tranziției se face într-o funcție booleană separată, cu aceeași parametrii.
  * (0.2) Implementați strategia Backtracking.
  * (0.2) Implementați strategia BFS.
  * (0.2) Implementați strategia Hillclimbing.
  * (BONUS 0.2) Implementați Simulated Annealing cu o euristică admisibilă și consistentă.
  
***

Detalii suplimentare:
  * strategia Hillclimbing implementata in `solve_hill_climbing` esueaza cu siguranta in cazul oricarui labirint cu bazine de acumulare in minime locale extinse pe toata suprafata de cautare a algoritmului in forma lui actuala
    * labirinturile generate automat in `maze_creator.py` contin foarte multe minime locale care impiedica gasirea unui drum prin hillclimbing
    * algoritmul va da rezultat doar prin aplicarea lui numai pe anumite tipuri de labirint, precum cel atribuit si comentat in `main.py` 
