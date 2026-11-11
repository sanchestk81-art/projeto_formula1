# 🏁 Setor F1 — Portal, DataTable da Temporada & Fan Store Oficial

Plataforma web completa de **Fórmula 1**, desenvolvida em **Python** utilizando **Flask** para a camada web e **PostgreSQL** como banco de dados relacional.

> **Destaques de Arquitetura e Engenharia:**
> - **Zero ORM:** Todas as consultas, inserções, atualizações e exclusões são executadas diretamente com SQL nativo utilizando cursores (`psycopg2.extras.RealDictCursor`).
> - **Nova Identidade Visual:** Nova logo esportiva em alta definição do **Setor F1** aplicada no cabeçalho e favicon.
> - **Carrossel / Banner Rotativo na Home:** Slider que avança automaticamente a cada 5 segundos com notícias e produtos selecionados pelo administrador.
> - **DataTable dos Pilotos da Temporada:** Tabela interativa na página inicial com filtro rápido, pontos na temporada e probabilidade visual/chance de vencer o campeonato.
> - **Edição Total no Admin (`/admin`):** O administrador pode criar, **editar** e excluir notícias, corridas/resultados e produtos da loja.
> - **Gestão da Loja Oficial:** O admin cadastra produtos, adiciona fotos locais ou remotas, define tags especiais (*Mais Vendido*, *Edição Limitada*, *Nova Coleção*, *Exclusivo*) e integra com os banners da Home.

---

## 🗂️ Estrutura de Pastas e Arquivos

```text
formula1/
│
├── .env                  # Configurações do PostgreSQL e secret key do Flask
├── .env.example          # Modelo de configuração para novos ambientes
├── requirements.txt      # Dependências (Flask, psycopg2-binary, python-dotenv)
├── db.py                 # Conexão direta com PostgreSQL sem ORM
├── script.py             # DDL: Cria o banco e as 9 tabelas do Setor F1
├── data.py               # DML: Popula o banco com histórico, carros, pilotos com pontos, produtos com tags e banners
├── app.py                # Aplicação Flask completa com CRUDs, rotas e regras de negócio
├── README.md             # Documentação do projeto
│
├── static/
│   ├── images/
│   │   ├── logo.png      # Nova Logo Oficial em alta definição do Setor F1
│   │   ├── pilotos/      # Pasta para fotos locais de pilotos
│   │   ├── carros/       # Pasta para fotos de carros
│   │   ├── produtos/     # Pasta para fotos de produtos (com suporte a upload)
│   │   └── logos/        # Logos adicionais
│   ├── css/
│   │   └── style.css     # Estilos CSS com suporte a Carrossel, DataTable e Tags
│   └── js/
│       └── main.js       # Comportamentos interativos
│
└── templates/
    ├── base.html                 # Layout base com Nova Logo, Menu com pedidos/admin e rodapé
    ├── index.html                # Home: Carrossel Rotativo + DataTable de Pilotos + Notícias
    ├── noticia_detalhe.html      # Leitura completa da notícia
    ├── pilotos.html              # Grid de Pilotos com busca interativa (atuais e lendas)
    ├── piloto_detalhe.html       # Perfil detalhado de cada piloto
    ├── equipes.html              # Equipes com fotos dos carros (monopostos), motores e pilotos
    ├── corridas.html             # Corridas históricas (2020, SP corrigido), pódios com fotos e bandeiras
    ├── loja.html                 # Loja Oficial com tags especiais e modal de cadastro
    ├── meus_pedidos.html         # Área do fã para acompanhar compras realizadas
    ├── sobre.html                # Sobre o Setor F1 + Formulário de contato/feedback
    ├── mensagens.html            # Mural de feedbacks da comunidade
    ├── login.html                # Tela de Login do Setor F1
    ├── cadastro.html             # Cadastro de novos fãs
    ├── admin.html                # Painel Administrativo com abas e botões de ação
    ├── admin_editar_noticia.html # Tela para o admin editar notícias existentes
    ├── admin_editar_corrida.html # Tela para o admin editar corridas e resultados
    └── admin_editar_produto.html # Tela para o admin editar produtos, fotos e tags
```

