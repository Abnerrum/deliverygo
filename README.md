# DeliveryGo 🍔🛵

Aplicação web de delivery desenvolvida em **Python + Flask**, com três perfis de acesso: **cliente, restaurante e entregador**. O projeto demonstra o fluxo completo de um pedido, do cardápio à entrega e avaliação.

## Funcionalidades

### Cliente
- Cadastro e login
- Busca de restaurantes e produtos
- Cardápio por categorias
- Carrinho com alteração de quantidade
- Checkout
- PIX, cartão e dinheiro simulados
- Histórico de pedidos
- Acompanhamento do status do pedido
- Avaliação após a entrega

### Restaurante
- Login próprio
- Painel de pedidos
- Abrir/fechar loja
- Categorias e produtos
- Disponibilidade dos produtos
- Fluxo: pendente → aceito → em preparo → pronto
- Indicadores básicos de pedidos e faturamento

### Entregador
- Login próprio
- Online/offline
- Visualização de entregas disponíveis
- Aceite da entrega
- Retirada do pedido
- Saída para entrega
- Confirmação da entrega
- Histórico

## Stack
- Python
- Flask
- Flask-SQLAlchemy
- Flask-Login
- Flask-SocketIO
- SQLite
- HTML5 / CSS3 / JavaScript
- Bootstrap 5
- pytest
- PyInstaller

## Estrutura

```text
deliverygo/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes/
│   │   ├── auth.py
│   │   ├── customer.py
│   │   ├── restaurant.py
│   │   └── driver.py
│   ├── static/
│   │   ├── css/style.css
│   │   └── js/app.js
│   └── templates/
│       ├── auth/
│       ├── customer/
│       ├── restaurant/
│       └── driver/
├── tests/
├── INICIAR.bat
├── build_exe.bat
├── desktop_launcher.py
├── config.py
├── run.py
├── seed.py
├── requirements.txt
├── requirements-dev.txt
└── README.md
```

## 🚀 Executar com um clique no Windows

Tenha o **Python 3.11+** instalado e habilitado no PATH. Depois dê duplo clique em:

```text
INICIAR.bat
```

Na primeira execução, o script cria o ambiente virtual, instala as dependências, cria/popula o SQLite caso ainda não exista, inicia o Flask e abre automaticamente:

```text
http://127.0.0.1:5000
```

Nas próximas execuções o ambiente e o banco existente são preservados.

## Execução manual

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python seed.py
python run.py
```

## Contas de demonstração

| Perfil | E-mail | Senha |
|---|---|---|
| Cliente | cliente@demo.com | 123456 |
| Restaurante | restaurante@demo.com | 123456 |
| Entregador | entregador@demo.com | 123456 |

## Fluxo para demonstração

1. Entre como cliente e faça um pedido.
2. Em outra janela, entre como restaurante e avance o pedido para **Aceito → Em preparo → Pronto**.
3. Entre como entregador, aceite a entrega e avance para **Saiu para entrega → Entregue**.
4. Volte ao cliente e envie uma avaliação.

## 🧪 Testes

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.\.venv\Scripts\python.exe -m pytest -v
```

A suíte cobre autenticação, login inválido, carrinho, checkout, mudanças de status e o fluxo completo até a avaliação.

## Gerar executável Windows

Execute primeiro `INICIAR.bat` e depois:

```text
build_exe.bat
```

O PyInstaller gera:

```text
dist\DeliveryGo\DeliveryGo.exe
```

## Screenshots

A seção de screenshots pode receber imagens em `docs/screenshots/` conforme a interface evoluir.

## Observações

O pagamento deste MVP é **simulado** e nenhuma cobrança real é efetuada. SQLite é utilizado para facilitar desenvolvimento e demonstração. Para produção, recomenda-se PostgreSQL, variáveis de ambiente para segredos, CSRF, HTTPS, rate limiting, logs e testes adicionais.

## Autor

Desenvolvido por **Abner Luiz** como projeto de estudo e portfólio em desenvolvimento backend e aplicações web.
