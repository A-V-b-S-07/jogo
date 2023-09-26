import tkinter as tk


def inicio_game():
    status = ''
    while status != 'fim':
      compras = ['uniforme', 'caldeirão', 'bichinho', 'livros', 'varinha de']
      print("Você é um nascido trouxa e acaba de completar onze anos. Logo quando acorda, há uma carta à sua espera.")
      print("A carta diz que você foi aceito(a) na Escola de Magia e Bruxaria de Hogwarts!")

      while True:
          decisão = input("Você vai aceitar o convite? ")

          if decisão == 'sim':
              print("Muito bem, agora você vai precisar comprar o seu material.")
              break
          elif decisão == 'não':
              print("Uma pena você ter recusado esse convite. SEU JOGO ACABOU!")
              status = 'fim'
              break
          else:
              print("Opção inválida. Digite 'sim' ou 'não'.")

      if status == 'fim':
        break

      print("Agora você foi para o Beco Diagonal comprar os seus materiais escolares.")
      print("Lista de material escolar:")
      print("Você tem que comprar livros, uma varinha, um caldeirão, uniforme e um animal de estimação de sua preferência.")

      acao_compras = input("Opções: 1-Ir comprar uma varinha | 2-Não ir às compras: ")
      if acao_compras == "1":
          item = input("Qual tipo de varinha você escolheu: fibra de coração de dragão, pelo de unicórnio ou pena de fênix? ")
          if item == "fibra de coração de dragão" or item == "pelo de unicórnio" or item == "pena de fênix":
              compras.append(item)
              print("Os itens da compra são:", *compras)
          else:
              print("Item inválido, perdeu sua chance")
      elif acao_compras == '2':

          if len(compras) <= 0:
              print("Sem compras")
          else:
              print('Os itens da mochila são:', *compras)
              print("Não tem como ir sem uma varinha")
              continue
      else:
          print("Tente novamente")


      print("Agora você esta dentro do expresso de Hogwarts e esta procurando uma cabine para se acomodar")
      print("Os gêmeos ti convidam para ficar com eles na cabine")

      while True:
          expresso = input("Você vai aceitar o convite? ")

          if expresso == 'sim':
              print("Os gêmeos adoraram sua companhia, e viraram amigos")
              break

          elif expresso == 'não':
              print("você encontrou uma cabine vazia e ficou sozinho pelo resto do caminho")
              break


      print("o expresso chegou a hogwarts")
      print("bem-vindo(a)")
      print("Ao chegar ao castelo, você é recebido(a) pelo Chapéu Seletor.")
      print("O Chapéu Seletor vai ajudá-lo(a) a ser selecionado(a) para uma das casas de Hogwarts.")

      print("A sua primeira escolha é: Grifinória (G), Lufa-Lufa (L), Corvinal (C) ou Sonserina (S)?")

      while True:
          escolha = input("Em qual casa você deseja ser selecionado(a)? ").lower()

          if escolha == 'g':
              print("Parabéns! O Chapéu Seletor o selecionou para a casa Grifinória.")
              print("Você mostra ser corajoso(a), determinado(a) e gostar de aventuras.")
              status = 'fim'
              break
          elif escolha == 'l':
              print("Parabéns! O Chapéu Seletor o selecionou para a casa Lufa-Lufa.")
              print("Você se torna conhecido(a) pela sua lealdade e amizade.")
              status = 'fim'
              break
          elif escolha == 'c':
              print("Parabéns! O Chapéu Seletor o selecionou para a casa Corvinal.")
              print("Você se destaca pela sua inteligência e sede de conhecimento.")
              status = 'fim'
              break
          elif escolha == 's':
              print("Parabéns! O Chapéu Seletor o selecionou para a casa Sonserina.")
              print("Você demonstra astúcia e determinação, com uma grande ambição.")
              status = 'fim'
              break
          else:
              print("Opção inválida! Escolha novamente.")
      if status == 'fim':
        break
            # as escolhas de não estão dando errado

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Hogwarts")
    
    inicio_game()