class InfixCalculator:
    def __init__(self):
        self.operators = {'+': 1, '-': 1, '*': 2, '/': 2}
        self.output_queue = []
        self.operator_stack = []

    def calculate_infix(self, expression):
        tokens = expression.split()

        for token in tokens:
            if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
                self.output_queue.append(int(token))
            elif token in self.operators:
                while (self.operator_stack and
                       self.operators[token] <= self.operators[self.operator_stack[-1]]):
                    self.output_queue.append(self.operator_stack.pop())
                self.operator_stack.append(token)
            elif token == '(':
                self.operator_stack.append(token)
            elif token == ')':
                while self.operator_stack and self.operator_stack[-1] != '(':
                    self.output_queue.append(self.operator_stack.pop())
                self.operator_stack.pop()
            else:
                raise ValueError(f"Invalid token: {token}")

        while self.operator_stack:
            self.output_queue.append(self.operator_stack.pop())

        rpn_expression = ' '.join(map(str, self.output_queue))
        rpn_calculator = RPNCalculator()
        result = rpn_calculator.calculate_rpn(rpn_expression)
        return result

# Example usage:
infix_calculator = InfixCalculator()
result = infix_calculator.calculate_infix("( 3 + 4 ) * 5")
print(result)
