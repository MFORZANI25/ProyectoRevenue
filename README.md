# ProyectoRevenue

DESCRIPCION
Se trata de un proyecto a implementarse en un área de Revenue Management de una empresa, que ayudaría a sus vendedores a obtener facilmente desde una app atraves de datos como numero de lista, sku y región los precios sugeridos de los distintos productos, los descuentos que hay para cada uno de ellos y finalmente el precio neto, que sería el costo que tendría ese SKU para el cliente. 

COMO CORRER PROYECTO
En primer lugar una vez que se hace fork en el mismo y lo corremos desde la terminal con python manage.py runserver entramos a http://127.0.0.1:8000/, a partir de este link hay dos opciones:
1. Loguearse a traves de: http://127.0.0.1:8000/admin/ (usuario: maria@hotmail.com y contraseña: maria, por ejemplo).
2. Tener una vista de la app, cuyas diferentes opciones son: http://127.0.0.1:8000/AppRevenue/arquitectura/ y así presionando sobre descuentos y precios netos ir pasando por los otros modelos y sus respectivas vistas (teniendo así 3 modelos con sus 3 vistas).
3. Ingresar datos a través de formularios a cada uno de los modelos: Modelo de Arquitecturas (http://127.0.0.1:8000/AppRevenue/arquitectura_formulario/), Modelo Descuentos (http://127.0.0.1:8000/AppRevenue/dto_formulario/) y Modelo Precio Neto (http://127.0.0.1:8000/AppRevenue/precioneto_formulario/).
4. Además, podemos hacer una busqueda en la Base de Datos a través del formulario desde: http://127.0.0.1:8000/AppRevenue/busquedaSKU/}

ASPECTOS ADICIONALES
La versión de django utilizada es 3.2.9

