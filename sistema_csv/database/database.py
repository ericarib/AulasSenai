import json #Lidar com arquivos JSON
from pathlib import Path # Lidas com os caminhos do windons 

class BancoFake:
    def __init__(self, arquivo_db ="banco.json"):
        self.arquivo_db = arquivo_db
        self.dados = {"clientes":[]} #clientes iniciando com vazio

        #Carregar valores anteriores salvos
        self._carregar()
    
    def _carregar(self):
        '''
        Carrega dados do arquivo JSON, se existir.
        Caso não exista, inicia o banco novo
        '''

        caminho = Path(self.arquivo_db)
        #Verifica se arquivo existe
        if caminho.is_file():
            #abrindo arquivo no modo leitura em UTF-8(pt-br)
            with open(caminho, 'r', encoding="utf-8") as arquivo:
                self.dados = json.load(arquivo)
        else:
            #chamar função para criar novo arquivo
            self._salvar()
    
    def _salvar(self):
        
        '''
        Salvar o conteudo do self.dados no JSON
        '''
        # abrir o arquivo no modo W (Escrita)
        with open(self.arquivo_db, "w",encoding="utf-8") as dados:
            #realizar um DUMP de PYTHON para JSON
            #ensure_ascii = False -> Escritas, emojis, mao viram código
            #indent = identação -> 4 recuo
            json.dump(self.dados, dados, ensure_ascii=False, indent=4)

    def adicionar_cliente(self,cliente_dict):
        self.dados['clientes'].append(cliente_dict)
        self._salvar()
    def listar_clientes(self):
        return self.dados['clientes']