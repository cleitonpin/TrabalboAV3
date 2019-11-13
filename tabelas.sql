CREATE TABLE campeonatos(
    cod_campeonato serial PRIMARY KEY,
    nome varchar(150) not null,
    data_inicio date not null,
    data_fim date not null,
    categoria varchar(50)
);

create table usuarios (
	telefone varchar(100),
	id_usuario serial primary key,
	email varchar(100) not null,
	usuario varchar(13) not null,
	senha varchar(100) not null,
	datanasc date not null
);
CREATE TABLE partidas(
    cod_partidas serial primary key,
    data_inicis_partidas date not null,
    hora_partidas time not null,
    local_partidas varchar(60) not null,
    cod_Campeonato int references campeonatos(cod_Campeonato)
);


create table equipes(
	nomeEquipe varchar(100) not null,
	cod_equipe SERIAL PRIMARY KEY,
	toplaner varchar (100) not null,
	midlaner varchar (100) not null,
	jungler varchar (100) not null,
	atirador varchar (100) not null,
	suport varchar (100) not null,
	reservas varchar (100),
	treinador varchar (100) not null
);
	
create table OrganizadorPessoa(
	id_pessoa SERIAL PRIMARY KEY,
	nome varchar(100) not null,
	contato varchar (100) not null,
	endereço varchar (100) not null
);
		
create table PessoaJuridica(
	id_pessoa int references OrganizadorPessoa(id_pessoa),
	cnpj varchar(100) not null
);
	
create table PessoaFisica(
	id_pessoa int references OrganizadorPessoa(id_pessoa),
	cpf varchar(100) not null
);

create table timecampeonato(
	cod_campeonato integer references campeonatos(cod_campeonato),
	cod_equipe integer references equipes(cod_equipe),
	vitorias integer,
	derrotas integer

);