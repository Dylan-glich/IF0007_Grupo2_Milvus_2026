-- =====================================================
-- IF0007 - Bases de Datos I
-- Grupo 2 - Milvus
-- Script PostgreSQL para comparación con Milvus
-- =====================================================

-- =====================================================
-- CREACIÓN DE LA BASE DE DATOS
-- =====================================================
-- Ejecutar una única vez.

CREATE DATABASE "Peliculas";

-- =====================================================
-- 1. CREACIÓN DE LA TABLA
-- =====================================================
CREATE TABLE "Pelicula" (
	"CI_IdPelicula" INT GENERATED ALWAYS AS IDENTITY,
	"CT_Titulo"    VARCHAR(100),
    "CT_Descripcion" TEXT,

    CONSTRAINT "PK_Pelicula" PRIMARY KEY ("CI_IdPelicula")
);

-- =====================================================
-- 2. INSERCIÓN DE DATOS
-- =====================================================
-- Se insertan las mismas películas utilizadas en
-- Milvus para que la comparación sea equivalente.

INSERT INTO "Pelicula" (
	"CT_Titulo",
	"CT_Descripcion"
	) 
	VALUES
		('Iron Man', 'Un millonario construye una armadura para convertirse en superheroe'),
		('Batman', 'Un hombre con traje de murcielago lucha contra el crimen en Gotham'),
		('El Rey Lion', 'Un cachorro de leon debe reclamar su reino en la selva africana'),
		('Titanic', 'Una historia de amor en un barco que se hunde en el oceano'),
		('Interstellar', 'Astronautas viajan a traves de un agujero de gusano para salvar la humanidad'),
		('Thor', 'Un dios nordico con un martillo lucha contra villanos en la Tierra'),
		('Frozen', 'Una princesa con poderes de hielo debe salvar a su reino'),
		('Gravity', 'Una astronauta queda atrapada sola en el espacio exterior'),
		('Romeo y Julieta', 'Dos jovenes de familias enemigas se enamoran perdidamente'),
		('Avengers', 'Un grupo de superheroes se une para salvar el mundo');
		
-- =====================================================
-- 3. CONSULTAS TRADICIONALES CON ILIKE
-- =====================================================
-- Estas consultas permiten comparar una búsqueda
-- basada en coincidencia textual con la búsqueda
-- semántica realizada por Milvus.

--======================================================
-- consulta 1: Superhéroes
--======================================================
SELECT "CT_Titulo", "CT_Descripcion"
	FROM "Pelicula"
		WHERE "CT_Titulo" ILIKE '%superheroe%'
		OR "CT_Descripcion" ILIKE '%superheroe%';
		
--======================================================
-- consulta 2: Amor
--======================================================
SELECT "CT_Titulo", "CT_Descripcion"
	FROM "Pelicula"
		WHERE "CT_Titulo" ILIKE '%amor%'
		OR "CT_Descripcion" ILIKE '%amor%';
		
--=======================================================
-- consulta 3: Espacio
--=======================================================
SELECT "CT_Titulo", "CT_Descripcion"
	FROM "Pelicula"
		WHERE "CT_Titulo" ILIKE '%espacio%'
		OR "CT_Descripcion" ILIKE '%espacio%';

		