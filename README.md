# Insertion Sort – Prestandaanalys

## Projektstruktur

```
src/                # Implementation av insertion sort
tests/unit/         # Enhetstester
tests/performance/  # Prestandatester
```

## Installation

Installera beroenden:

```
pip install pytest pytest-benchmark
```

## Körning av tester

Kör alla tester med:

```
python -m pytest -s
```

**Notera:**
Flaggan `-s` används för att visa utskrifter från prestandatesterna i terminalen för uppgift 4.

## Prestandatest

Prestandatesterna mäter körtiden för insertion sort med olika liststorlekar:

* 1000
* 2000
* 3000
* 4000
* 5000

## Analys

Resultaten visar att körtiden ökar snabbare än linjärt när listans storlek ökar.
När listan fördubblas indikerar kvadratisk tidskomplexitet:

**O(n²)**

Detta överensstämmer med hur insertion sort fungerar, där varje element jämförs med tidigare element.

