🐔 Galiponto – Sistema de Gerenciamento Avícola
O Galiponto é uma plataforma full stack desenvolvida para o gerenciamento completo de granjas e pequenas produções avícolas.
O sistema permite registrar, acompanhar e analisar dados de plantel, produção de ovos, alimentação e saúde das aves, centralizando informações que normalmente ficam dispersas em planilhas ou anotações manuais.
Este projeto foi desenvolvido com foco em organização de código, domínio de regras de negócio reais e boas práticas de desenvolvimento, servindo também como projeto de portfólio.
 Objetivo do Projeto
Resolver problemas reais da gestão avícola, como:
Falta de controle histórico de produção
Dificuldade em acompanhar custos de alimentação e saúde
Ausência de relatórios claros para tomada de decisão
Centralização de dados em um único sistema acessível
 O que este projeto demonstra
Desenvolvimento de APIs REST com Flask
Integração com PostgreSQL via Supabase
Modelagem de banco de dados orientada ao domínio
Comunicação frontend ↔ backend
Organização de projeto full stack
Uso de TypeScript no frontend
Deploy em ambiente real (Vercel)
Estruturação de um sistema pensando em crescimento e manutenção
 Tecnologias Utilizadas
Backend
Python 3.11
Flask
Supabase (PostgreSQL)
Flask-CORS
Python-dotenv
Frontend
React 18
TypeScript
Vite
Tailwind CSS
Lucide React
 Funcionalidades
 Dashboard
Visão geral do plantel
Métricas de produção
Alertas de saúde
Estatísticas mensais
 Gerenciamento de Galinhas
Cadastro e edição de galinhas
Controle de entrada e saída
Identificação individual
Status ativo/inativo
🥚 Produção de Ovos
Registro diário de produção
Histórico por período
Métricas de produtividade
🌽 Alimentação
Registro de tipos de ração
Controle de quantidade e custos
Histórico de alimentação
Análise de custos
 Saúde
Registro de vacinas, doenças e tratamentos
Histórico por galinha
Custos veterinários
📑 Relatórios
Produção
Custos
Saúde
Exportação de dados
 Demonstração
 Atualmente o projeto não possui uma demo pública online.
(Opcionalmente, adicione aqui prints ou um link para vídeo.)
🛠️ Instalação e Execução
Pré-requisitos
Python 3.11+
Node.js 18+
npm ou yarn
Conta no Supabase
🔧 Configuração do Supabase
Crie um projeto em: https://supabase.com�
Execute o SQL disponível em:
Copiar código

supabase/migrations/20250924174153_summer_cave.sql
Copie a URL do projeto e a chave anônima em:
Copiar código

Settings > API
🐍 Backend (Flask)
Copiar código
Bash
git clone <repository-url>
cd farmchicken-backend
python -m venv venv
Ative o ambiente virtual:
Linux / Mac:
Copiar código
Bash
source venv/bin/activate
Windows:
Copiar código
Bash
venv\Scripts\activate
Instale as dependências:
Copiar código
Bash
pip install -r requirements.txt
Configure o .env:
Copiar código
Env
FLASK_ENV=development
SECRET_KEY=sua-chave-secreta
SUPABASE_URL=https://seu-projeto.supabase.co
SUPABASE_ANON_KEY=sua-chave-anonima
Execute o servidor:
Copiar código
Bash
python src/main.py
Backend disponível em:
Copiar código

http://localhost:5000
⚛️ Frontend (React)
Copiar código
Bash
cd project
npm install
npm run dev
Frontend disponível em:
Copiar código

http://localhost:5173
🔌 API Endpoints
Galinhas
GET /api/chickens
POST /api/chickens
PUT /api/chickens/:id
DELETE /api/chickens/:id
Produção de Ovos
GET /api/egg-production
POST /api/egg-production
PUT /api/egg-production/:id
DELETE /api/egg-production/:id
Alimentação
GET /api/feeding
POST /api/feeding
PUT /api/feeding/:id
DELETE /api/feeding/:id
Saúde
GET /api/health
POST /api/health
PUT /api/health/:id
DELETE /api/health/:id
🗄️ Modelagem do Banco de Dados
O banco de dados foi modelado para refletir entidades reais do domínio avícola:
Galinhas
Produção de ovos
Alimentação
Saúde
As tabelas utilizam UUID, controle de datas e relacionamento entre entidades.
🔒 Segurança
Validação de dados no frontend e backend
Sanitização de inputs
CORS configurado
Row Level Security (RLS) no Supabase
Tratamento de erros
📄 Licença
Este projeto está sob a licença MIT.
👤 Autor
Projeto desenvolvido para fins de aprendizado, portfólio e aplicação prática de conceitos de desenvolvimento full stack