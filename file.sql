-- TABELAS_IDD dimensoes e fato

create table dm_modalidade_de_ensino(
    id_modalidade_de_ensino int identity(1,1) not null,
    modalidade_de_ensino varchar(100) not null
)

create table dm_grau_academico(
    id_grau_academico int identity(1,1) not null,
    grau_academico varchar(100) not null
)

create table dm_curso(
    id_curso int identity(1,1) not null,
    curso varchar(100) not null,
)

create table dm_organizacao_academica(
    id_organizacao_academica int identity(1,1) not null,
    organizacao_academica varchar(100) not null
)

create table dm_categoria_administrativa(
    id_categoria_administrativa int identity(1,1) not null,
    categoria_administrativa varchar(100) not null
)

create table dm_instituicao_de_ensino(
    id_codigo_intituicao int identity(1,1) not null,
    nome_instituicao varchar(100) not null,
)

create table dm_estado(
    id_estado int identity(1,1) not null,
    sigla_da_uf varchar(2) not null,
    nome varchar(100) not null
)

create table dm_municipio(
    id_municipio int identity(1,1) not null,
    municipio varchar(100) not null
)

create table fat_idd(
	id_idd int identity(1,1) not null,
	id_curso int not null,
    id_codigo_intituicao int not null,
    id_municipio in not null,
    id_estado int not null,
    id_organizacao_academica int not null,
    id_categoria_administrativa int not null,
    id_grau_academico int,
    id_modalidade_de_ensino int,
    idd_continuo numeric(1,3),
    idd_faixa varchar(5),
    ano char(4) int not null,
    numero_concluintes int not null,
    numero_participantes int,
    numero_participantes_nota_enem int,
    proporcao_concluintes numeric(1,3),
    nome_bruta_idd numeric(1,3)
)

-- TABELAS FATO E DIMENSAO PROUNI

create table dm_tipo_bolsa(
    id_tipo_bolsa int identity(1,1) not null,
    tipo_bolsa varchar(50)
)

create table dm_turno(
    id_turno int identity(1,1) not null,
    turno varchar(50)
)

create table dm_regiao(
    id_regiao int identity(1,1) not null,
    regiao varchar(50)
)
create table dm_etinia(
    id_etinia int identity(1,1) not null,
    etinia  varchar(50)
)

create table dm_tipo_escola(
    id_tipo_escola int identity(1,1) not null,
    tipo_escola varchar(50)
)

create table dm_grau_curso(
    id_grau_curso int identity(1,1) not null,
    grau_curso varchar(50)
)

create table fat_prouni(
    id_fat_prouni int identity(1,1) not null,
    id_codigo_intituicao int,
    id_municipio int,
    id_tipo_bolsa int,
    id_curso int,
    id_turno int,
    id_regiao int,
    id_estado int,
    id_etinia int,
    modalidade_ensino_bolsa varchar(150),
    sexo_beneficiario varchar(2),
    data_nascimento DATE,
    beneficio_deficiente_fisico varchar(100),
    ano_concessao_bolsa varchar(4),
)

create table fat_fies(
    id_fies int identity(1,1) not null,
    id_uf_residencia int,--'UF_RESIDENCIA', id_uf_residencia
    id_municipio int,--'MUNICIPIO_RESIDENCIA', id_municipio
    id_etinia int,--'ETNIA_COR', id_etinia
    id_tipo_escola int,--'TIPO_ESCOLA_ENSINO_MEDIO', id_tipo_escola
    id_intituicao int,--'NOME_DA_IES', id_intituicao
    id_organizacao_academica int,--'ORGANIZACAO_ACADEMICA_DA_IES', id_organizacao_academica
    id_municipio_intituicao int,--'MUNICIPIO_DA_IES', id_municipio_intituicao
    id_uf_intituicao int,--'UF_DA_IES', id_uf_intituicao
    id_municipio_local_oferta int,--'MUNICIPIO_DO_LOCAL_DE_OFERTA', id_municipio_local_oferta
    id_uf_local_de_oferta int,--'UF_DO_LOCAL_DE_OFERTA', id_uf_local_de_oferta
    id_curso int,--'NOME_CURSO', id_curso
    id_turno int,--'TURNO_CURSO', id_turno
    id_grau_curso int,--'GRAU_CURSO', id_grau_curso
    is_oncluiu_curso_superior bit,--'is_oncluiu_curso_superior',
    pessoal_com_deficiencia bit,--'pessoal_com_deficiencia',
    ano_processo_seletivo varchar(4),--'ano_processo_seletivo',
    semestre_processo_seletivo varchar(4),--'semestre_processo_seletivo',
    sexo_do_estudante varchar(1),--'sexo_do_estudante',
    data_nascimento date,--'data_nascimento',
    qtde_membros_grupo_familiar int,--'qtde_membros_grupo_familiar',
    renda_familiar_mensal_bruta numeric(7,2),--'renda_familiar_mensal_bruta',
    renda_mensal_bruta_per_capita numeric(7,2),--'renda_mensal_bruta_per_capita',
    media_nota_enem numeric(6,2),--'media_nota_enem',
    ano_do_enem varchar(4),--'ano_do_enem',
    nota_redacao int,--'nota_redacao',
    nota_matematica_e_suas_tecnologias numeric(6,2),--'nota_matematica_e_suas_tecnologias',
    nota_linguagens_e_codicos_e_suas_tecnologias numeric(6,2),--'nota_linguagens_e_codicos_e_suas_tecnologias',
    nota_ciencia_natureza_e_suas_tecnologias numeric(6,2),--'nota_ciencia_natureza_e_suas_tecnologias',
    nota_ciencia_humanas_e_suas_tecnologias numeric(6,2),--'nota_ciencia_humanas_e_suas_tecnologias',
    situacao_inscricao_fies int,--'situacao_inscricao_fies',
    percentual_de_financiamento int,--'percentual_de_financiamento',
    semestre_do_financiamento int,--'semestre_do_financiamento',
    qtde_semestre_financiado int,--'qtde_semestre_financiado',
    data_processamento date,--'data_processamento'
)