-- Consulta tradicional con ILIKE

-- consulta 1
SELECT CT_Titulo, CT_Descripcion
	FROM Pelicula
		WHERE CT_Titulo ILIKE '%superheroe%'
		OR CT_Descripcion ILIKE '%superheroe%';

-- consulta 2
SELECT CT_Titulo, CT_Descripcion
	FROM Pelicula
		WHERE CT_Titulo ILIKE '%amor%'
		OR CT_Descripcion ILIKE '%amor%';

-- consulta 3
SELECT CT_Titulo, CT_Descripcion
	FROM Pelicula
		WHERE CT_Titulo ILIKE '%espacio%'
		OR CT_Descripcion ILIKE '%espacio%';