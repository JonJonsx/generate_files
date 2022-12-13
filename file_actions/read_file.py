import pandas as pd


def read_file_csv(file_name):
    if file_name.count("dm") == 0:
        return pd.read_csv(f"./input_files/{file_name}.csv")
    else:
        return pd.read_csv(f"./raw_files/dm/{file_name}.csv")


class ReadFile:
    def __init__(self):
        pass

    def read_idd(self):
        df = read_file_csv("IDD_2021")
        df.columns = ["ANO", "CODIGO_DA_AREA", "AREA_DE_AVALIACAO", "GRAU_ACADEMICO", "CODIGO_DA_IES", "NOME_DA_IES","SIGLA_DA_IES", "ORGANIZACAO_ACADEMICA", "CATEGORIA_ADMINISTRATIVA", "CODIGO_DO_CURSO",
                      "MODALIDADE_DE_ENSINO", "CODIGO_DO_MUNICIPIO", "MUNICIPIO_DO_CURSO", "SIGLA_DA_UF",
                      "N_DE_CONCLUINTES_INSCRITOS", "N_DE_CONCLUINTES_PARTICIPANTES",
                      "N_DE_CONCLUINTES_PARTICIPANTES_COM_NOTA_NO_ENEM",
                      "PROPORCAO_DE_CONCLUINTES_PARTICIPANTES_COM_NOTA_NO_ENEM", "NOTA_BRUTA_IDD", "IDD_CONTINUO",
                      "IDD_FAIXA", "OBSERVACAO"]

        df = df[
            ["AREA_DE_AVALIACAO", "GRAU_ACADEMICO", "SIGLA_DA_IES", "NOME_DA_IES", "MUNICIPIO_DO_CURSO", "SIGLA_DA_UF",
             "ORGANIZACAO_ACADEMICA",
             "CATEGORIA_ADMINISTRATIVA",
             "MODALIDADE_DE_ENSINO",
             "IDD_CONTINUO", "IDD_FAIXA", "ANO",
             "N_DE_CONCLUINTES_INSCRITOS", "N_DE_CONCLUINTES_PARTICIPANTES",
             "N_DE_CONCLUINTES_PARTICIPANTES_COM_NOTA_NO_ENEM",
             "PROPORCAO_DE_CONCLUINTES_PARTICIPANTES_COM_NOTA_NO_ENEM", "NOTA_BRUTA_IDD"]]

        return df

    def read_prouni(self):
        df = read_file_csv("PROUNI")
        df = df[['NOME_IES_BOLSA', 'trim(MUNICIPIO_BENEFICIARIO)',
                      'TIPO_BOLSA', 'NOME_CURSO_BOLSA', 'NOME_TURNO_CURSO_BOLSA', 'REGIAO_BENEFICIARIO',
                      'trim(UF_BENEFICIARIO)', 'RACA_BENEFICIARIO', 'MODALIDADE_ENSINO_BOLSA', 'SEXO_BENEFICIARIO',
                      'DATA_NASCIMENTO',
                      'IS_BENEFICIARIO_DEFICIENTE_FISICO', 'ANO_CONCESSAO_BOLSA']]
        return df

    def read_inmet_sp(self):
        df = read_file_csv("INMET_SP")
        return df

    def read_fies(self):
        df = read_file_csv("FIES")
        df = df[['UF_RESIDENCIA', 'MUNICIPIO_RESIDENCIA', 'ETNIA_COR', 'TIPO_ESCOLA_ENSINO_MEDIO', 'NOME_DA_IES',
                 'ORGANIZACAO_ACADEMICA_DA_IES', 'MUNICIPIO_DA_IES', 'UF_DA_IES', 'NOME_CURSO', 'TURNO_CURSO',
                 'GRAU_CURSO',
                 'IS_ONCLUIU_CURSO_SUPERIOR', 'PESSOAL_COM_DEFICIENCIA', 'ANO_PROCESSO_SELETIVO',
                 'SEMESTRE_PROCESSO_SELETIVO', 'SEXO_DO_ESTUDANTE', 'DATA_NASCIMENTO',
                 'QTDE_MEMBROS_GRUPO_FAMILIAR', 'RENDA_FAMILIAR_MENSAL_BRUTA', 'RENDA_MENSAL_BRUTA_PER_CAPITA',
                 'MEDIA_NOTA_ENEM', 'ANO_DO_ENEM', 'NOTA_REDACAO', 'NOTA_MATEMATICA_E_SUAS_TECNOLOGIAS',
                 'NOTA_LINGUAGENS_E_CODICOS_E_SUAS_TECNOLOGIAS',
                 'NOTA_CIENCIA_NATUREZA_E_SUAS_TECNOLOGIAS',
                 'NOTA_CIENCIA_HUMANAS_E_SUAS_TECNOLOGIAS', 'SITUACAO_INSCRICAO_FIES',
                 'PERCENTUAL_DE_FINANCIAMENTO', 'SEMESTRE_DO_FINANCIAMENTO',
                 'QTDE_SEMESTRE_FINANCIADO', 'DATA_PROCESSAMENTO']]
        df = df.rename(columns={'UF_DA_IES': 'SIGLA_DA_UF'})
        return df

    def read_enem_itens_prova(self):
        df = read_file_csv("ENEM_ITENS_PROVA")
        return df

    def read_enem_microdados(self):
        df = read_file_csv("ENEM_MICRODADOS")
        return df

    # DIMENSOES

    def read_dm_categoria_administrativa(self):
        df = read_file_csv("dm_categoria_administrativa")
        return df

    def read_dm_curso(self):
        df = read_file_csv("dm_curso")
        return df

    def read_dm_estado(self):
        df = read_file_csv("dm_estado")
        return df

    def read_dm_etinia(self):
        df = read_file_csv("dm_etinia")
        return df

    def read_dm_grau_academico(self):
        df = read_file_csv("dm_grau_academico")
        return df

    def read_dm_grau_curso(self):
        df = read_file_csv("dm_grau_curso")
        return df

    def read_dm_instituicao_de_ensino(self):
        df = read_file_csv("dm_instituicao_de_ensino")
        return df

    def read_dm_modalidade_de_ensino(self):
        df = read_file_csv("dm_modalidade_de_ensino")
        return df

    def read_dm_municipio(self):
        df = read_file_csv("dm_municipio")
        return df

    def read_dm_organizacao_academica(self):
        df = read_file_csv("dm_organizacao_academica")
        return df

    def read_dm_regiao(self):
        df = read_file_csv("dm_regiao")
        return df

    def read_dm_tipo_bolsa(self):
        df = read_file_csv("dm_tipo_bolsa")
        return df

    def read_dm_tipo_escola(self):
        df = read_file_csv("dm_tipo_escola")
        return df

    def read_dm_turno(self):
        df = read_file_csv("dm_turno")
        return df

    def read_dm_modalidade_ensino(self):
        df = read_file_csv("dm_modalidade_de_ensino")
        return df

    def read_fat_fies(self):
        return pd.read_csv(f"./raw_files/fat/fat_fies.csv")

    def read_fat_prouni(self):
        return pd.read_csv(f"./raw_files/fat/fat_prouni.csv")

    def read_fat_idd(self):
        return pd.read_csv(f"./raw_files/fat/fat_idd.csv")