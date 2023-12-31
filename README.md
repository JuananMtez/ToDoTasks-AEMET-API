## About the project

This project entails the design and implementation of a software solution based on web services, utilizing Docker microservices. The architectural framework comprises the following key modules:

1. REST API as a Common Gateway:

- Functions as a unified access point to the software infrastructure.
- Provides endpoints for seamless communication with the AEMET API.
2. Task Management Microservice:

- Manages the creation, storage, and retrieval of tasks as defined by platform users.
Exposes a REST API to facilitate interaction with its functionality.

This project delves into the realm of microservices architecture, emphasizing the importance of a centralized REST API for streamlined access. Additionally, the gateway extends its functionality by offering endpoints for efficient communication with the AEMET API. The dedicated microservice focuses on task management, contributing to a robust and scalable software solution.


### Overall architecture
<p align="center" >
  <img width="500" src="https://github.com/JuananMtez/ToDoTasks-AEMET-API/assets/86200289/660d0a42-40cc-49b6-bbd3-37a6ef9683cf" alt="Sublime's custom image"/>
</p>

### Gateway server

It is responsible for establishing communication with the rest of the servers, showing the user the result or data that the other servers have provided.

### Tasks server

It is responsible for allowing users to register a "TO DO" style task system. Each task in turn can be decomposed in different subtasks, or also named as checklists

### Built With
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)


### Prerequisites
* Python 3.8 or superior
* Docker


### Installation
1. Clone the repo.
```sh
git clone https://github.com/JuananMtez/ToDoTasks-AEMET-API.git
```

2. Go to the root folder.
```sh
cd ToDoTasks-AEMET-API
```

3. Initialize Docker containers
```sh
docker-compose up -d
```

### Usage

1. Using browser, open ```http:localhost:8080/docs```


## Author

* **Juan Antonio Martínez López** - [Website](https://juananmtez.github.io/) - [LinkedIn](https://www.linkedin.com/in/juanantonio-martinez/)




## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
