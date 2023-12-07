import os
import re

def is_valid_email(email):
    # Usar uma expressão regular para verificar se o email tem um formato válido
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)

def processar_resposta(resposta, nome):
    # Utilizar uma estrutura de dados, como um dicionário, para mapear respostas a mensagens correspondentes
    mensagens = {
        '1': ("Problema: Atualizações de Definições de Vírus Desatualizadas",
              "Mensagem de Solução: É necessário a atualização do software, para isso vá nos três pontos no canto superior esquerdo, clique em 'Atualizar software' e após 'Atualizar'."),
        '2': ("Problema: Problemas de Desempenho do Sistema",
              "Mensagem de Solução: Se você notar que o sistema está mais lento, tente ajustar as configurações de escaneamento em segundo plano ou agendar escaneamentos em horários mais convenientes."),
        '3': ("Problema: Falso Positivo",
              "Mensagem de Solução: Às vezes, antivírus pode ter falsos positivos. Você pode adicionar o arquivo à lista de exclusões para evitar que ele seja detectado erroneamente."),
        '4': ("Problema: Instalação ou Atualização Mal-sucedida",
              "Mensagem de Solução: Certifique-se de que seu sistema atenda aos requisitos do antivírus e tente reinstalar ou atualizar o programa."),
        '5': ("Problema: Bloqueio de Sites Seguros",
              "Mensagem de Solução: Verifique as configurações do antivírus e, se necessário, adicione os sites à lista de exceções, para isso, vá na aba permitir site e digite o URL do site desejado."),
        '6': ("Problema: Problemas de Licença ou Ativação",
              "Mensagem de Solução: Certifique-se de que sua licença está atualizada e ativada. Se necessário, siga as instruções de ativação fornecidas pelo provedor."),
        '7': ("Problema: Incapacidade de Remoção de Malware",
              "Mensagem de Solução: Recomendo executar uma verificação completa do sistema e, se o problema persistir, entre em contato com o suporte técnico."),
        '8': ("Problema: Bloqueio de Arquivos Legítimos",
              "Mensagem de Solução: Verifique o histórico de quarentena e restaure os arquivos bloqueados que você acredita serem seguros."),
        '0': encerrar_chat
    }

    # Utilizar o método get para lidar com respostas não mapeadas
    mensagem = mensagens.get(resposta, ('', 'Digite apenas 1, 2, 3, 4, 5, 6, 7 ou 8'))
    print(mensagem[0])
    print(mensagem[1] if mensagem[0] else '')

def processar_sistema_travando(nome):
    while True:
        opcao = input(f'{os.linesep}{nome}, qual desses problemas mais se encaixa com o seu atual?{os.linesep}'
                      f'[1] - Definições de Vírus Desatualizadas{os.linesep}'
                      f'[2] - Problemas de Desempenho do Sistema{os.linesep}'
                      f'[3] - Falso Positivo{os.linesep}'
                      f'[4] - Instalação ou Atualização Mal-sucedida{os.linesep}'
                      f'[5] - Bloqueio de Sites Seguros{os.linesep}'
                      f'[6] - Problemas de Licença ou Ativação{os.linesep}'
                      f'[7] - Incapacidade de Remoção de Malware{os.linesep}'
                      f'[8] - Bloqueio de Arquivos Legítimos{os.linesep}'
                      f'[0] - Voltar ao menu principal{os.linesep}')

        if opcao == '0':
            break

        processar_resposta(opcao, nome)

def encerrar_chat():
    print('O chat foi encerrado. Caso precise de mais ajuda, entre em contato conosco posteriormente.')
    exit()

def start():
    while True:
        # Pedir o nome e verificar se é composto apenas por letras
        nome = input('Digite seu nome: ')
        if not nome.replace(" ", "").isalpha():
            print('Nome deve conter apenas letras. Tente novamente.')
            continue

        # Pedir o CPF e verificar se tem 11 dígitos
        cpf = ""
        while len(cpf) != 11:
            cpf = input('Digite seu CPF (apenas números, 11 dígitos): ')
            if len(cpf) != 11 or not cpf.isdigit():
                print('CPF deve conter exatamente 11 dígitos numéricos.')

        email = ""
        while not is_valid_email(email):
            email = input('Digite seu e-mail: ')
            if not is_valid_email(email):
                print('E-mail deve ter um formato válido.')

        print('Olá! Bem-vindo ao chat da Lumus')

        while True:
            resposta = input(f'Em que posso ajudar?{os.linesep}'
                             f'[1] - Atualizações de Definições de Vírus Desatualizadas{os.linesep}'
                             f'[2] - Problemas de Desempenho do Sistema{os.linesep}'
                             f'[3] - Falso Positivo{os.linesep}'
                             f'[4] - Instalação ou Atualização Mal-sucedida{os.linesep}'
                             f'[5] - Bloqueio de Sites Seguros{os.linesep}'
                             f'[6] - Problemas de Licença ou Ativação{os.linesep}'
                             f'[7] - Incapacidade de Remoção de Malware{os.linesep}'
                             f'[8] - Bloqueio de Arquivos Legítimos{os.linesep}'
                             f'[0] - Encerrar o chat{os.linesep}')

            if resposta == '0':
                encerrar_chat()

            processar_resposta(resposta, nome)

if __name__ == '__main__':
    start()
