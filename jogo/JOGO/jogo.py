import tkinter as tk
from tkinter import messagebox


class StoryApp:
    
    def __init__(self, master):
        self.master = master
        master.title("Hogwarts")
        master.geometry("700x700")
        root.configure(bg='silver')

        self.story_pages = {#cada número representa uma página da história 
            1: {
                "text": "Você é um nascido trouxa e acaba de completar onze anos. Logo quando acorda, há uma carta à sua espera. A carta diz que você foi aceito(a) na Escola de Magia e Bruxaria de Hogwarts!:",
                "options": {#as opções te levam para o número que está posto no final, dependendo da opção o resultado muda
                    "SIM": 2,
                    "NÃO": 3
                }
            },
            2: {
                "text": "Muito bem, agora você vai precisar comprar o seu material. Você foi para o Beco Diagonal comprar os seus materiais escolares. Lista de material escolar:  Você tem que comprar livros, uma varinha, um caldeirão, uniforme e um animal de estimação de sua preferência",
                "options": {
                    "Ir comprar uma varinha": 4,
                    "Não ir comprar uma varinha": 8
                }
            },
            3: {
                "text": "Uma pena você ter recusado esse convite. SEU JOGO ACABOU!",
            },
            4: {
                "text": "Qual tipo de varinha você escolheu:.",
                "options": {
                    "fibra de coração de dragão": 5,
                    "pelo de unicórnio": 6,
                    "pena de fênix": 7
                }
            },
            5: {
                "text": "Os itens da compra são: Uniforme, caldeirão, bichinho, livros, varinha de fibra de coração de dragão",
                "options": {
                    "Ir para o Expresso Hogwarts": 9
                }
            },
            6: {
                "text": "Os itens da compra são: Uniforme, caldeirão, bichinho, livros, varinha de fibra de pelo de unicórnio",
                "options": {
                    "Ir para o Expresso Hogwarts": 9
                }
            },
            7: {
                "text": "Os itens da compra são: Uniforme, caldeirão, bichinho, livros, varinha de fibra de pena de fênix",
                "options": {
                    "Ir para o Expresso Hogwarts": 9
                }
            },
            8: {
                "text": "Não tem como ir sem uma varinha. Perde sua chance!",
            },
            9: {
                "text": "Agora você esta dentro do expresso de Hogwarts e esta procurando uma cabine para se acomodar. Os gêmeos ti convidam para ficar com eles na cabine. Você vai aceitar o convite? ",
                "options": {
                    "Sim": 10,
                    "Não": 11
                }
            },
            10: {
                "text": "Os gêmeos adoraram sua companhia, e viraram amigos",
                "options": {
                    "Ir para a seleção": 12
                }
            },
            11: {
                "text": "Você encontrou uma cabine vazia e ficou sozinho pelo resto do caminho",
                "options": {
                    "Ir para a seleção": 12
                }
            },

            12: {
                "text": "O expresso chegou a hogwarts, bem-vindo(a)!"
                "Ao chegar ao castelo, você é recebido(a) pelo Chapéu Seletor."
                "O Chapéu Seletor vai ajudá-lo(a) a ser selecionado(a) para uma das casas de Hogwarts.",
                "options": {
                    "Ser selecionado": 13
                }
            },
            
            13: {
                "text": "Em qual casa você deseja ser selecionado(a)? ",
                "options": {
                    "Sonserina": 14,
                    "Corvinal": 15,
                    "Lufa-Lufa": 16,
                    "Grifinória": 16
                }
            },
            
            14: {
                "text": "Parabéns! O Chapéu Seletor o selecionou para a casa Sonserina."
                "Você demonstra astúcia e determinação, com uma grande ambição.",
                "options": {
                    "Fim"
                }

            },
            15: {
                "text": "Parabéns! O Chapéu Seletor o selecionou para a casa Corvinal."
                "Você se destaca pela sua inteligência e sede de conhecimento.",
               
            },
            16: {
                "text": "Parabéns! O Chapéu Seletor o selecionou para a casa Lufa-Lufa."
                "Você se torna conhecido(a) pela sua lealdade e amizade.",

            },
            17: {
                "text": "Parabéns! O Chapéu Seletor o selecionou para a casa Grifinória."
                "Você mostra ser corajoso(a), determinado(a) e gostar de aventuras.",

            },  
        }

        self.current_page = 1

        self.story_text = tk.Text(master, wrap="word", height=6, width=40)
        self.story_text.pack(pady=10)
        self.update_story_text()

        self.option_buttons = []
        self.create_option_buttons()

    def update_story_text(self): # atualiza as opções 
        self.story_text.delete("1.0", tk.END)
        self.story_text.insert(tk.END, self.story_pages[self.current_page]["text"])

    def create_option_buttons(self): # cria os botões 
        for button in self.option_buttons:
            button.destroy()
        self.option_buttons = []

        options = self.story_pages[self.current_page]["options"] # permite ter opções, e serem levadas para as próximas páginas
        for option_text, next_page in options.items():
            button = tk.Button(self.master, text=option_text, command=lambda page=next_page: self.choose_option(page))
            button.pack(pady=8)
            self.option_buttons.append(button)

    def choose_option(self, next_page):
        if next_page in self.story_pages:
            self.current_page = next_page
            self.update_story_text()
            self.create_option_buttons()
            


if __name__ == "__main__":
    root = tk.Tk() 
    app = StoryApp(root)
    root.mainloop()

