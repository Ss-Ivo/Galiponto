import os
from supabase import create_client, Client
from typing import Optional

# Configurações do Supabase
SUPABASE_URL = os.getenv('SUPABASE_URL', 'https://your-project.supabase.co')
SUPABASE_KEY = os.getenv('SUPABASE_ANON_KEY', 'your-anon-key')

# Cliente global do Supabase
supabase: Optional[Client] = None

def init_supabase():
    """Inicializa o cliente do Supabase"""
    global supabase
    try:
        supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
        return supabase
    except Exception as e:
        print(f"Erro ao inicializar Supabase: {e}")
        return None

def get_supabase_client() -> Optional[Client]:
    """Retorna o cliente do Supabase"""
    global supabase
    if supabase is None:
        supabase = init_supabase()
    return supabase

# Tipos de dados
class SupabaseService:
    """Serviço para interagir com o Supabase"""
    
    def __init__(self):
        self.client = get_supabase_client()
    
    # Métodos para Galinhas
    async def get_chickens(self):
        """Busca todas as galinhas"""
        try:
            response = self.client.table('galinhas').select('*').order('created_at', desc=True).execute()
            return response.data
        except Exception as e:
            print(f"Erro ao buscar galinhas: {e}")
            return []
    
    async def create_chicken(self, chicken_data):
        """Cria uma nova galinha"""
        try:
            response = self.client.table('galinhas').insert(chicken_data).execute()
            return response.data[0] if response.data else None
        except Exception as e:
            print(f"Erro ao criar galinha: {e}")
            return None
    
    async def update_chicken(self, chicken_id, chicken_data):
        """Atualiza uma galinha"""
        try:
            response = self.client.table('galinhas').update(chicken_data).eq('id', chicken_id).execute()
            return response.data[0] if response.data else None
        except Exception as e:
            print(f"Erro ao atualizar galinha: {e}")
            return None
    
    async def delete_chicken(self, chicken_id):
        """Remove uma galinha"""
        try:
            response = self.client.table('galinhas').delete().eq('id', chicken_id).execute()
            return True
        except Exception as e:
            print(f"Erro ao remover galinha: {e}")
            return False
    
    # Métodos para Produção de Ovos
    async def get_egg_production(self):
        """Busca toda a produção de ovos"""
        try:
            response = self.client.table('producao_ovos').select('*').order('data', desc=True).execute()
            return response.data
        except Exception as e:
            print(f"Erro ao buscar produção de ovos: {e}")
            return []
    
    async def create_egg_production(self, production_data):
        """Cria um novo registro de produção"""
        try:
            response = self.client.table('producao_ovos').insert(production_data).execute()
            return response.data[0] if response.data else None
        except Exception as e:
            print(f"Erro ao criar produção: {e}")
            return None
    
    async def update_egg_production(self, production_id, production_data):
        """Atualiza um registro de produção"""
        try:
            response = self.client.table('producao_ovos').update(production_data).eq('id', production_id).execute()
            return response.data[0] if response.data else None
        except Exception as e:
            print(f"Erro ao atualizar produção: {e}")
            return None
    
    async def delete_egg_production(self, production_id):
        """Remove um registro de produção"""
        try:
            response = self.client.table('producao_ovos').delete().eq('id', production_id).execute()
            return True
        except Exception as e:
            print(f"Erro ao remover produção: {e}")
            return False
    
    # Métodos para Alimentação
    async def get_feeding(self):
        """Busca todos os registros de alimentação"""
        try:
            response = self.client.table('alimentacao').select('*').order('data', desc=True).execute()
            return response.data
        except Exception as e:
            print(f"Erro ao buscar alimentação: {e}")
            return []
    
    async def create_feeding(self, feeding_data):
        """Cria um novo registro de alimentação"""
        try:
            response = self.client.table('alimentacao').insert(feeding_data).execute()
            return response.data[0] if response.data else None
        except Exception as e:
            print(f"Erro ao criar alimentação: {e}")
            return None
    
    async def update_feeding(self, feeding_id, feeding_data):
        """Atualiza um registro de alimentação"""
        try:
            response = self.client.table('alimentacao').update(feeding_data).eq('id', feeding_id).execute()
            return response.data[0] if response.data else None
        except Exception as e:
            print(f"Erro ao atualizar alimentação: {e}")
            return None
    
    async def delete_feeding(self, feeding_id):
        """Remove um registro de alimentação"""
        try:
            response = self.client.table('alimentacao').delete().eq('id', feeding_id).execute()
            return True
        except Exception as e:
            print(f"Erro ao remover alimentação: {e}")
            return False
    
    # Métodos para Saúde
    async def get_health(self):
        """Busca todos os registros de saúde"""
        try:
            response = self.client.table('saude').select('*').order('data', desc=True).execute()
            return response.data
        except Exception as e:
            print(f"Erro ao buscar saúde: {e}")
            return []
    
    async def create_health(self, health_data):
        """Cria um novo registro de saúde"""
        try:
            response = self.client.table('saude').insert(health_data).execute()
            return response.data[0] if response.data else None
        except Exception as e:
            print(f"Erro ao criar saúde: {e}")
            return None
    
    async def update_health(self, health_id, health_data):
        """Atualiza um registro de saúde"""
        try:
            response = self.client.table('saude').update(health_data).eq('id', health_id).execute()
            return response.data[0] if response.data else None
        except Exception as e:
            print(f"Erro ao atualizar saúde: {e}")
            return None
    
    async def delete_health(self, health_id):
        """Remove um registro de saúde"""
        try:
            response = self.client.table('saude').delete().eq('id', health_id).execute()
            return True
        except Exception as e:
            print(f"Erro ao remover saúde: {e}")
            return False

