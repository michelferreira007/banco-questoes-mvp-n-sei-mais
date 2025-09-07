import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from flask import Flask
from src.models.user import db
from src.models.question import Question

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(os.path.dirname(__file__), 'database', 'app.db')}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    return app

def seed_questions():
    """Adiciona questões de exemplo ao banco de dados"""
    
    app = create_app()
    
    sample_questions = [
        {
            'year': 2023,
            'subject': 'Matemática',
            'topic': 'Álgebra',
            'question_text': 'Qual é o valor de x na equação 2x + 5 = 15?',
            'option_a': 'x = 3',
            'option_b': 'x = 5',
            'option_c': 'x = 7',
            'option_d': 'x = 10',
            'option_e': 'x = 15',
            'correct_answer': 'B',
            'explanation': 'Resolvendo: 2x + 5 = 15 → 2x = 10 → x = 5',
            'exam_type': 'PAS'
        },
        {
            'year': 2023,
            'subject': 'Português',
            'topic': 'Gramática',
            'question_text': 'Qual das alternativas apresenta um exemplo de oração subordinada substantiva?',
            'option_a': 'Ele chegou cedo.',
            'option_b': 'Espero que você venha.',
            'option_c': 'O livro está na mesa.',
            'option_d': 'Choveu muito ontem.',
            'option_e': 'Maria é inteligente.',
            'correct_answer': 'B',
            'explanation': 'A oração "que você venha" é subordinada substantiva objetiva direta.',
            'exam_type': 'Vestibular'
        },
        {
            'year': 2022,
            'subject': 'História',
            'topic': 'Brasil Colonial',
            'question_text': 'Qual foi o principal produto de exportação do Brasil durante o período colonial?',
            'option_a': 'Café',
            'option_b': 'Açúcar',
            'option_c': 'Ouro',
            'option_d': 'Algodão',
            'option_e': 'Tabaco',
            'correct_answer': 'B',
            'explanation': 'O açúcar foi o principal produto de exportação durante grande parte do período colonial brasileiro.',
            'exam_type': 'PAS'
        },
        {
            'year': 2022,
            'subject': 'Física',
            'topic': 'Mecânica',
            'question_text': 'Um objeto em queda livre, partindo do repouso, percorre 45m em 3s. Qual é a aceleração da gravidade?',
            'option_a': '5 m/s²',
            'option_b': '9,8 m/s²',
            'option_c': '10 m/s²',
            'option_d': '15 m/s²',
            'option_e': '20 m/s²',
            'correct_answer': 'C',
            'explanation': 'Usando h = gt²/2: 45 = g×9/2 → g = 10 m/s²',
            'exam_type': 'Vestibular'
        },
        {
            'year': 2021,
            'subject': 'Química',
            'topic': 'Química Orgânica',
            'question_text': 'Qual é a fórmula molecular do metano?',
            'option_a': 'CH₂',
            'option_b': 'CH₃',
            'option_c': 'CH₄',
            'option_d': 'C₂H₄',
            'option_e': 'C₂H₆',
            'correct_answer': 'C',
            'explanation': 'O metano é o hidrocarboneto mais simples, com fórmula CH₄.',
            'exam_type': 'PAS'
        }
    ]
    
    with app.app_context():
        # Criar todas as tabelas
        db.create_all()
        
        # Adicionar novas questões
        for q_data in sample_questions:
            question = Question(**q_data)
            db.session.add(question)
        
        db.session.commit()
        print(f"Adicionadas {len(sample_questions)} questões de exemplo!")

if __name__ == '__main__':
    seed_questions()

