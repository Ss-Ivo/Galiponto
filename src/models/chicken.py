from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import uuid

db = SQLAlchemy()

class Galinha(db.Model):
    __tablename__ = 'galinhas'
    
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    numero_identificacao = db.Column(db.String(50), unique=True, nullable=False)
    data_entrada = db.Column(db.Date, nullable=False)
    raca = db.Column(db.String(100), nullable=False)
    idade_entrada = db.Column(db.Integer, nullable=False)
    origem = db.Column(db.String(200), nullable=False)
    ativa = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relacionamentos
    saidas = db.relationship('SaidaGalinha', backref='galinha', lazy=True, cascade='all, delete-orphan')
    registros_saude = db.relationship('Saude', backref='galinha', lazy=True, cascade='all, delete-orphan')
    
    def to_dict(self):
        return {
            'id': self.id,
            'numero_identificacao': self.numero_identificacao,
            'data_entrada': self.data_entrada.isoformat() if self.data_entrada else None,
            'raca': self.raca,
            'idade_entrada': self.idade_entrada,
            'origem': self.origem,
            'ativa': self.ativa,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

class SaidaGalinha(db.Model):
    __tablename__ = 'saidas_galinhas'
    
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    galinha_id = db.Column(db.String(36), db.ForeignKey('galinhas.id'), nullable=False)
    data_saida = db.Column(db.Date, nullable=False)
    motivo = db.Column(db.String(200), nullable=False)
    observacoes = db.Column(db.Text, default='')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'galinha_id': self.galinha_id,
            'data_saida': self.data_saida.isoformat() if self.data_saida else None,
            'motivo': self.motivo,
            'observacoes': self.observacoes,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

class ProducaoOvos(db.Model):
    __tablename__ = 'producao_ovos'
    
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    data = db.Column(db.Date, nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    galinhas_produtoras = db.Column(db.JSON, default=list)
    observacoes = db.Column(db.Text, default='')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'data': self.data.isoformat() if self.data else None,
            'quantidade': self.quantidade,
            'galinhas_produtoras': self.galinhas_produtoras or [],
            'observacoes': self.observacoes,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

class Alimentacao(db.Model):
    __tablename__ = 'alimentacao'
    
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    data = db.Column(db.Date, nullable=False)
    tipo_racao = db.Column(db.String(100), nullable=False)
    quantidade_kg = db.Column(db.Numeric(10, 2), nullable=False)
    custo = db.Column(db.Numeric(10, 2), nullable=False)
    observacoes = db.Column(db.Text, default='')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'data': self.data.isoformat() if self.data else None,
            'tipo_racao': self.tipo_racao,
            'quantidade_kg': float(self.quantidade_kg),
            'custo': float(self.custo),
            'observacoes': self.observacoes,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

class Saude(db.Model):
    __tablename__ = 'saude'
    
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    galinha_id = db.Column(db.String(36), db.ForeignKey('galinhas.id'), nullable=False)
    data = db.Column(db.Date, nullable=False)
    tipo = db.Column(db.String(20), nullable=False)  # vacina, doenca, tratamento
    descricao = db.Column(db.Text, nullable=False)
    custo = db.Column(db.Numeric(10, 2), default=0)
    observacoes = db.Column(db.Text, default='')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'galinha_id': self.galinha_id,
            'data': self.data.isoformat() if self.data else None,
            'tipo': self.tipo,
            'descricao': self.descricao,
            'custo': float(self.custo),
            'observacoes': self.observacoes,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

