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
                .button {
                    width: 50px;
                    height: 50px;
                    margin: 5px;
                }
            </style>
        </head>
        <body>
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
                <button class="button" type="button" onclick="addToExpression('.')">.</button>
                <button class="button" type="button" onclick="addToExpression('0')">0</button>
                <button class="button" type="button" onclick="calculateExpression()">=</button>
                <button class="button" type="button" onclick="clearExpression()">C</button>
            </form>

            {% if result %}
                <h2>Result: {{ result }}</h2>
            {% endif %}

            <script>
                function addToExpression(value) {
                    var expression = document.getElementById('expression');
                    expression.value += value;
                }

                function calculateExpression() {
                    var expression = document.getElementById('expression');
                    var result = eval(expression.value);
                    expression.value = result;
                }

                function clearExpression() {
                    var expression = document.getElementById('expression');
                    expression.value = '';
                }
            </script>
        </body>
        </html>
    ''')


if __name__ == '__main__':
    app.run()
