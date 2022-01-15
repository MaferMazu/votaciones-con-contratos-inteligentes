# Votación con contratos inteligentes
Proyecto 2

> Universidad Simón Bolívar
> Septiembre-Diciembre 2021

> María Fernanda Magallanes Zubillaga
> 13-10787


La tecnología blockchain surgió y la forma de tratar y pensar algunos problemas de centralización y seguridad cambiaron. La idea de tener una red peer-to-peer descentralizada, en donde los cambios se hacen bajo consenso de los involucrados y todo criptográficamente seguro hace que haya propuestas de usar esta tecnología para cosas como transacciones monetarias, almacenamiento de información (ejemplo médica) y votaciones transparentes.

Para este proyecto se desarrolló una aplicación que utiliza los conceptos de blockchain y contratos inteligentes para crear un escenario de votación seguro y transparente para la elección de presidentes y gobernadores. Se utilizó Solidity como lenguaje de programación del contrato inteligente; Python y librerías como Brownie para simular una red y un comportamiento automático del uso de este contrato; y algunas librerías como random y Faker para tener un comportamiento aleatorio y con datos de ejemplo.

## Funcionalidades y Requerimientos
Dentro del marco del proyecto se requirieron 4 partes del proyecto. Los generadores (de votantes y votos), con la posibilidad también de registrar votantes, candidatos y localidades; la segunda parte corresponde a la creación de los centros de votación; la tercera corresponde con la creación del contrato y las funcionalidades de inicializar el escenario, registrar localidades de votación, registrar votantes, registrar candidatos, votar, cerrar el proceso de votación, reportar los ganadores y dar reporte por localidad; y la cuarta parte de mostrar el resumen del proceso electoral.

De estos requerimientos se pudo completar casi todo a excepción de la segunda parte de creación de centros de votación, y la parte de generación de votos funciona pero esto no sucede en centros distintos de forma concurrente como lo piden los requerimientos.

## Contrato Inteligente
Este artefacto programado en Solidity es el que permite simular el comportamiento de una votación. El escenario de la votación asignado fue Elecciones de Gobernadores, y opcionalmente elecciones presidenciales de una vuelta.

El contrato tiene varias funcionalidades: inicializar el escenario, registrar localidades de votación, registrar votantes, registrar candidatos, votar, cerrar el proceso de votación, reportar los ganadores y dar reporte por localidad.

La implementación del mismo se basó en un ejemplo de un contrato de votaciones con delegación de votos propuesto en la documentación de Solidity (https://docs.soliditylang.org/en/v0.4.24/solidity-by-example.html#voting ); en donde se crearon estructuras de Solidity para representar a los votantes, los candidatos y las localidades; se crearon arreglos para almacenar todos los candidatos, y las localidades para poder acceder fácil a esa información a través de índices y poder guardar esa información en forma de entero y no como estructuras más complejas. También se decidió usar estructuras clave valor como los mappings para guardar información valiosa para ciertas verificaciones dentro del contrato; se tomó esta decisión pensando en que sería menos costoso preguntar por un índice en un mapping en vez de tener que recorrer arreglos de estructuras más complejas a pesar de saber que se está gastando en almacenamiento se ahorra en ejecución. Otras variables fueron almacenadas, como por ejemplo el presidente actual para limitar la ejecución de algunas acciones, el saber si las votaciones están cerradas y un arreglo de resultado_final que almacena una estructura generada por el reporte.

### Best Practice
Siguiendo las recomendaciones de mejores prácticas de los contratos inteligentes, se tuvo especial cuidado en que sea muy legible y autodocumentado, luego se tomó en consideración el tener código reusable, de buena calidad y lo más simple posible.

### Antipatrones
Para evitar antipatrones se tomaron ciertas consideraciones. Se tomó en cuenta constructors with care, asegurando que realmente el dueño del contrato sea la dirección que hace el deploy. Con respecto al antipatrón de re-entrada no se tuvo mucho problema porque la vulnerabilidad viene de hacer transferencias de manera pública o externas y en nuestro escenario no hay transferencias de este tipo, sin embargo se colocaron varias barreras de entrada en forma de require en las funciones para evitar comportamientos indeseados (como por ejemplo que una dirección que no es votante pueda votar), o que alguien que no sea el presidente no tenga capacidad de hacer registros. Con respecto al over/underflows, se tomó la consideración de trabajar con uint que internamente son uint256 por si la cantidad de datos en particular el número de votantes aumenta mucho de número poder soportarlo; además en Solidity a partir de las versiones 0.8.0 ya no son necesarias las librerías como SafeMath, ya viene incorporado
(https://docs.soliditylang.org/en/v0.8.11/080-breaking-changes.html#how-to-update-your-code ).

Con respecto a Race Conditions/ Front Running no se implementó nada especial dentro del contrato para prevenirlo, más que prevenir que se haga a lo mejor una consulta de resultados finales si todavía hay posibilidades de votar para mantener consistencia.

Antipatrones como Unexpected Ether, DELEGATECALL y unchecked call no fueron atacados directamente dentro del contrato porque dentro del escenario de votación trabajado no se tuvieron transferencias o llamadas a call dentro del contrato. Otros patrones como entropy illusion, block timestamp manipulation o external contract referencing fueron tomados en cuenta pero no implementados porque en la aplicación de votaciones no se usó nada que pudiera generar vulnerabilidades en esos aspectos.

## Información adicional

El repositorio donde se encuentra el código fuente es:
https://github.com/MaferMazu/votaciones-con-contratos-inteligentes 

Aquí una demostración de cómo usar la aplicación:
https://youtu.be/2EY4Ddcn8LQ

## Cosas interesantes
- En el contrato se puede hacer voto nulo (el índice que hay que colocar en la votación es 0) tanto por presidente como por gobernador, se cuenta como voto pero no se suma esta información al “candidato nulo”.
- Se sacrificó almacenamiento con varios mappings para salvar gas de ejecución de ciclos con estructuras más complejas.
- La forma de agregar localidades es con una lista de locaciones, pero si una de estas locaciones ya fue registrada anteriormente se revierte la operación del contrato.
- A pesar de saber que es mejor usar byte32 que son estructuras de tamaño estática en vez de strings dinámicos, se decidió usar strings para fines del proyecto para evitar algunas conversiones.

## Bibliografía
Mastering Ethereum. Andreas M. 2019. https://github.com/ethereumbook/ethereumbook 

Voting. Solidity by Example. Solidity Documentation. https://docs.soliditylang.org/en/v0.4.24/solidity-by-example.html#voting 

Brownie Documentation. https://eth-brownie.readthedocs.io/en/stable/toctree.html 
