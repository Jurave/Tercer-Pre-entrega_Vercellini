Autor: Julia
Nombre: Julia Vercellinii

Objetivo del TP presentado:
1. Desarrollar web en Django con el patrón MVT:
2 Subir a Github, compartir link para poder entregar el TP.
3. El poryecto tiene que tener herencia de HTML, bloques templates.
4. Tres clases al menos
5. Formulario para insertar clases de los modelos
6. Un formaulario para buscar algo en la base de datos (earch)
7. Readme, que explique el orden de las pruebas.
8. Entregara con nombre

Formato: link al repositorio de Github con el nombre "Tercera Pre-entrega + Apellido"

Seguidamente se describen los pasos a seguir para realizar las pruebas y las distintas consideraciones sobre el TP:

Se desarrollo una web en Django con el patron MVT, sobre un proyecto a desarrollar, que se trata de una herramienta que permite guardar en un único lugar el contenido de las distinta redes sociales que uno utiliza, sin necesidad de estar buscándolo individualmente en cada una de ellas.
El proyecto cuenta con herencia de HTML, bloques, templats, y tres clases- 
A su vez se diseñaron los formularios para cada una de clases, y se puede realizar una búsqueda a partir del email el usuario

Seguidamente se detallan los pasos a seguir para las pruebas:

En el menú de inicio (http://127.0.0.1:8000/miaplicacion/) se podrá visualizar en la parte superior el "Inicio" y los siguientes accesos:

* Usuarios
* Categorías
* Poteos
+ Administracion

A su vez se realizaron modificaciones de imágenes y textos asociados al proyecto.

Seguidamente se detallarán las funcionalidades por cada de las opciones del menú:

1. Usuarios:
a. Ingeso a usuarios: se puede verificar herencia de templates, el titulo de la sección: "Ususarios", se colocó el  nombre de la seccion "Listado de Usuarios" y una tabla con la información de los usuarios existentes (algunos cargados a partir de la base biblioteca.db  del DBBrowser)..
b. Formulario: accediendo a http://127.0.0.1:8000/miaplicacion/usuarios_form2/, se visualizan los datos para la carga de un nuevo usuario. Se ingresan los datos en el formulario, una vez enviados los datos la página nos redirecciona a la página principal y luego ingreando en usuarios se podrá visualizar los datos ingresados.
    En forms.py se definió una clase de formulario para usuarios, y que se creo en la aplicación, se creó un un nuevo campo que no se encontraban en la tabla original, este es el campo: Sexo.
    En caso de no completar el nombre del usuario e email, el sistema requerirá su carga obligatoria para poder avanzar.

2. Categorías:
a. Ingeso a Categorías: se puede verificar herencia de templates, el titulo de la sección: "Cateogorias", se colocó el  nombre de la seccion "Listado de Categorías" y debajo del encabezado se puede visualaiz la tabla con la información del contenido de las categorías existentes (algunos cargados a partir de la base biblioteca.db  del DBBrowser)..
b. Formulario: accediendo a http://127.0.0.1:8000/miaplicacion/categorias_form2/, se visualizan los datos para la carga de una nueva categoría. Se ingresan los datos en el formulario, una vez enviados los datos la página nos redirecciona a la página principal y luego ingreando en categorías se podrá visualizar los datos ingresados.
    En forms.py se definió una clase de formulario para categorías, y se creó un un nuevo campo que no se encontraban en la tabla original y que se detectó era necesario a futuro, este es el campo es : Categoría elegida.
    En caso de no completar algunos de los campos que se encuentran en el formulario, el sistema requerira de su carga obligatoria para avanzar en la creación de la categoría requerida.

3. Posteos:
a. Ingeso a Posteos: se puede verificar herencia de templates, el titulo de la sección: "Posteos", se colocó el  nombre de la seccion "Listado de Posteos" y debajo del encabezado se puede visualaiz la tabla con la información del contenido de los posteos existentes (algunos cargados a partir de la base biblioteca.db  del DBBrowser).
b. Formulario: accediendo a http://127.0.0.1:8000/miaplicacion/posteos_form2/, se visualizan los datos para la carga de un nuevo posteo. Se ingresan los datos en el formulario, una vez enviados los datos la página nos redirecciona a la página principal y luego ingreando en posteos se podrá visualizar los datos ingresados.
    En forms.py se definió una clase de formulario para posteos, en caso de querer a futuro realizar alguna modificacion sobre el mismo podremos realizarlo directamente desde aquí.
    En caso de no completar algunos de los campos que se encuentran en el formulario, el sistema requerira de su carga obligatoria para avanzar en la creación de la categoría requerida.


4. Búsqueda: se relizó un búsqueda a partir de email, para que el sistema nos traiga la información del usuario: para acceder a la búsqueda hay que ingresar a:
http://127.0.0.1:8000/miaplicacion/buscar_email/
Colocando un email de la base de usuarios se podrá visualizar el resultado de la búsqueda. Probar con: jb@gmail.com
En el resultado de la búsqueda se puede visualizar la herencia del template de la página de inicio.  
En caso de no ingresar un mail en la búsqueda el sistema arrojará el siguiente mensaje: "No se ingresaron datos para buscar!"

5. Administración:
a. Se creo el usuario: admin y la contraseña 12345, el sistema nos alertó acerca de lo frágil de la contraseña pero para este ejercicio se dejó esa clave.
b. Dentro de administración se podrán visualizar las siguientes secciones:
    Autenticación y autorización: alli se podrá ver al usuario admin a quien se le asignó y nombre, apellido e email. y se selecionaron los Permisos que se requerian para el mismo.
    MiAplicación: en esta sección se pueden visualizar las distintas categorías de la aplicación: ingresando en cada una se podrá observar:
    Usuarios: ingresando se visualiza el nombre de los usuarios, e ingresando en alguno de los usuarios podremos acceder a la información completa del mismo, pudiendo realizar algún cambio guardarlo y que este luego se actualice en nuestra tabla.
    Posteos: ingresando se visualiza el nombre de los posteos, e ingresando en alguno de los posteos  podremos acceder a la informacción completa del posteo, pudiendo realizar algun cambio, guardarlo y que este luego se actualice en nuestra tabla.
    Categorias: ingresando se visualiza el nombre de las categorías, e ingresando en alguno de ellas podremos acceder a la informacción completa de la misma, pudiendo realizar algun cambio, guardarlo y que este luego se actualice en nuestra tabla.
    Eliminar datos: en caso de querer eliminar algun registro de Usuarios, Posteos o Categorías, el sistema preguna previo a eliminarlo si deseamos hacerlo, en caso de estar seguros de hacerlo se procede a su elminación.

    
