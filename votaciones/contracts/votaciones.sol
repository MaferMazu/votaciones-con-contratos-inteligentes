// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.8.0;
import "./utils/Strings.sol";

contract Votaciones {
    // Esto declara estructuras para la votacion

    // Estrucutra de un votante
    struct Votante {
        string nombre; //nombre del votante
        string correo; //correo del votante
        bool voto; //si el votante voto
        uint presidente; //indice del presidente que eligio
        uint gobernador; //indice del gobernador que eligio
        uint localidad; //indice de la localidad del votante
        bool existe; //si el votante existe
    }

    // Estrucutra de un Candidato a Presidente o Gobernacion
    struct Candidato {
        address direccion; //direccion del candidato
        uint votos; //numero de votos
    }

    // Estructura de una localidad y su informacion
    struct Localidad {
        string nombre; //nombre de localidad
        uint[] candidatos; //indice candidatos a gobernadores en candidatos_todos
        uint poblacion; //num de votantes
        uint votantes; // num de votantes que ya ejercieron el voto

    }

    // Relaciona la direccion con un votante
    mapping(address => Votante) votantes;
    // Candidatos a la presidencia
    uint[] public candidatos_presidencia;
    mapping (address => bool) es_candidato;
    mapping(uint => bool) public es_candidato_presidencial;
    mapping(uint => bool) public es_candidato_gobernadores;
    Candidato[] public candidatos_todos;
    // Localidades
    Localidad[] public localidades;
    mapping(string => bool) localidad_existe;

    address public presidente;
    bool public votacionesCerradas;
    string[] resultado_final;


    constructor(){
        presidente = msg.sender;
        votacionesCerradas = false;
        // Informacion para votos nulos
        votantes[address(0x0)] = Votante({nombre: "Voto Nulo", correo: "-", voto: true, presidente: 0, gobernador: 0, localidad: 0, existe: true});
        candidatos_todos.push(Candidato({direccion: address(0x0), votos: 0}));
        candidatos_presidencia.push(0);
        es_candidato_presidencial[0] = true;
        es_candidato_gobernadores[0] = true;
    }

    function reinicializar() external {}


    function registrarLocalidades(string[] memory _localidades) external {
        require(presidente == msg.sender, "Solo el presidente puede registrar la localidad.");
        for (uint i = 0; i< _localidades.length; i++){
            require(!localidad_existe[_localidades[i]], "Alguna localidad ya existe.");
            uint[] memory mis_candidatos;
            localidades.push(Localidad({nombre: _localidades[i], candidatos: mis_candidatos, poblacion: 0, votantes:0}));
            uint index = localidades.length - 1;
            localidades[index].candidatos.push(0);
            localidad_existe[_localidades[i]] = true;
        }

    }

    function registrarVotante(address _direccion, string memory _nombre, string memory _correo, uint _localidad) external{
        require(presidente == msg.sender, "Solo el presidente puede registrar votante.");
        require(_localidad < localidades.length);
        Votante memory votante = votantes[_direccion];
        require(!votante.existe, "El votante ya existe.");
        votantes[_direccion] = Votante({nombre: _nombre, correo: _correo, voto: false, presidente: 0, gobernador: 0, localidad: _localidad, existe: true});
        localidades[_localidad].poblacion += 1;
    }

    function registrarCandidato(address _direccion, bool _presidencial) external {
        require(presidente == msg.sender, "Solo el presidente puede registrar candidato.");
        Votante storage mi_candidato = votantes[_direccion];
        require(mi_candidato.existe, "El candidato debe ser un votante.");
        require(!es_candidato[_direccion], "Ya es un candidato.");
        candidatos_todos.push(Candidato({direccion: _direccion, votos: 0}));
        uint index = candidatos_todos.length - 1;
        if (_presidencial){
            candidatos_presidencia.push(index);
            es_candidato_presidencial[index] = true;
        }
        else{
            uint localidad_candidato = mi_candidato.localidad;
            localidades[localidad_candidato].candidatos.push(index);
            es_candidato_gobernadores[index] = true;
        }
        es_candidato[_direccion]=true;

    }

    function votar(uint _presidente, uint _gobernador) external {
        require(!votacionesCerradas, "Votaciones cerradas.");
        require(_presidente < candidatos_todos.length, "El presidente debe ser un candidato.");
        require(_gobernador < candidatos_todos.length, "El gobernador debe ser un candidato.");
        require(es_candidato_presidencial[_presidente], "El presidente escogido debe ser candidato presidencial.");
        require(es_candidato_gobernadores[_gobernador], "El gobernador escogido debe ser candidato a gobernador.");
        Votante memory votante = votantes[msg.sender];
        require(votante.existe, "El votante no existe.");
        require(!votante.voto, "Ya voto.");
        Candidato memory goberna = candidatos_todos[_gobernador];
        address direccion_gobernador = goberna.direccion;
        Votante memory v_gobernador = votantes[direccion_gobernador];
        if (_gobernador != 0){
            require(v_gobernador.localidad == votante.localidad, "El gobernador y el votante deben ser de la misma localidad.");
            candidatos_todos[_gobernador].votos += 1;
        }
        if (_presidente!=0 ){  
            candidatos_todos[_presidente].votos += 1;
        }
        
        votantes[msg.sender].voto = true;
        votantes[msg.sender].presidente = _presidente;
        votantes[msg.sender].gobernador = _gobernador;
        localidades[votante.localidad].votantes +=1;

    }

    function cerrarVotaciones() external{
        require(presidente == msg.sender, "Solo el presidente puede cerrar la votacion.");
        votacionesCerradas = true;
    }

    function reportePresidencial() external view returns(string memory localidad, string memory nombre_ganador, uint votos, uint abstencion){
        uint poblacion = 0;
        uint _votantes = 0;
        for (uint i=0; i< localidades.length; i++){
            poblacion += localidades[i].poblacion;
            _votantes += localidades[i].votantes;
        }
        if (poblacion == 0){
            return ("Todas las localidades", "Nadie", 0, 0);
        }
        uint cuentaGanadora = 0;
        uint indexGanador = 0;
        for (uint i=0; i<candidatos_presidencia.length; i++){
            uint index = candidatos_presidencia[i];
            if (candidatos_todos[index].votos > cuentaGanadora){
                cuentaGanadora = candidatos_todos[index].votos;
                indexGanador = i;
            }
            
        }
        address dir = candidatos_todos[indexGanador].direccion;
        Votante memory votante = votantes[dir];
        
        uint _abstencion = 100 - (_votantes * 100 / poblacion);
        return ("Todas las localidades", votante.nombre, cuentaGanadora, _abstencion);
    }

    function reportePorLocalidad(uint _localidad) external view returns (string memory localidad, string memory nombre_ganador, uint votos, uint abstencion){
        if (localidades[_localidad].poblacion == 0){
            return (localidades[_localidad].nombre, "Nadie", 0, 0);
        }
        uint cuentaGanadora = 0;
        uint indexGanador = 0;
        for (uint i=0; i<localidades[_localidad].candidatos.length; i++){
            uint index = localidades[_localidad].candidatos[i];
            if (candidatos_todos[index].votos > cuentaGanadora){
                cuentaGanadora = candidatos_todos[index].votos;
                indexGanador = i;
            }
            
        }
        address dir = candidatos_todos[indexGanador].direccion;
        Votante memory votante = votantes[dir];
        uint _abstencion = 100 - (localidades[_localidad].votantes * 100 / localidades[_localidad].poblacion);
        return (localidades[_localidad].nombre, votante.nombre, cuentaGanadora, _abstencion);
    }

    function reporteTotal() external returns(string[] memory){
        require(votacionesCerradas, "Las votaciones siguen abiertas.");
        string memory localidad_nombre;
        string memory ganador_nombre;
        uint cuenta;
        uint abstencion;
        (localidad_nombre, ganador_nombre, cuenta, abstencion)= this.reportePresidencial();
        resultado_final.push(localidad_nombre);
        resultado_final.push(ganador_nombre);
        resultado_final.push(Strings.toString(cuenta));
        resultado_final.push(Strings.toString(abstencion));
        for (uint i=0; i<localidades.length; i++){
            (localidad_nombre, ganador_nombre, cuenta, abstencion)= this.reportePorLocalidad(i);
            resultado_final.push(localidad_nombre);
            resultado_final.push(ganador_nombre);
            resultado_final.push(Strings.toString(cuenta));
            resultado_final.push(Strings.toString(abstencion));
        }
        return resultado_final;
    }

    function reporteTotalLocalidad() external returns(string[] memory){
        for (uint i=0; i<localidades.length; i++){
            string memory localidad_nombre;
            string memory ganador_nombre;
            uint cuenta;
            uint abstencion;
            (localidad_nombre, ganador_nombre, cuenta, abstencion)= this.reportePorLocalidad(i);
            resultado_final.push(localidad_nombre);
            resultado_final.push(ganador_nombre);
            resultado_final.push(Strings.toString(cuenta));
            resultado_final.push(Strings.toString(abstencion));
        }
        return resultado_final;
    }
}