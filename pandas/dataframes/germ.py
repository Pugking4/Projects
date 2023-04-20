import pandas as pd

# Eingabedaten
schueler = ["Alice", "Bob", "Charlie", "David", "Eva"]
mathe_punkte = [90, 80, 85, 88, 92]
naturwissenschaft_punkte = [89, 91, 80, 86, 95]
englisch_punkte = [85, 88, 90, 92, 94]

daten = []

for i, schueler in enumerate(schueler):
    durchschnitt = (mathe_punkte[i] + naturwissenschaft_punkte[i] + englisch_punkte[i]) / 3
    daten.append({
        'schueler': schueler,
        'mathe_punkte': mathe_punkte[i],
        'naturwissenschaft_punkte': naturwissenschaft_punkte[i],
        'englisch_punkte': englisch_punkte[i],
        'durchschnitt': durchschnitt
    })

df = pd.DataFrame(daten)
df.set_index('schueler', inplace=True)

print(df)
