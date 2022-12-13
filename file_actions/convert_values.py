import pandas as pd
from file_actions.read_file import ReadFile

class ConvertValues:
    def __init__(self):
        self.read_file = ReadFile()
        self.dm_estado = self.read_file.read_dm_estado()
        self.dm_curso = self.read_file.read_dm_curso()
        self.dm_municipio = self.read_file.read_dm_municipio()
        self.dm_organizacao_academica = self.read_file.read_dm_organizacao_academica()
        self.dm_categoria_administrativa = self.read_file.read_dm_categoria_administrativa()
        self.dm_grau_academico = self.read_file.read_dm_grau_academico()
        self.dm_modalidade_de_ensino = self.read_file.read_dm_modalidade_ensino()
        self.dm_instituicao = self.read_file.read_dm_instituicao_de_ensino()
        self.dm_tipo_bolsa = self.read_file.read_dm_tipo_bolsa()
        self.dm_turno = self.read_file.read_dm_turno()
        self.dm_regiao = self.read_file.read_dm_regiao()
        self.dm_etinia = self.read_file.read_dm_etinia()
        self.dm_tipo_bolsa = self.read_file.read_dm_tipo_bolsa()




    def convert_uf(self, df,columns):
        for index, i in enumerate(list(df[columns].dropna(axis=0, how='all'))):
            if i in list(self.dm_estado['sigla_da_uf']):
                # print(self.fat_idd['SIGLA_DA_UF'][index])
                df[columns][index] = \
                    self.dm_estado.loc[self.dm_estado['sigla_da_uf'] == i, 'id_estado'].item()

    def convert_curso(self, df,columns):
        for index, i in enumerate(list(df[columns].dropna(axis=0, how='all'))):
            if i in list(self.dm_curso['nome_curso']):
                # print(self.fat_idd['SIGLA_DA_UF'][index])
                df[columns][index] = \
                    self.dm_curso.loc[self.dm_curso['nome_curso'] == i, 'id_curso'].item()


