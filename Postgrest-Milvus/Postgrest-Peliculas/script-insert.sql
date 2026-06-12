-- Insertamos las mismas peliculas que cargamos en milvus

INSERT INTO Pelicula (
	CT_Titulo,
	CT_Descripcion
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