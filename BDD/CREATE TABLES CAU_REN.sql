-- Table: public.cau_ren_cargas_trabajador

-- DROP TABLE public.cau_ren_cargas_trabajador;

CREATE TABLE IF NOT EXISTS CAU_REN_CARGAS_TRABAJADOR ( 
	CARGAS_TRABAJADOR_rut_carga_PK SERIAL PRIMARY KEY,
	rut_afil TEXT,
	nombre TEXT,
	direccion TEXT,
	comuna TEXT,
	ciudad TEXT,
	fono_part INT,
	est_afil TEXT,
	rut_carga TEXT,
	nombre_carga TEXT,
	parentesco TEXT,
	glosa TEXT,
	fch_extincion DATE
)
WITH (
  OIDS=FALSE
);

-- Table: public.cau_ren_causante_bloqueado

-- DROP TABLE public.cau_ren_causante_bloqueado;

CREATE TABLE IF NOT EXISTS CAU_REN_CAUSANTE_BLOQUEADO ( 
	CAUSANTE_BLOQUEADO_numero_registro_PK INT PRIMARY KEY,
	circular INT,
	fecha_circular DATE,
	causal SMALLINT,
	empresa_rut BIGINT,
	observacion TEXT,
	estado SMALLINT,
	causal_de_bloq SMALLINT,
	fecha_inicio DATE,
	fecha_de_termino DATE,
	rut_carga BIGINT,
	tipo_carga TEXT
)
WITH (
  OIDS=FALSE
);

-- Table: public.cau_ren_disminucion_sistema

-- DROP TABLE public.cau_ren_disminucion_sistema;

CREATE TABLE IF NOT EXISTS CAU_REN_DISMINUCION_SISTEMA ( 
	DISMINUCION_SISTEMA_rut_carga_PK BIGINT PRIMARY KEY,
	rut_afil BIGINT,
	fecha_disminucion DATE,
	causal_disminucion TEXT,
	usuario_grabacion TEXT
	
)
WITH (
  OIDS=FALSE
);


-- Table: public.cau_ren_rentas_por_mes_anio

-- DROP TABLE public.cau_ren_rentas_por_mes_anio;

CREATE TABLE IF NOT EXISTS CAU_REN_RENTAS_POR_MES_ANIO ( 
	RENTAS_POR_MES_ANIO_id_rentas_PK SERIAL PRIMARY KEY,
	mes TEXT,
	anio INT,
	porcentaje INT
)
WITH (
  OIDS=FALSE
);