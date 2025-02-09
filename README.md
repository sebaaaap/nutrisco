jonathan, descarga la imagen de postgres y pon: 

 docker run --name nutrisco -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=nutrisco -p 5432:5432 -d postgres

dps para ingresar a la bdd desde la misma terminal: 

 docker exec -it nutrisco bash
 psql -U postgres -d nutrisco