---

## 🏎️ Principais Funcionalidades Implementadas

### 1. Nova Logo Oficial "Setor F1"
- Desenvolvida com design moderno inspirado no automobilismo de ponta (monoposto veloz, escudo em fibra de carbono com acabamento cromado e a tipografia marcante **SETOR F1**).
- Salva em [`static/images/logo.png`](file:///c:/Users/54040262867/OneDrive%20-%20SESISENAISP%20-%20Escolas/Documentos/DEV/formula1/static/images/logo.png).

### 2. Carrossel / Banner Rotativo na Home
- Slider automático que passa sozinho a cada 5 segundos na página inicial.
- Possui setas de navegação lateral (anterior/próximo), bolinhas indicadoras de slide e pausa inteligente ao passar o mouse.
- O administrador pode escolher exibir notícias ou produtos diretamente no carrossel, ou cadastrar banners personalizados no painel admin!

### 3. DataTable dos Pilotos da Temporada & Chances de Título
- Localizada na Home ([`index.html`](file:///c:/Users/54040262867/OneDrive%20-%20SESISENAISP%20-%20Escolas/Documentos/DEV/formula1/templates/index.html)), traz:
  1. **Posição (#):** Com destaque dourado para o líder, prata e bronze.
  2. **Piloto:** Foto, bandeira do país, número e nacionalidade.
  3. **Equipe:** Com badge estilizado na cor da equipe.
  4. **Pontos na Temporada:** Pontuação somada na tabela.
  5. **Chance de Vencer o Campeonato:** Barra de progresso visual colorida (Verde/Amarelo/Vermelho) com a porcentagem estatística de título.
  6. **Filtro em Tempo Real:** Campo de busca rápida no topo da tabela para filtrar por piloto ou equipe instantaneamente.

### 4. Edição de Corridas e Notícias no Painel Admin (Update)
- O administrador agora conta com botões **Editar ✏️** e **Excluir 🗑️** em cada notícia e corrida cadastrada.
- Formulários pré-preenchidos permitem corrigir resultados, pódios ou textos de notícias a qualquer momento, gravando tudo diretamente no PostgreSQL.

### 5. Gestão Completa da Loja Oficial pelo Admin (CRUD + Tags + Fotos)
- Na aba "🛍️ Loja & Produtos" do Painel Admin:
  - **Cadastrar Produto:** Nome, categoria, equipe associada, preço, descrição e estoque.
  - **Tags Especiais:** Seletor de tags com badges visuais:
    - 🔥 **Mais Vendido** (vermelho fogo)
    - ⭐ **Edição Limitada** (dourado ouro)
    - ✨ **Nova Coleção** (azul/ciano)
    - 💎 **Exclusivo** (roxo metálico)
  - **Fotos:** O admin pode **fazer upload de uma foto do próprio computador** ou informar uma URL da web!
  - **Editar e Excluir:** Botões para alterar preços, estoque, fotos e tags de qualquer produto.

---

## 🔑 Credenciais Padrão para Testes

| Perfil | E-mail | Senha | O que pode fazer |
|---|---|---|---|
| **Administrador** | `admin@setorf1.com` | `admin123` | Publicar e editar notícias, corridas, produtos com fotos/tags e banners |
| **Fã / Cliente** | `fa@setorf1.com` | `fa123` | Comprar na Loja Oficial e acompanhar pedidos |

---

## 🚀 Como Executar o Projeto

1. **Iniciar a aplicação Flask:**
   ```powershell
   python app.py
   ```
2. **Acessar no navegador:**
   👉 **[http://127.0.0.1:5000](http://127.0.0.1:5000)**
