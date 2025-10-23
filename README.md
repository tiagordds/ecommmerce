# Ecommerce Project
Uma plataforma de ecommerce totalmente funcional, utilizando Python (django) para o back-end, Java para funcionalidades adicionais e HTML/CSS para o front-end. Esse projeto permite ao usuário procurar produtos, adicionar ao carrinho, realizar uma compra, para o administrador, permite criar novos produtos, ajustar tipo e quantidade, pedidos e usuários.


## Features
- User Authentication: Register, log in, and log out functionality.
- Autenticação de Usuário: Registro, Log in e log out.

- Product Management: Admins can add, edit, and delete product.
- Gerenciamento de Produtos: Administradores pode criar, editar e deletar produtos da plataforma.

- Products Sub-Category: Products can have sub-categories, like Smartphones with 128GB and 256GB.
- Sub-Categorias de produtos: Produtos pode ter sub-categorias, como um Smarphone nas versões de 128GB e 256GB.

- Shopping Cart: Users can add products to their cart and proceed to checkout.
- Carrinho de Compras: Usuários tem acesso a funcionalidade de carrinhos de compra, podendo adicionar diversos produtos ao carrinho.

- Order History: Users can view past orders.
- Histórico de Compras

- Responsive Design: Built with HTML and CSS for a seamless experience on all devices.
- Design Responsivo: Utilizando HTML e CSS foi criado uma experiência funcional em qualquer dispositivo.

- Search Functionality: Search for products by name or category.
- Funcionalidade de Pesquisa

- Admin Panel: Manage users, products, and orders through the Django admin interface.
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


