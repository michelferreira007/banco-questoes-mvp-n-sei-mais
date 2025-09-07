from flask import Blueprint, jsonify, request
from src.models.question import Question
from src.models.user import db

question_bp = Blueprint('question', __name__)

@question_bp.route('/questions', methods=['GET'])
def get_questions():
    """Retorna questões com filtros opcionais"""
    year = request.args.get('year', type=int)
    subject = request.args.get('subject')
    topic = request.args.get('topic')
    exam_type = request.args.get('exam_type')
    
    query = Question.query
    
    if year:
        query = query.filter(Question.year == year)
    if subject:
        query = query.filter(Question.subject == subject)
    if topic:
        query = query.filter(Question.topic == topic)
    if exam_type:
        query = query.filter(Question.exam_type == exam_type)
    
    questions = query.all()
    return jsonify([question.to_dict() for question in questions])

@question_bp.route('/questions/<int:question_id>', methods=['GET'])
def get_question(question_id):
    """Retorna uma questão específica"""
    question = Question.query.get_or_404(question_id)
    return jsonify(question.to_dict())

@question_bp.route('/questions', methods=['POST'])
def create_question():
    """Cria uma nova questão"""
    data = request.get_json()
    
    question = Question(
        year=data['year'],
        subject=data['subject'],
        topic=data.get('topic'),
        question_text=data['question_text'],
        option_a=data['option_a'],
        option_b=data['option_b'],
        option_c=data['option_c'],
        option_d=data['option_d'],
        option_e=data['option_e'],
        correct_answer=data['correct_answer'],
        explanation=data.get('explanation'),
        exam_type=data['exam_type']
    )
    
    db.session.add(question)
    db.session.commit()
    
    return jsonify(question.to_dict()), 201

@question_bp.route('/filters', methods=['GET'])
def get_filters():
    """Retorna os filtros disponíveis"""
    years = db.session.query(Question.year).distinct().order_by(Question.year.desc()).all()
    subjects = db.session.query(Question.subject).distinct().order_by(Question.subject).all()
    exam_types = db.session.query(Question.exam_type).distinct().order_by(Question.exam_type).all()
    
    return jsonify({
        'years': [year[0] for year in years],
        'subjects': [subject[0] for subject in subjects],
        'exam_types': [exam_type[0] for exam_type in exam_types]
    })

@question_bp.route('/check-answer', methods=['POST'])
def check_answer():
    """Verifica se a resposta está correta"""
    data = request.get_json()
    question_id = data['question_id']
    user_answer = data['answer']
    
    question = Question.query.get_or_404(question_id)
    is_correct = question.correct_answer.upper() == user_answer.upper()
    
    return jsonify({
        'correct': is_correct,
        'correct_answer': question.correct_answer,
        'explanation': question.explanation
    })

