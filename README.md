# FarmChicken Pro - Sistema de Gerenciamento Avícola

Sistema completo para gerenciamento de fazendas de galinhas, com controle de plantel, produção de ovos, alimentação e saúde dos animais.

## 🚀 Tecnologias

### Backend
- **Flask** - Framework web Python
- **Supabase** - Banco de dados PostgreSQL na nuvem
- **Flask-CORS** - Suporte a CORS
- **Python-dotenv** - Gerenciamento de variáveis de ambiente

### Frontend
- **React 18** - Biblioteca JavaScript
- **TypeScript** - Tipagem estática
- **Tailwind CSS** - Framework CSS
- **Lucide React** - Ícones
- **Vite** - Build tool

## 📋 Funcionalidades

### Dashboard
- Visão geral do plantel
- Métricas de produção
- Alertas de saúde
- Estatísticas mensais

### Gerenciamento de Galinhas
- Cadastro de galinhas
- Controle de entrada e saída
- Rastreamento por identificação
- Status ativo/inativo

### Produção de Ovos
- Registro diário de produção
- Controle por galinha produtora
- Histórico de produção
- Métricas de produtividade

### Controle de Alimentação
- Registro de tipos de ração
- Controle de quantidade e custos
- Histórico de alimentação
- Análise de custos

### Controle de Saúde
- Registro de vacinas
- Controle de doenças
- Tratamentos aplicados
- Custos veterinários

### Relatórios
- Relatórios de produção
- Análise de custos
- Relatórios de saúde
- Exportação de dados

## 🛠️ Instalação e Configuração

### Pré-requisitos
- Python 3.11+
- Node.js 18+
- npm ou yarn
- Conta no Supabase

### Configuração do Supabase

1. **Crie um projeto no Supabase**
   - Acesse https://supabase.com
   - Crie uma nova conta ou faça login
   - Crie um novo projeto

2. **Configure o banco de dados**
   - Execute o SQL do arquivo `supabase/migrations/20250924174153_summer_cave.sql`
   - Ou use o SQL Editor no dashboard do Supabase

3. **Obtenha as credenciais**
   - Vá em Settings > API
   - Copie a URL do projeto e a chave anônima

### Backend (Flask API)

1. **Clone o repositório**
```bash
git clone <repository-url>
cd farmchicken-backend
```

2. **Crie e ative o ambiente virtual**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

3. **Instale as dependências**
```bash
pip install -r requirements.txt
```

4. **Configure as variáveis de ambiente**
```bash
cp .env.example .env
# Edite o arquivo .env com suas credenciais do Supabase
```

Exemplo do arquivo `.env`:
```env
FLASK_ENV=development
SECRET_KEY=sua-chave-secreta-aqui
SUPABASE_URL=https://seu-projeto.supabase.co
SUPABASE_ANON_KEY=sua-chave-anonima-aqui
```

5. **Execute o servidor**
```bash
python src/main.py
```

O servidor estará disponível em `http://localhost:5000`

### Frontend (React)

1. **Navegue para o diretório do frontend**
```bash
cd ../project
```

2. **Instale as dependências**
```bash
npm install
```

3. **Execute em modo desenvolvimento**
```bash
npm run dev
```

O frontend estará disponível em `http://localhost:5173`

4. **Build para produção**
```bash
npm run build
```

## 🚀 Deploy no Vercel

### Preparação

1. **Build do frontend**
```bash
cd project
npm run build
```

2. **Copie os arquivos para o backend**
```bash
cp -r dist/* ../farmchicken-backend/src/static/
```

### Deploy

1. **Instale a CLI do Vercel**
```bash
npm i -g vercel
```

2. **Faça login no Vercel**
```bash
vercel login
```

3. **Deploy do projeto**
```bash
cd farmchicken-backend
vercel
```

4. **Configure as variáveis de ambiente no Vercel**
   - Acesse o dashboard do Vercel
   - Vá em Settings > Environment Variables
   - Adicione:
     ```
     FLASK_ENV=production
     SECRET_KEY=sua-chave-secreta-aqui
     SUPABASE_URL=https://seu-projeto.supabase.co
     SUPABASE_ANON_KEY=sua-chave-anonima-aqui
     ```

5. **Redeploy**
```bash
vercel --prod
```

## 📁 Estrutura do Projeto

