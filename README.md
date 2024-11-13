# Mutant DNA API
Esta aplicación es una API REST diseñada para responder a un enunciado que solicita proveer de un endpoint para analizar secuencias de ADN y determinar si un ser humano es un mutante, según ciertos patrones en su ADN.

## Tecnologías

- **Lenguaje:** Python
- **Framework:** Flask

## Índice

- [Instalación](#instalación)
- [Configuración](#configuración)
- [Ejecución](#ejecución)
- [Endpoints](#endpoints)

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/GerardoDR/py-mutant-dna-api.git

    ```
2. Ingresa al directorio del proyecto:
    ```bash
    cd py-mutant-dna-api
    ```
3. Crea el archivo .venv
    ```bash
    py -3 -m venv .venv
    ```
4. Activa el ambiente
    - Windows:
    ```bash
    .venv\Scripts\activate
    ```
    - Linux/MacOS
    ```bash
    . .venv/bin/activate
    ```
5. Instala las dependencias:
    ```bash
    pip -r requirements.txt
    ```
## Ejecución

1. Opción de aplicación local (mínima):
    ```bash
    python -m flask --app server run
    ```
2. Si confias en los usuarios en tu red podés disponibilizar el servidor públicamente agregando --host=0.0.0.0 a la linea de comando:
    ```bash
    python -m flask --app server run --host=0.0.0.0
    ```
3. El servidor correrá en http://127.0.0.1:5000 por defecto.
## Endpoints

1. #### URL: ``` /mutant```
- Método: POST
- Descripción: Verifica si una secuencia de ADN pertenece a un mutante.
- Body: (matriz NxN compuesta por caracteres los caracteres: "A","C","G","T" )
    ```
    {
    "dna": ["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"]
    }
    ```
