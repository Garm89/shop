from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
@app.route('/main/')
def main():
    context = {'title': 'Главная'}
    return render_template('main.html', **context)


@app.route('/jeans/')
def jeans():
    context = {'title': 'Джинсы'}
    return render_template('jeans.html', **context)


@app.route('/shorts/')
def shorts():
    context = {'title': 'Рубашки'}
    return render_template('shorts.html', **context)

@app.route('/dress/')
def dress():
    context = {'title': 'Платья'}
    return render_template('dress.html', **context)


@app.route('/jacket/')
def jacket():
    context = {'title': 'Куртки'}
    return render_template('jacket.html', **context)

@app.route('/costume/')
def costume():
    context = {'title': 'Костюмы'}
    return render_template('costume.html', **context)


@app.route('/blazers/')
def blazers():
    context = {'title': 'Блейзеры'}
    return render_template('blazers.html', **context)


@app.route('/sneakers/')
def sneakers():
    context = {'title': 'Кроссовки'}
    return render_template('sneakers.html', **context)


if __name__ == "__main__":
    app.run(debug=True)
