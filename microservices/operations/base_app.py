
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

db = SQLAlchemy(app)
ma = Marshmallow(app)


class PerformedOperation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    result = db.Column(db.Float, nullable=True)

    def __repr__(self):
        return '<Operation Number: {id} | Result: {result}>'.format(id=self.id, result=self.result)


class PerformedSingleOperandOperation(PerformedOperation):
    first_operand = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<Operation Number: {id} | Operand: {operand} | Result: {result}>'.format(id=self.id, operand=self.first_operand, result=self.result)


class PerformedDoubleOperandOperation(PerformedSingleOperandOperation):
    second_operand = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<Operation Number: {id} | First Operand: {first_operand} | Second Operand: {second_operand} | Result: {result}>'.format(id=self.id, first_operand=self.first_operand, second_operand=self.second_operand, result=self.result)


class PerformedSingleOperandOperationSchema(ma.Schema):
    class Meta:
        # we want to expose:
        fields = ('id', 'first_operand', 'result')


class PerformedDoubleOperandOperationSchema(ma.Schema):
    class Meta:
        # we want to expose:
        fields = ('id', 'first_operand', 'second_operand', 'result')


single_op_schema = PerformedSingleOperandOperationSchema()
double_op_schema = PerformedDoubleOperandOperationSchema()

def save_operation(operation):
    db.session.add(operation)
    db.session.commit()

def save_single_op(operand, result):
    operation = PerformedSingleOperandOperation(
        first_operand=operand, result=result
    )
    save_operation(operation)

def save_double_op(first_operand, second_operand, result):
    operation = PerformedDoubleOperandOperation(
        first_operand=first_operand, second_operand=second_operand,
        result=result
    )
    save_operation(operation)


class SingleOperandMathematicalOperation(Resource):

    def calculate(self, operand):
        pass

    def post(self, operand):
        result = self.calculate(operand=operand)
        save_single_op(operand=operand, result=result)
        return result, 200

    def get(self):
        return list(
            map(
                lambda performed_op: single_op_schema.dump(performed_op).data,
                PerformedSingleOperandOperation.query.all()
            )
        ), 200


class DoubleOperandMathematicalOperation(Resource):

    def calculate(self, first_operand, second_operand):
        pass

    def post(self, first_operand, second_operand):
        result = self.calculate(
            first_operand=first_operand, second_operand=second_operand
        )
        save_double_op(
            first_operand=first_operand, second_operand=second_operand,
            result=result
        )
        return result, 200

    def get(self):
        return list(
            map(
                lambda performed_op: double_op_schema.dump(performed_op).data,
                PerformedDoubleOperandOperation.query.all()
            )
        ), 200
