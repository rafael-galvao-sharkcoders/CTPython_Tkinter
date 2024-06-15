import tkinter as tk 
from tkinter import messagebox
import requests
import json
from datetime import datetime

API_KEY = "073beab07b34f4bb86f16fdb81a38990"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def obter_dados_metreologicos(cidade):
    params = {
        'q': cidade,
        'appid': API_KEY,
        'units': 'metric',
        'lang': 'pt'
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()

def guardar_historico(cidade, temperatura):
    with open('historico_temperatura.txt', 'a', encoding='uft-8') as ficheiro:
        data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ficheiro.write(f"{data_hora} - {cidade}: {temperatura}ºC\n")

class AppMetreologia:
    def __init__(self, root):
        self.root = root
        self.root.title("App da Metreologia")
        self.root.geometry("400x200")

        self.cidade_label = tk.Label(root, text="Cidade:")
        self.cidade_label.pack(pady=10)

        self.cidade_entry = tk.Entry(root, width=50)
        self.cidade_entry.pack(pady=10)

        self.buscar_button = tk.Button(root, text="Pesquisar:", command=self.procurar_meteorlogia)
        self.buscar_button.pack(pady=10)

        self.resultado_label = tk.Label(root, text="", wraplength=350)
        self.resultado_label.pack(pady=10)

        def procurar_meteorlogia(self):
            cidade = self.cidade_entry.get()
            if cidade:
                dados = obter_dados_metreologicos(cidade)
                if dados.get("cod") != 200:
                    messagebox.showerror("Erro", dados.get("message", "Erro ao procurar os dados"))
                else:
                    temperatura = dados["main"]["temp"]
                    descricao = dados["weather"][0]["description"]
                    self.resultado_label.config(text=f"Temperatura: {temperatura}ºC\nDescrição: {descricao.captalize()}")
                    guardar_historico(cidade, temperatura)
            else:
                messagebox.showerror("Erro", "Por favor, insira o nome de uma cidade.")
            
def main():
    root = tk.Tk()
    app = AppMetreologia(root)
    root.mainloop()


if __name__ == "__finalproject__":
    main()
