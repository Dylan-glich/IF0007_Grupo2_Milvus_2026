CREATE TABLE Pelicula (
	CI_IdPelicula INT GENERATED ALWAYS AS IDENTITY,
	CT_Titulo     VARCHAR(100),
    CT_Descripcion TEXT,

    CONSTRAINT PK_Pelicula PRIMARY KEY (CI_IdPelicula)
);