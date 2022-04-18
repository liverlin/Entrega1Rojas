# Entrega Final

## Estructura del proyecto:
Rama principal: main
Apps: 
- AppCpder: 
Maneja los perfiles y cursos 
Permite realizar un CRUD con cursos

- Aula: Maneja la vision de las personas (alumnos y profesores), permite ver el listado de personas
Además de un CRUD con los profesores

## Vistas: 
- inicio: Pagina de inicio genérica
- Profesores: Permite añadir y acceder al listado de profesores ademas de editar (CRUD)
- Cursos: permite acceder al listado de cursos y editarlo (CRUD con clase de vistas )
- Estudiantes: Permite añadir estudiante y acceder al listado de alumnos
- EditarPerfil: Permite acceder a la informacion del usuario ademas de poder editar dicha informacion


## Plantillas:
- Inicio: 
Es la vista de entrada
Se muestra aquí los resultados de la busquesda de cursos
El mensaje del medio cambia dependiendo de si estas logueado o no 

- cursos , profesores, estudiantes: funcionalidades similares 
basicamente se encargan de mostrar el formulario y la herencia de la vista padre
