from src.models.user import db

class Question(db.Model):
    __tablename__ = 'questions'
    
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    topic = db.Column(db.String(200), nullable=True)
    question_text = db.Column(db.Text, nullable=False)
    option_a = db.Column(db.Text, nullable=False)
    option_b = db.Column(db.Text, nullable=False)
    option_c = db.Column(db.Text, nullable=False)
    option_d = db.Column(db.Text, nullable=False)
    option_e = db.Column(db.Text, nullable=False)
    correct_answer = db.Column(db.String(1), nullable=False)  # A, B, C, D, E
    explanation = db.Column(db.Text, nullable=True)
    exam_type = db.Column(db.String(50), nullable=False)  # PAS, Vestibular, etc.
    
    def to_dict(self):
        return {
            'id': self.id,
            'year': self.year,
            'subject': self.subject,
            'topic': self.topic,
            'question_text': self.question_text,
            'option_a': self.option_a,
            'option_b': self.option_b,
            'option_c': self.option_c,
            'option_d': self.option_d,
            'option_e': self.option_e,
            'correct_answer': self.correct_answer,
            'explanation': self.explanation,
            'exam_type': self.exam_type
        }

