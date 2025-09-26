from flask import Blueprint, request, jsonify
import asyncio
from src.lib.supabase_client import SupabaseService

chickens_bp = Blueprint('chickens', __name__)
supabase_service = SupabaseService()

def run_async(coro):
    """Helper para executar funções async em rotas síncronas"""
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    return loop.run_until_complete(coro)

# Rotas para Galinhas
@chickens_bp.route('/chickens', methods=['GET'])
def get_chickens():
    try:
        chickens = run_async(supabase_service.get_chickens())
        return jsonify(chickens)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@chickens_bp.route('/chickens', methods=['POST'])
def create_chicken():
    try:
        data = request.get_json()
        
        chicken_data = {
            'numero_identificacao': data['numero_identificacao'],
            'data_entrada': data['data_entrada'],
            'raca': data['raca'],
            'idade_entrada': data['idade_entrada'],
            'origem': data['origem'],
            'ativa': data.get('ativa', True)
        }
        
        chicken = run_async(supabase_service.create_chicken(chicken_data))
        
        if chicken:
            return jsonify(chicken), 201
        else:
            return jsonify({'error': 'Erro ao criar galinha'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@chickens_bp.route('/chickens/<chicken_id>', methods=['PUT'])
def update_chicken(chicken_id):
    try:
        data = request.get_json()
        
        chicken_data = {}
        if 'numero_identificacao' in data:
            chicken_data['numero_identificacao'] = data['numero_identificacao']
        if 'data_entrada' in data:
            chicken_data['data_entrada'] = data['data_entrada']
        if 'raca' in data:
            chicken_data['raca'] = data['raca']
        if 'idade_entrada' in data:
            chicken_data['idade_entrada'] = data['idade_entrada']
        if 'origem' in data:
            chicken_data['origem'] = data['origem']
        if 'ativa' in data:
            chicken_data['ativa'] = data['ativa']
        
        chicken = run_async(supabase_service.update_chicken(chicken_id, chicken_data))
        
        if chicken:
            return jsonify(chicken)
        else:
            return jsonify({'error': 'Galinha não encontrada'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@chickens_bp.route('/chickens/<chicken_id>', methods=['DELETE'])
def delete_chicken(chicken_id):
    try:
        success = run_async(supabase_service.delete_chicken(chicken_id))
        
        if success:
            return jsonify({'message': 'Galinha removida com sucesso'})
        else:
            return jsonify({'error': 'Erro ao remover galinha'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Rotas para Produção de Ovos
@chickens_bp.route('/egg-production', methods=['GET'])
def get_egg_production():
    try:
        production = run_async(supabase_service.get_egg_production())
        return jsonify(production)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@chickens_bp.route('/egg-production', methods=['POST'])
def create_egg_production():
    try:
        data = request.get_json()
        
        production_data = {
            'data': data['data'],
            'quantidade': data['quantidade'],
            'galinhas_produtoras': data.get('galinhas_produtoras', []),
            'observacoes': data.get('observacoes', '')
        }
        
        production = run_async(supabase_service.create_egg_production(production_data))
        
        if production:
            return jsonify(production), 201
        else:
            return jsonify({'error': 'Erro ao criar produção'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@chickens_bp.route('/egg-production/<production_id>', methods=['PUT'])
def update_egg_production(production_id):
    try:
        data = request.get_json()
        
        production_data = {}
        if 'data' in data:
            production_data['data'] = data['data']
        if 'quantidade' in data:
            production_data['quantidade'] = data['quantidade']
        if 'galinhas_produtoras' in data:
            production_data['galinhas_produtoras'] = data['galinhas_produtoras']
        if 'observacoes' in data:
            production_data['observacoes'] = data['observacoes']
        
        production = run_async(supabase_service.update_egg_production(production_id, production_data))
        
        if production:
            return jsonify(production)
        else:
            return jsonify({'error': 'Produção não encontrada'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@chickens_bp.route('/egg-production/<production_id>', methods=['DELETE'])
def delete_egg_production(production_id):
    try:
        success = run_async(supabase_service.delete_egg_production(production_id))
        
        if success:
            return jsonify({'message': 'Registro de produção removido com sucesso'})
        else:
            return jsonify({'error': 'Erro ao remover produção'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Rotas para Alimentação
@chickens_bp.route('/feeding', methods=['GET'])
def get_feeding():
    try:
        feeding = run_async(supabase_service.get_feeding())
        return jsonify(feeding)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@chickens_bp.route('/feeding', methods=['POST'])
def create_feeding():
    try:
        data = request.get_json()
        
        feeding_data = {
            'data': data['data'],
            'tipo_racao': data['tipo_racao'],
            'quantidade_kg': data['quantidade_kg'],
            'custo': data['custo'],
            'observacoes': data.get('observacoes', '')
        }
        
        feeding = run_async(supabase_service.create_feeding(feeding_data))
        
        if feeding:
            return jsonify(feeding), 201
        else:
            return jsonify({'error': 'Erro ao criar alimentação'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@chickens_bp.route('/feeding/<feeding_id>', methods=['PUT'])
def update_feeding(feeding_id):
    try:
        data = request.get_json()
        
        feeding_data = {}
        if 'data' in data:
            feeding_data['data'] = data['data']
        if 'tipo_racao' in data:
            feeding_data['tipo_racao'] = data['tipo_racao']
        if 'quantidade_kg' in data:
            feeding_data['quantidade_kg'] = data['quantidade_kg']
        if 'custo' in data:
            feeding_data['custo'] = data['custo']
        if 'observacoes' in data:
            feeding_data['observacoes'] = data['observacoes']
        
        feeding = run_async(supabase_service.update_feeding(feeding_id, feeding_data))
        
        if feeding:
            return jsonify(feeding)
        else:
            return jsonify({'error': 'Alimentação não encontrada'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@chickens_bp.route('/feeding/<feeding_id>', methods=['DELETE'])
def delete_feeding(feeding_id):
    try:
        success = run_async(supabase_service.delete_feeding(feeding_id))
        
        if success:
            return jsonify({'message': 'Registro de alimentação removido com sucesso'})
        else:
            return jsonify({'error': 'Erro ao remover alimentação'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Rotas para Saúde
@chickens_bp.route('/health', methods=['GET'])
def get_health():
    try:
        health = run_async(supabase_service.get_health())
        return jsonify(health)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@chickens_bp.route('/health', methods=['POST'])
def create_health():
    try:
        data = request.get_json()
        
        health_data = {
            'galinha_id': data['galinha_id'],
            'data': data['data'],
            'tipo': data['tipo'],
            'descricao': data['descricao'],
            'custo': data.get('custo', 0),
            'observacoes': data.get('observacoes', '')
        }
        
        health = run_async(supabase_service.create_health(health_data))
        
        if health:
            return jsonify(health), 201
        else:
            return jsonify({'error': 'Erro ao criar saúde'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@chickens_bp.route('/health/<health_id>', methods=['PUT'])
def update_health(health_id):
    try:
        data = request.get_json()
        
        health_data = {}
        if 'galinha_id' in data:
            health_data['galinha_id'] = data['galinha_id']
        if 'data' in data:
            health_data['data'] = data['data']
        if 'tipo' in data:
            health_data['tipo'] = data['tipo']
        if 'descricao' in data:
            health_data['descricao'] = data['descricao']
        if 'custo' in data:
            health_data['custo'] = data['custo']
        if 'observacoes' in data:
            health_data['observacoes'] = data['observacoes']
        
        health = run_async(supabase_service.update_health(health_id, health_data))
        
        if health:
            return jsonify(health)
        else:
            return jsonify({'error': 'Saúde não encontrada'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@chickens_bp.route('/health/<health_id>', methods=['DELETE'])
def delete_health(health_id):
    try:
        success = run_async(supabase_service.delete_health(health_id))
        
        if success:
            return jsonify({'message': 'Registro de saúde removido com sucesso'})
        else:
            return jsonify({'error': 'Erro ao remover saúde'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

