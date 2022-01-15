# Votaciones con contratos inteligentes

Esta es una aplicación que utiliza Solidity y los conceptos de contratos inteligentes para crear un escenario de votación seguro y transparente de presidentes y gobernadores.

> Estado: 🔧 En construcción


## 💡 Instalación 

```bash
python3 -m venv venv
source venv/bin/activate
make requirements
cd votaciones
```

## 🔍 Cómo probar las funcionalidades 
```bash
brownie run main
```

### Comandos
- Generar votantes

```bash
genVotante -f scripts/file_examples/micro.txt
```
- Generar votos aleatorios

> Nota: si se quiere modificar la abstención se puede hacer dentro del archivo scripts.main.py

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

## 💻 Cómo interactuar con el contrato de forma manual
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
En donde `<nombreFuncion>` puede ser una de las funciones del contrato; `<argumentos>` los argumentos de la función y la `<direccion_cuenta` es la dirección para interactuar con el contrato.

**Funciones**
- registrarLocalidades

Registra localidades para la votación y toma como argumento una lista de strings.

- registrarVotante

Registra un votante a partir de una dirección, un string de nombre, un string de correo y un entero positivo como el índice de la localidad.

- registrarCandidato

A partir de una dirección de una cuenta que tiene que ser votante; y un booleano para saber si es un candidato presidencial se crea un candidato.

- votar

Toma como argumento dos enteros positivos; el primero el índice de la votación presidenial y el segundo el de gobernador.

- cerrarVotaciones

Cierra la posibilidad de votar.

**Reportes**

- reportePresidencial
- reportePorLocalidad: tiene un uint de argumento (indice de localidad)
- reporteTotal

> 📌 Para más información de cómo usar brownie console: https://eth-brownie.readthedocs.io/en/stable/quickstart.html#core-functionality
