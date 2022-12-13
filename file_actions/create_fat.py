from file_actions.read_file import ReadFile
from file_actions import create_file


class CreateFat:
    def __init__(self):
        self.read_file = ReadFile()
        self.fat_fies = self.read_file.read_fies()
        self.fat_idd = self.read_file.read_idd()
        self.fat_prouni = self.read_file.read_prouni()
        self.lista_fat = [
            {"fat_idd": ["id_idd", "id_curso", "id_codigo_intituicao", "id_municipio", "id_estado",
                         "id_organizacao_academica", "id_categoria_administrativa", "id_grau_academico",
                         "id_modalidade_de_ensino", "idd_continuo", "idd_faixa", "ano", "numero_concluintes",
                         "numero_participantes", "numero_participantes_nota_enem", "proporcao_concluintes",
                         "nome_bruta_idd"]},
            {"fat_prouni": ["id_fat_prouni", "id_codigo_intituicao", "id_municipio", "id_tipo_bolsa", "id_curso",
                            "id_turno",
                            "id_regiao", "id_estado", "id_etinia", "modalidade_ensino_bolsa", "sexo_beneficiario",
                            "data_nascimento", "beneficio_deficiente_fisico", "ano_concessao_bolsa"]},
            {"fat_fies": ["id_fies", "id_uf_residencia", "id_municipio", "id_etinia", "id_tipo_escola",
                          "id_intituicao", "id_organizacao_academica", "id_municipio_intituicao", "id_uf_intituicao",
                          "id_curso", "id_turno", "id_grau_curso",
                          "is_oncluiu_curso_superior", "pessoal_com_deficiencia", "ano_processo_seletivo",
                          "semestre_processo_seletivo", "sexo_do_estudante", "data_nascimento",
                          "qtde_membros_grupo_familiar", "renda_familiar_mensal_bruta", "renda_mensal_bruta_per_capita",
                          "media_nota_enem", "ano_do_enem", "nota_redacao", "nota_matematica_e_suas_tecnologias",
                          "nota_linguagens_e_codicos_e_suas_tecnologias", "nota_ciencia_natureza_e_suas_tecnologias",
                          "nota_ciencia_humanas_e_suas_tecnologias", "situacao_inscricao_fies",
                          "percentual_de_financiamento", "semestre_do_financiamento", "qtde_semestre_financiado",
                          "data_processamento"]},
        ]

    def generic_create_fat(self, file_columns, posicao):
        create_file.CreateFile(file_columns.drop_duplicates(),
                               list(self.lista_fat[posicao].keys())[0],
                               list(self.lista_fat[posicao].values()))

    def call_create_fat(self):
        self.generic_create_fat(
            self.fat_idd[[
                "AREA_DE_AVALIACAO", "NOME_DA_IES", "MUNICIPIO_DO_CURSO", "SIGLA_DA_UF", "ORGANIZACAO_ACADEMICA",
                "CATEGORIA_ADMINISTRATIVA", "GRAU_ACADEMICO",
                "MODALIDADE_DE_ENSINO",
                "IDD_CONTINUO", "IDD_FAIXA", "ANO",
                "N_DE_CONCLUINTES_INSCRITOS", "N_DE_CONCLUINTES_PARTICIPANTES",
                "N_DE_CONCLUINTES_PARTICIPANTES_COM_NOTA_NO_ENEM",
                "PROPORCAO_DE_CONCLUINTES_PARTICIPANTES_COM_NOTA_NO_ENEM", "NOTA_BRUTA_IDD"]], 0)
        self.generic_create_fat(self.fat_prouni[:], 1)
        self.generic_create_fat(self.fat_fies[:], 2)