```
farmchicken-backend/
├── src/
│   ├── lib/
│   │   └── supabase_client.py  # Cliente do Supabase
│   ├── routes/
│   │   └── chickens.py         # Endpoints da API
│   ├── static/                 # Frontend build
│   └── main.py                 # Aplicação principal
├── venv/                       # Ambiente virtual Python
├── requirements.txt            # Dependências Python
├── vercel.json                # Configuração do Vercel
├── .env.example               # Exemplo de variáveis de ambiente
└── README.md                  # Documentação

project/
├── src/
│   ├── components/            # Componentes React
│   ├── hooks/                # Custom hooks
│   ├── lib/                  # Utilitários e configurações
│   └── main.tsx              # Entrada da aplicação
├── dist/                     # Build de produção
├── package.json              # Dependências Node.js
└── vite.config.ts            # Configuração do Vite
```

## 🔧 API Endpoints

### Galinhas
- `GET /api/chickens` - Lista todas as galinhas
- `POST /api/chickens` - Cria nova galinha
- `PUT /api/chickens/:id` - Atualiza galinha
- `DELETE /api/chickens/:id` - Remove galinha

### Produção de Ovos
- `GET /api/egg-production` - Lista produção de ovos
- `POST /api/egg-production` - Registra nova produção
- `PUT /api/egg-production/:id` - Atualiza registro
- `DELETE /api/egg-production/:id` - Remove registro

### Alimentação
- `GET /api/feeding` - Lista registros de alimentação
- `POST /api/feeding` - Cria novo registro
- `PUT /api/feeding/:id` - Atualiza registro
- `DELETE /api/feeding/:id` - Remove registro

### Saúde
- `GET /api/health` - Lista registros de saúde
- `POST /api/health` - Cria novo registro
- `PUT /api/health/:id` - Atualiza registro
- `DELETE /api/health/:id` - Remove registro

## 🗄️ Schema do Banco de Dados (Supabase)

### Tabela: galinhas
```sql
CREATE TABLE galinhas (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  numero_identificacao text UNIQUE NOT NULL,
  data_entrada date NOT NULL,
  raca text NOT NULL,
  idade_entrada integer NOT NULL,
  origem text NOT NULL,
  ativa boolean DEFAULT true,
  created_at timestamptz DEFAULT now()
);
```

### Tabela: producao_ovos
```sql
CREATE TABLE producao_ovos (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  data date NOT NULL,
  quantidade integer NOT NULL,
  galinhas_produtoras text[] DEFAULT '{}',
  observacoes text DEFAULT '',
  created_at timestamptz DEFAULT now()
);
```

### Tabela: alimentacao
```sql
CREATE TABLE alimentacao (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  data date NOT NULL,
  tipo_racao text NOT NULL,
  quantidade_kg decimal(10,2) NOT NULL,
  custo decimal(10,2) NOT NULL,
  observacoes text DEFAULT '',
  created_at timestamptz DEFAULT now()
);
```

### Tabela: saude
```sql
CREATE TABLE saude (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  galinha_id uuid REFERENCES galinhas(id) ON DELETE CASCADE,
  data date NOT NULL,
  tipo text NOT NULL CHECK (tipo IN ('vacina', 'doenca', 'tratamento')),
  descricao text NOT NULL,
  custo decimal(10,2) DEFAULT 0,
  observacoes text DEFAULT '',
  created_at timestamptz DEFAULT now()
);
```

## 🎨 Design System

O sistema utiliza um design moderno e responsivo com:

- **Cores**: Paleta baseada em tons de verde (agricultura)
- **Tipografia**: Fontes system com boa legibilidade
- **Componentes**: Cards, botões e formulários consistentes
- **Responsividade**: Adaptado para desktop e mobile
- **Animações**: Transições suaves e micro-interações

## 📱 Responsividade

O sistema é totalmente responsivo e funciona em:
- Desktop (1024px+)
- Tablet (768px - 1023px)
- Mobile (320px - 767px)

## 🔒 Segurança

- Validação de dados no frontend e backend
- Sanitização de inputs
- CORS configurado adequadamente
- Tratamento de erros robusto
- Row Level Security (RLS) no Supabase

## 📊 Monitoramento

- Logs de erro detalhados
- Métricas de performance
- Alertas de saúde do sistema
- Dashboard do Supabase para monitoramento do banco

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 📞 Suporte

Para suporte técnico ou dúvidas sobre o sistema, entre em contato através dos issues do GitHub.

---

**FarmChicken Pro** - Sistema completo para gestão avícola moderna e eficiente com Supabase.

