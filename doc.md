# Documentação

## Usuários

- Criar usuário

        POST /usuarios/
        body: {
            "email": "string",
            "empresa": "string",
            "senha": "string"
        }

        respostas:
          - 200: {
            "mensagem": "Usuário criado com sucesso",
            "usuario": {
                "id": 14,
                "email": "user13@email.com",
                "empresa": "foo"
            },
            "token": "282357d976aa6fe3222efda64afb9178f7f12550"
          }

          -409: {
            "mensagem": "Um usuário com este email já existe"
          }

- Login

        POST /usuarios/login/
        body: {
            "email": "string",
            "senha": "string"
        }

        respostas: 
        - 200: {
            "mensagem": "Login efetuado com sucesso",
            "token": "ea700ff50ad66d64c7ced3a3dfd893516730a767"
        }
        - 401: {
            "mensagem": "Usuário e/ou senha inválidos"
        }

- Logout

        POST /usuarios/logout/
        headers:
            - Authorization: Token <token>
        
        respostas:
        - 200: {
            "mensagem": "Logout realizado com sucesso"
        }
        - 401: {
            "detail": "Invalid token."
        }

- Deletar usuário

        DELETE /usuarios/
        headers:
            - Authorization: Token <token>
        
        respostas:
        - 200: {
            "mensagem": "Usuário deletado com sucesso"
        }
        - 401: {
            "detail": "Invalid token."
        }

## Empregados
- Listar

        GET /funcionarios/
        headers:
            - Authorization: Token <token>
        resposta:
        - 200: [
            {
                "id": 0,
                "nome": "string"
                "empresa": 0,
                "roupas": [],
            },
        ]

- Obter um funcionario pelo id

        GET /funcionarios/:id/
        headers:
            - Authorization: Token <token>

        resposta:
        - 200: {
            "id": 0,
            "nome": "string"
            "empresa": 0,
            "roupas": [],
        }

- Criar um funcionario

        POST /funcionarios/
        headers:
            - Authorization: Token <token>
        
        body: {
            "nome": "string"
        }

        resposta:
        - 200: {
            "id": 0,
            "nome": "string"
            "empresa": 0,
            "roupas": [],
        }
        - 400: {
            "nome": [
                "This field is required."
            ]
        }
        - 401: {
            "detail": "Invalid token."
        }

- Editar um funcionario

        PUT /funcionarios/:id/
        headers:
            - Authorization: Token <token>

        body: {
            "nome": "string"
        }

        resposta:
        - 200: {
            "id": 0,
            "nome": "string"
            "empresa": 0,
            "roupas": [],
        }
        - 400: {
            "nome": [
                "This field is required."
            ]
        }
        - 401: {
            "detail": "Invalid token."
        }
        - 404: {
            "detail": "Not found."
        }

- Deletar um funcionario

        DELETE /funcionarios/:id/
        headers:
            - Authorization: Token <token>

        resposta:
        - 204: (sucesso, sem corpo de resposta)
        - 401: {
            "detail": "Invalid token."
        }
        - 404: {
            "detail": "Not found."
        }

- Salvar preferencia de roupa

        PATCH /empregados/:id/salvar-preferencias/
        headers:
            - Authorization: Token <token>

        body: {
            "tipo": "string",
            "tamanho": 0,
            "cor": "#ffffff"
        }

        resposta:
        - 200: {
            "id": 0,
            "empresa": 0,
            "roupas": [
                {
                    "id": 0,
                    "tipo": "string",
                    "tamanho": 0,
                    "cor": "#ffffff"
                },
                {
                    "id": 0,
                    "tipo": "string",
                    "tamanho": 0,
                    "cor": "#ffffff"
                }
            ],
            "nome": "string"
        }
        - 401: {
            "detail": "Invalid token."
        }
        - 404: {
            "detail": "Not found."
        }
