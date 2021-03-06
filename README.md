# Votaciones con contratos inteligentes

Esta es una aplicaci贸n que utiliza Solidity y los conceptos de contratos inteligentes para crear un escenario de votaci贸n seguro y transparente de presidentes y gobernadores.

> Estado: 馃敡 Finalizado con detalles t茅cnicos

Video de c贸mo instalar y usar la aplicaci贸n: https://youtu.be/2EY4Ddcn8LQ

## 馃挕 Instalaci贸n 

```bash
python3 -m venv venv
source venv/bin/activate
make requirements
cd votaciones
```

## 馃攳 C贸mo probar las funcionalidades 
```bash
brownie run main
```

### Comandos
- Generar votantes

```bash
genVotante -f scripts/file_examples/micro.txt
```
- Generar votos aleatorios

> Nota: si se quiere modificar la abstenci贸n se puede hacer dentro del archivo scripts.main.py

```bash
genVotos
```

- Reporte por localidad

```bash
reportePorLocalidad <index>
```

Si el index no lo consigue agarra la localidad 0 por defecto.

- Reporte Presidencial

```bash
reportePresidencial
```

- Salir del programa

```bash
exit
```

## 馃捇 C贸mo interactuar con el contrato de forma manual
- Entrar a la red

```bash
brownie console
```

- Deploy del contrato

```bash
v = Votaciones.deploy({'from': accounts[0]})
```

- Diferentes funcionalidades

```bash
v.<nombreFuncion>(<argumentos>,{'from': <direccion_cuenta>})
```
En donde `<nombreFuncion>` puede ser una de las funciones del contrato; `<argumentos>` los argumentos de la funci贸n y la `<direccion_cuenta` es la direcci贸n para interactuar con el contrato.

**Funciones**
- registrarLocalidades

Registra localidades para la votaci贸n y toma como argumento una lista de strings.

- registrarVotante

Registra un votante a partir de una direcci贸n, un string de nombre, un string de correo y un entero positivo como el 铆ndice de la localidad.

- registrarCandidato

A partir de una direcci贸n de una cuenta que tiene que ser votante; y un booleano para saber si es un candidato presidencial se crea un candidato.

- votar

Toma como argumento dos enteros positivos; el primero el 铆ndice de la votaci贸n presidenial y el segundo el de gobernador.

- cerrarVotaciones

Cierra la posibilidad de votar.

**Reportes**

- reportePresidencial
- reportePorLocalidad: tiene un uint de argumento (indice de localidad)
- reporteTotal

> 馃搶 Para m谩s informaci贸n de c贸mo usar brownie console: https://eth-brownie.readthedocs.io/en/stable/quickstart.html#core-functionality
