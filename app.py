from flask import Flask, render_template, request

app = Flask(__name__)


# Главная страница
@app.route('/')
def home():
    return render_template('index.html')

# Маршрут для обработки данных формы (например, заявка от клиента)
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Здесь можно добавить логику для обработки данных, например, отправку письма
    # или сохранение данных в базу данных

    return f"Спасибо, {name}, ваша заявка принята!"


if __name__ == '__main__':
    app.run(debug=True)