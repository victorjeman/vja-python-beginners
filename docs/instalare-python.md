# Ghid de instalare Python + VSCode (Windows)

---

## Pasul 1 - Instalam Python

1. Deschide browserul si intra pe: https://www.python.org/downloads/
2. Apasa butonul mare galben **"Download Python 3.x.x"**
3. Deschide fisierul descarcat (ex: `python-3.x.x-amd64.exe`)
4. **FOARTE IMPORTANT** - Bifeaza casuta **"Add python.exe to PATH"** (jos in fereastra de instalare)
5. Apasa **"Install Now"**
6. Asteapta sa se termine instalarea
7. Apasa **"Close"**

### Verificam ca Python s-a instalat corect

1. Apasa tasta `Windows` si scrie `cmd`
2. Deschide **Command Prompt**
3. Scrie urmatoarea comanda si apasa `Enter`:

```
python --version
```

4. Daca vezi ceva de genul `Python 3.12.4` inseamna ca totul e bine!
5. Daca nu merge, incearca:

```
python3 --version
```

---

## Pasul 2 - Instalam Visual Studio Code

1. Intra pe: https://code.visualstudio.com/
2. Apasa butonul mare albastru **"Download for Windows"**
3. Deschide fisierul descarcat
4. Apasa **"Next"** de cateva ori
5. La pasul **"Select Additional Tasks"** bifeaza **"Add to PATH"**
6. Apasa **"Install"**
7. Apasa **"Finish"**

---

## Pasul 3 - Instalam extensia Python in VSCode

1. Deschide **Visual Studio Code**
2. In bara din stanga apasa pe iconita cu **4 patratele** (Extensions) sau apasa `Ctrl + Shift + X`
3. In bara de cautare scrie: `Python`
4. Primul rezultat ar trebui sa fie **"Python"** de la **Microsoft**
5. Apasa butonul albastru **"Install"**

---

## Pasul 4 - Cream primul fisier Python

1. In VSCode apasa `Ctrl + N` (fisier nou)
2. Apasa `Ctrl + S` si salveaza fisierul cu numele `test.py` (oriunde pe calculator, ex: Desktop)
3. Scrie in fisier:

```python
print("Salut! Python functioneaza!")
```

4. Salveaza cu `Ctrl + S`

---

## Pasul 5 - Rulam codul

1. Apasa butonul **▶ (Play)** din coltul dreapta sus al editorului
2. In partea de jos a ecranului ar trebui sa apara:

```
Salut! Python functioneaza!
```

3. Daca vezi mesajul, felicitari, totul este gata!

---

## Nu merge? Alternativa online

Daca nu reusesti sa instalezi Python, poti scrie cod direct in browser:

https://www.pythonsandbox.com

Scrie `print("Salut!")` si apasa **Run**. Functioneaza fara sa instalezi nimic!
