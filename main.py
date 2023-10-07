from flask import Flask, request, render_template_string
import math

app = Flask(__name__)


@app.route('/')
def calculator():
    return render_template_string('''
        <html>
        <head>
            <title>Calculator</title>
            <style>
                .calculator {
                    text-align: center;
                    margin-top: 100px;
                }

                .button {
                    width: 50px;
                    height: 50px;
                    margin: 5px;
                }
            </style>
            <script>
                function addToExpression(value) {
                    document.getElementById("expression").value += value;
                }

                function calculate() {
                    let expression = document.getElementById("expression").value;
                    let result = eval(expression);
                    document.getElementById("expression").value = result;
                }

                function clearExpression() {
                    document.getElementById("expression").value = '';
                }

               function calculateTrigFunction() {
                    let expression = document.getElementById("expression").value;
                                     // 将角度转换为弧度
                    let radians = eval(expression) * Math.PI / 180;
                    let result = Math.sin(radians);  // 计算正弦函数
                    document.getElementById("expression").value = result;
                }

                function calculateExponent() {
                    let expression = document.getElementById("expression").value;
                    let result = Math.exp(eval(expression));  // 计算指数函数
                    document.getElementById("expression").value = result;
                }

                function calculateLogarithm() {
                    let expression = document.getElementById("expression").value;
                    let result = Math.log10(eval(expression));  // 计算以10为底的对数
                    document.getElementById("expression").value = result;
                }
            </script>
        </head>
        <body>
            <div class="calculator">
                <h1>Calculator</h1>
                <form action="/calculate" method="POST">
                    <input type="text" id="expression" name="expression" required readonly>
                    <br>
                    <button class="button" type="button" onclick="addToExpression('1')">1</button>
                    <button class="button" type="button" onclick="addToExpression('2')">2</button>
                    <button class="button" type="button" onclick="addToExpression('3')">3</button>
                    <button class="button" type="button" onclick="addToExpression('+')">+</button>
                    <br>
                    <button class="button" type="button" onclick="addToExpression('4')">4</button>
                    <button class="button" type="button" onclick="addToExpression('5')">5</button>
                    <button class="button" type="button" onclick="addToExpression('6')">6</button>
                    <button class="button" type="button" onclick="addToExpression('-')">-</button>
                    <br>
                    <button class="button" type="button" onclick="addToExpression('7')">7</button>
                    <button class="button" type="button" onclick="addToExpression('8')">8</button>
                    <button class="button" type="button" onclick="addToExpression('9')">9</button>
                    <button class="button" type="button" onclick="addToExpression('*')">*</button>
                    <br>
                    <button class="button" type="button" onclick="addToExpression('0')">0</button>
                    <button class="button" type="button" onclick="addToExpression('.')">.</button>
                    <button class="button" type="button" onclick="calculate()">=</button>
                    <button class="button" type="button" onclick="addToExpression('/')">/</button>
                    <br>
                    <button class="button" type="button" onclick="clearExpression()">C</button>
                    <button class="button" type="button" onclick="calculateTrigFunction()">sin</button>
                    <button class="button" type="button" onclick="calculateExponent()">exp</button>
                    <button class="button" type="button" onclick="calculateLogarithm()">log</button>
                </form>
            </div>
        </body>
        </html>
    ''')


if __name__ == '__main__':
    app.run(debug=True)
