# TFG_Miguel_Laloma
# TFG_Miguel_Laloma

Este proyecto configura un entorno de desarrollo local para WordPress utilizando Docker y Docker Compose.

## Requisitos

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Python](https://www.python.org/downloads/)

## Configuración

1. Levante los servicios de Docker:

```
    docker-compose up -d
```

2. Puede acceder al repositorio desde local host Accede a tu sitio de WordPress en tu navegador:
    
    http://localhost:8000

3. Para incorporar la funcionalidad del chatbot deben ejecutarse las siguientes instrucciones:
 
 Entrenamiento del modelo:
```
    make train
```

 Despliegue del servicio del chatbot:
```
    make chatbot
```

 Opcionalmente puede comprobarse el funcionamiento del modelo antes de desplegarse:
```
    make test
```

Adicionalmente es posible acceder a la instancia pública de la web a través del siguiente enlace:
    https://16.171.142.156/
