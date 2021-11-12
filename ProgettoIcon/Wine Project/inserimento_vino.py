import tkinter as tk
from functools import partial
from main import *






window = tk.Tk()
window.geometry("626x417")
window.title("Ricerca vino")
window.resizable(False, False)
window.configure(background="#fff5f5")

background_image = tk.PhotoImage(file='../img/bg_val.png')
background_label = tk.Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

#photo = tk.PhotoImage(file='../img/wineresize2.png')
#tk.Label(window, image=photo).place(x=0, y=0)

#tk.Label(window, image=photo).place(x=0, y=0)


def answer():
    text = "               "
    output = tk.Label(window, text=text, fg="#67BD66", font=("Times New Roman", 16)
                           ).place(x=290, y=340)
    inputFix = float(textFix.get("1.0", "end-1c"))

    inputVolAc = float(textVol.get("1.0", "end-1c"))

    inputCitAc = float(textCit.get("1.0", "end-1c"))

    inputCh = float(textChl.get("1.0", "end-1c"))

    inputFSD = float(textFSD.get("1.0", "end-1c"))

    inputTSD = float(textTSD.get("1.0", "end-1c"))

    inputSul = float(textSul.get("1.0", "end-1c"))

    inputAl = float(textAlc.get("1.0", "end-1c"))

    row = {'fixed acidity': inputFix, 'volatile acidity': inputVolAc, 'citric acid': inputCitAc, 'chlorides': inputCh, 'free sulfur dioxide': inputFSD,
           'total sulfur dioxide': inputTSD, 'sulphates': inputSul, 'alcohol': inputAl}
    X_KB = df_empty.append(row, ignore_index=True)

    forest = RandomForestClassifier(max_depth=11, random_state=10)
    forest.fit(X_train, Y_train)
    forest_pred = forest.predict(X_KB)
    text = forest_pred
    output = tk.Label(window, text=text, fg="#A65297", font=("Times New Roman", 16)
                           ).place(x=297, y=340)






title = tk.Label(text="Inserimento Dati Vino", fg="#282828", bg="#A65297", font=("Georgia", 20)).place(x=170, y=0)

# Fixed Acidity
labelFix = tk.Label(text="Fixed Acidity", fg="#282828", bg="#A65297", font=("Georgia", 14)).place(x=70, y=50)
textFix = tk.Text(width=12, height=1, font=14)
textFix.place(x=300, y=55)
# Volatile Acidity
labelVol = tk.Label(text="Volatile Acidity", fg="#282828", bg="#A65297", font=("Georgia", 14)).place(x=70, y=80)
textVol = tk.Text(width=12, height=1, font=14)
textVol.place(x=300, y=85)
# Citric Acid
labelCit = tk.Label(text="Citric Acid", fg="#282828", bg="#A65297", font=("Georgia", 14)).place(x=70, y=110)
textCit = tk.Text(width=12, height=1, font=14)
textCit.place(x=300, y=115)
# Chlorides
labelChl = tk.Label(text="Chlorides", fg="#282828", bg="#A65297", font=("Georgia", 14)).place(x=70, y=140)
textChl= tk.Text(width=12, height=1, font=14)
textChl.place(x=300, y=145)
# Free Sulfur Dioxide
labelFSD = tk.Label(text="Free Sulfur Dioxide", fg="#282828", bg="#A65297", font=("Georgia", 14)).place(x=70, y=170)
textFSD= tk.Text(width=12, height=1, font=14)
textFSD.place(x=300, y=175)
# Total Sulfur Dioxide
labelTSD = tk.Label(text="Total Sulfur Dioxide", fg="#282828", bg="#A65297", font=("Georgia", 14)).place(x=70, y=200)
textTSD = tk.Text(width=12, height=1, font=14)
textTSD.place(x=300, y=205)
# Sulphates
labelSul = tk.Label(text="Sulphates", fg="#282828", bg="#A65297", font=("Georgia", 14)).place(x=70, y=230)
textSul = tk.Text(width=12, height=1, font=14)
textSul.place(x=300, y=235)
# Alcohol
labelAlc = tk.Label(text="Alcohol", fg="#282828", bg="#A65297", font=("Georgia", 14)).place(x=70, y=260)
textAlc = tk.Text(width=12, height=1, font=14)
textAlc.place(x=300, y=265)



answer_button = tk.Button(text="Qualità", fg="#282828", bg="#A65297", font="Georgia",
                        width=40, command=partial(answer)).place(x=70, y=375)

window.mainloop()