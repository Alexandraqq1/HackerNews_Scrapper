import pandas as pd
from pathlib import Path

def save_to_excel(df, filename="data/stiri.xlsx"):

    # creez un obiect path pentru a lucra mai usor cu fisierele
    path = Path(filename)

    # Daca folderul "data" nu exista, il creez
    path.parent.mkdir(exist_ok=True)

    # Daca fisierul excel existra deja, il deschidem si il combinam cu date noi
    if path.exists():
        old = pd.read_excel(path, engine="openpyxl")
        # combin datele vechi + cele noi
        # elimin duplicatele ( aceleasi linkuri )
        combined = pd.concat([old, df]).drop_duplicates(subset=["Link"], keep="first")
    else:
        # daca fisierul excel nu exista, folosim datele curente
        combined = df


    # salvam totul intr un fisier excel
    combined.to_excel(path, index=False)

    print(f"Am salvat {len(df)} de stiri noi. Stiri in total: {len(combined)}")

