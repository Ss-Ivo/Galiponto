# 🐔 Galiponto – Sistema de Gerenciamento Avícola
[https://galipo.vercel.app?_vercel_share=NXEWvQhYfPN7TThNoEUCqowqXdrEwizM](https://galipo-bnyncpyvg-iss-projects-c57e8e8f.vercel.app)
> ⚡ **TL;DR**  
> Plataforma **full stack** para gerenciamento avícola, com backend em **Flask**, frontend em **React + TypeScript** e banco de dados **PostgreSQL (Supabase)**.  
> Desenvolvido como projeto de portfólio e aplicação prática para resolver problemas reais de gestão.

---

## 🎯 Sobre o Projeto

O **Galiponto** é uma plataforma desenvolvida para o gerenciamento completo de granjas e pequenas produções avícolas.  
O sistema centraliza informações que normalmente ficam espalhadas em planilhas ou anotações manuais, permitindo **controle, análise e histórico** de dados.

O foco do projeto está em:
- domínio de regras de negócio reais
- organização de código
- boas práticas de desenvolvimento
- visão de produto

---

## 🧠 O que este projeto demonstra

- Desenvolvimento de **APIs REST** com Flask  
- Integração com **PostgreSQL via Supabase**  
- Modelagem de dados orientada ao domínio  
- Comunicação **frontend ↔ backend**  
- Organização de projeto **full stack**  
- Uso de **TypeScript** no frontend  
- Deploy em ambiente real (Vercel)  

---

## 🚀 Tecnologias Utilizadas

### Backend
- Python 3.11  
- Flask  
- Supabase (PostgreSQL)  
- Flask-CORS  
- Python-dotenv  

### Frontend
- React 18  
- TypeScript  
- Vite  
- Tailwind CSS  
- Lucide React  

---

## 📋 Funcionalidades

### 📊 Dashboard
- Visão geral do plantel  
- Métricas de produção  
- Alertas de saúde  
- Estatísticas mensais  

### 🐓 Gerenciamento de Galinhas
- Cadastro e edição de galinhas  
- Controle de entrada e saída  
- Identificação individual  
- Status ativo/inativo  

### 🥚 Produção de Ovos
- Registro diário de produção  
- Histórico por período  
- Métricas de produtividade  

### 🌽 Alimentação
- Registro de tipos de ração  
- Controle de quantidade e custos  
- Histórico de alimentação  
- Análise de custos  

### 💉 Saúde
- Registro de vacinas, doenças e tratamentos  
- Histórico por galinha  
- Custos veterinários  

### 📑 Relatórios
- Produção  
- Custos  
- Saúde  
- Exportação de dados  

---

## 🖥️ Demonstração

> ⚠️ **Atualmente o projeto não possui uma demo pública online.**  
> Prints ou vídeo de demonstração podem ser adicionados futuramente.

---

## 🛠️ Instalação e Execução

### Pré-requisitos
- Python 3.11+  
- Node.js 18+  
- npm ou yarn  
- Conta no Supabase  

---

### 🔧 Configuração do Supabase

1. Crie um projeto em https://supabase.com  
2. Execute o SQL disponível em:
```
supabase/migrations/20250924174153_summer_cave.sql
```
3. Copie a **URL do projeto** e a **chave anônima** em:
```
Settings > API
```

---

### 🐍 Backend (Flask)

```bash
git clone <repository-url>
cd farmchicken-backend
python -m venv venv
```

Ative o ambiente virtual:

Linux / Mac:
```bash
source venv/bin/activate
```

Windows:
```bash
venv\Scripts\activate
```

Instale as dependências:
```bash
pip install -r requirements.txt
```

Configure o arquivo `.env`:
```env
FLASK_ENV=development
SECRET_KEY=sua-chave-secreta
SUPABASE_URL=https://seu-projeto.supabase.co
SUPABASE_ANON_KEY=sua-chave-anonima
```

Execute o servidor:
```bash
python src/main.py
```

Backend disponível em:
```
http://localhost:5000
```

---

### ⚛️ Frontend (React)

```bash
cd project
npm install
npm run dev
```

Frontend disponível em:
```
http://localhost:5173
```

---

## 🔌 API Endpoints

### Galinhas
- GET `/api/chickens`  
- POST `/api/chickens`  
- PUT `/api/chickens/:id`  
- DELETE `/api/chickens/:id`  

### Produção de Ovos
- GET `/api/egg-production`  
- POST `/api/egg-production`  
- PUT `/api/egg-production/:id`  
- DELETE `/api/egg-production/:id`  

### Alimentação
- GET `/api/feeding`  
- POST `/api/feeding`  
- PUT `/api/feeding/:id`  
- DELETE `/api/feeding/:id`  

### Saúde
- GET `/api/health`  
- POST `/api/health`  
- PUT `/api/health/:id`  
- DELETE `/api/health/:id`  

---

## 🗄️ Banco de Dados

O banco foi modelado para representar entidades reais do domínio avícola:

- Galinhas  
- Produção de ovos  
- Alimentação  
- Saúde  

Utiliza UUID, controle de datas e relacionamentos entre tabelas.

---

## 🔒 Segurança

- Validação de dados no frontend e backend  
- Sanitização de inputs  
- CORS configurado  
- Row Level Security (RLS) no Supabase  
- Tratamento de erros  

---

## 📄 Licença

Este projeto está sob a licença **MIT**.

---

## 👤 Autor

Projeto desenvolvido para fins de aprendizado, portfólio e aplicação prática de conceitos de desenvolvimento full stack.
