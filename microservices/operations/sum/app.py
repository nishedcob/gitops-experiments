
from base_app import app, api, db, DoubleOperandMathematicalOperation

class SumOperation(DoubleOperandMathematicalOperation):
    """
    This Microservice should sum the two numbers it recieves and return the
    answer as a Python float or int (ints get casted as floats when parsed
    as a response) type

    >>> SumOperation().calculate(1, 1)
    2

    >>> SumOperation().calculate(2.0, 3.0)
    5.0

    >>> SumOperation().calculate(4.1, 5.2)
    9.3
    """

    def calculate(self, first_operand, second_operand):
        return first_operand + second_operand

api.add_resource(
    SumOperation,
    '/<float:first_operand>/<float:second_operand>',
    '/<int:first_operand>/<float:second_operand>',
    '/<float:first_operand>/<int:second_operand>',
    '/<int:first_operand>/<int:second_operand>',
    '/'
)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
