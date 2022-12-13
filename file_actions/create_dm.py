import numpy as np

from file_actions.read_file import ReadFile
from file_actions import create_file


class SepareteColumns():
    def __init__(self):
        self.read_file = ReadFile()
        self.fat_prouni = self.read_file.read_prouni()
        self.fat_idd = self.read_file.read_idd()
        self.fat_fies = self.read_file.read_fies()
        self.lista_dms = [
            {"dm_modalidade_de_ensino": ["id_modalidade_de_ensino", "modalidade_de_ensino"]},
            {"dm_grau_academico": ["id_grau_academico", "grau_academico"]},
            {"dm_curso": ["id_curso", "nome_curso"]},
            {"dm_organizacao_academica": ["id_organizacao_academica", "organizacao_academica"]},
            {"dm_categoria_administrativa": ["id_categoria_administrativa", "categoria_administrativa"]},
            {"dm_instituicao_de_ensino": ["id_instituicao_de_ensino", "nome_da_ies"]},
            {"dm_estado": ["id_estado", "sigla_da_uf"]},
            {"dm_municipio": ["id_municipio", "municipio"]},
            {"dm_tipo_bolsa": ["id_tipo_bolsa", "tipo_bolsa"]},
            {"dm_regiao": ["id_regiao", "regiao"]},
            {"dm_etinia": ["id_etinia", "etinia"]},
            {"dm_tipo_escola": ["id_tipo_escola", "tipo_escola"]},
            {"dm_turno": ["id_turno", "turno"]},
            {"dm_grau_curso": ["id_grau_curso", "grau_curso"]},
            {"dm_situacao_inscricao_fies": ["id_situacao_inscricao_fies","situacao_inscricao_fies"]}
        ]

    def generic_create_dimension(self, file_columns, posicao):
        if len(file_columns) == 1:

            create_file.CreateFile(file_columns.dropna(axis=0, how='all').unique(),
                                   list(self.lista_dms[posicao].keys())[0],
                                   list(self.lista_dms[posicao].values()))
        else:
            create_file.CreateFile(file_columns.dropna(axis=0, how='all').drop_duplicates(),
                                   list(self.lista_dms[posicao].keys())[0],
                                   list(self.lista_dms[posicao].values()))

    def call_create_dimension(self):
        self.generic_create_dimension(self.fat_idd["MODALIDADE_DE_ENSINO"], 0)
        self.generic_create_dimension(self.fat_idd["GRAU_ACADEMICO"], 1)
        self.generic_create_dimension(self.fat_prouni["NOME_CURSO_BOLSA"], 2)
        self.generic_create_dimension(self.fat_idd["ORGANIZACAO_ACADEMICA"], 3)
        self.generic_create_dimension(self.fat_idd["CATEGORIA_ADMINISTRATIVA"], 4)
        self.generic_create_dimension(self.fat_fies[["NOME_DA_IES"]], 5)
        self.generic_create_dimension(self.fat_idd["SIGLA_DA_UF"], 6)
        self.generic_create_dimension(self.fat_idd["MUNICIPIO_DO_CURSO"], 7)
        self.generic_create_dimension(self.fat_prouni["TIPO_BOLSA"], 8)
        self.generic_create_dimension(self.fat_prouni["REGIAO_BENEFICIARIO"], 9)
        self.generic_create_dimension(self.fat_prouni["RACA_BENEFICIARIO"], 10)
        self.generic_create_dimension(self.fat_fies["TIPO_ESCOLA_ENSINO_MEDIO"], 11)
        self.generic_create_dimension(self.fat_fies["TURNO_CURSO"], 12)
        self.generic_create_dimension(self.fat_fies["GRAU_CURSO"], 13)
        self.generic_create_dimension(self.fat_fies["SITUACAO_INSCRICAO_FIES"], 14)
