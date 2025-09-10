# Pandas


# Andmetabelite sidumine

## Juhend: Kuidas ühendada kaks DataFrame'i võtme (key) alusel

Kui sul on kaks andmestikku (DataFrame'i), mida ühendab ühine veerg (nt "linn"), saad need ühendada `pd.merge()` funktsiooniga.

**Näide:**

```python
import pandas as pd

# Andmestikud
df1 = pd.DataFrame({
    "linn": ["Tallinn", "Tartu", "Pärnu"],
    "temperatuur": [18.5, 19.2, 17.8]
})

df2 = pd.DataFrame({
    "linn": ["Tallinn", "Tartu", "Pärnu"],
    "elanike_arv": [440000, 95000, 51000]
})

# Ühenda DataFrame'id 'linn' veeru alusel
df_koos = pd.merge(df1, df2, on="linn")

print(df_koos)
```

**Selgitus:**
- `pd.merge(df1, df2, on="linn")` ühendab mõlemad tabelid selle veeru põhjal, mis on mõlemas olemas (`linn`).
- Tulemusena saad ühe DataFrame'i, kus on kõik veerud mõlemast tabelist.

**Kui võtme nimi on erinev:**
```python
df_koos = pd.merge(df1, df2, left_on="linn", right_on="linna_nimi")
```

**Lisainfo:**  
- Vaikimisi tehakse "inner join" ehk ainult need read, mis on mõlemas tabelis olemas.
- Kui soovid kõiki ridu mõlemast tabelist ("outer join"), lisa `how="outer"`:
  ```python
  df_koos = pd.merge(df1, df2, on="linn", how="outer")
  ```

## Juhend: Kuidas filtreerida DataFrame'i andmeid

DataFrame'i filtreerimine tähendab, et saad valida ainult need read, mis vastavad mingile tingimusele.

# Filtreeri ainult read, kus temperatuur on üle 18 kraadi
kuumad = df[df["temperatuur"] > 18]
print(kuumad)
```

**Teisi näiteid:**
- Ainult Tallinn ja Tartu:
  ```python
  df[df["linn"].isin(["Tallinn", "Tartu"])]
  ```
- Ainult niiskus alla 70:
  ```python
  df[df["niiskus"] < 70]
  ```
- Ainult read, kus linna nimi algab T-tähega:
  ```python
  df[df["linn"].str.startswith("T")]
  ```

**Kokkuvõte:**  
Filtreerimiseks kasuta kujul `df[tingimus]`, kus tingimus on loogiline avaldis veeru kohta.

## Andmete parandamine

**Eemalda kõik tühikud**

  ```python
  df["linn"] = df["linn"].str.replace(" ", "")
  ```

**Näide: asenda temperatuur alla 17 väärtusega "külm", muidu "soe"**

```python
df["temp_kategooria"] = np.where(df["temperatuur"] < 17, "külm", "soe")
```

**Juhend:**  
- `np.where(tingimus, väärtus_kui_tõene, väärtus_kui_väär)`

```python
df["temp_kategooria"] = np.where(df["temperatuur"] < 17, "külm", "soe")
print(df)
```
## Vea parandamine kui andmed on NaN (puuduvad andmed)

**Asenda kõik NaN väärtused nulliga**
df = df.fillna(0)

**Või eemalda read, kus on NaN**
df = df.dropna()

## Juhend andmete sorteerimiseks

```python
# Sorteeri temperatuuriveeru järgi kasvavalt
df_sorted = df.sort_values(by="temperatuur")
print(df_sorted)

# Sorteeri tuule kiiruse järgi kahanevalt
df_sorted_desc = df.sort_values(by="tuul", ascending=False)
print(df_sorted_desc)
```

**Kokkuvõte:**  
- Kasuta `.sort_values(by="veeru_nimi")` soovitud veeru järgi sortimiseks.
- Lisa `ascending=False`, kui soovid kahanevat järjestust.
- Mitme veeru puhul kasuta nimekirja: `by=["veeru1", "veeru2"]`


## ÜLESANDED

***Lähteandmed***

```python
import pandas as pd

ilmaandmed = {
    "linn": ["Tallinn", "Tartu", "Pärnu", "Narva", "Kuressaare"],
    "temperatuur": [18.5, 19.2, 17.8, 16.4, 15.9],
    "niiskus": [65, 60, 70, 68, 75],
    "tuul": [4.2, 3.8, 5.0, 4.5, 6.1]
}

linnad_andmed = {
    "linn": ["Tallinn", "Tartu", "Pärnu", "Narva", "Kuressaare"],
    "elanike_arv": [440000, 95000, 51000, 57000],
    "pindala": [159.2, 38.8, 32.2, 84.5, 15.0]  # km²
}
```

- [ ] Leia, millises linnas on kõrgeim temperatuur.
- [ ] Arvuta iga linna rahvastikutihedus (elanike arv / pindala).
- [ ] Filtreeri välja linnad, kus niiskus on üle 70%.
- [ ] Sorteeri andmed tuule kiiruse järgi kasvavalt.
- [ ] Lisa uus veerg, mis näitab kas temperatuur on üle keskmise ("üle keskmise" / "alla keskmise").
- [ ] Ühenda ilmaandmed ja elanike andmed üheks DataFrame'iks.
- [ ] Leia, millises linnas on kõige rohkem elanikke.
- [ ] Asenda kõik linnanimed väikeste tähtedega.
- [ ] Eemalda read, kus mõni väärtus on puudu (NaN).
- [ ] Salvesta lõplik DataFrame CSV-failina.