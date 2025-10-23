# Ecommerce Project
Uma plataforma de ecommerce totalmente funcional, utilizando Python (django) para o back-end, Java para funcionalidades adicionais e HTML/CSS para o front-end. Esse projeto permite ao usuário procurar produtos, adicionar ao carrinho, realizar uma compra, para o administrador, permite criar novos produtos, ajustar tipo e quantidade, pedidos e usuários.


## Features
- Autenticação de Usuário: Registro, Log in e log out.

- Gerenciamento de Produtos: Administradores pode criar, editar e deletar produtos da plataforma.

- Sub-Categorias de produtos: Produtos pode ter sub-categorias, como um Smarphone nas versões de 128GB e 256GB.

- Carrinho de Compras: Usuários tem acesso a funcionalidade de carrinhos de compra, podendo adicionar diversos produtos ao carrinho.

- Histórico de Compras

- Design Responsivo: Utilizando HTML e CSS foi criado uma experiência funcional em qualquer dispositivo.

- Funcionalidade de Pesquisa

- Painel de Administrador: Usando a interface de administrador do Django, você tem todo o controle do site.

## Tecnologias Usadas
- Backend: Python (Django)

- Frontend: HTML, CSS

- Funcionalidades adicionais: Java

- Database: SQLite (default for development)

- Autenticação: Django Allauth

- Estilo: Custom CSS for a modern and responsive design

# Instalação
Passo-a-passo:

1. Clone o repositório:

```bash
git clone https://github.com/tiagordds/ecommmerce.git
cd ecommmerce
```

2. Crie um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```


4. Faça as mnigrações:

```bash
python manage.py migrate
```

5. Crie um superusuario (para acesso ao painel de administrador do Django):

```bash
python manage.py createsuperuser
```

6. Inicialize o servidor:

```bash
python manage.py runserver
```


7. Acesse:

### Abra o seu navegador e acesse http://127.0.0.1:8000/

### Acesso ao painel de administrador http://127.0.0.1:8000/admin/

# Screenshots
![ECCOMERCE_1](https://github.com/user-attachments/assets/9a3128d6-6083-4964-bcad-826d26209441)
![ECCOMERCE_2](https://github.com/user-attachments/assets/c2de156f-3b2f-4795-9e0a-d59e9cc2f0bd)
![ECCOMERCE_4](https://github.com/user-attachments/assets/ac8d46ca-9020-46c1-9f6e-d3896784752b)
![ECCOMERCE_3](https://github.com/user-attachments/assets/fd7f2799-6a15-4973-adbf-2f0b990e2204)


