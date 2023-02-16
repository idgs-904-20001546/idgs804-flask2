from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
from form import UserForm  
from dinamic_box import DinamicBoxForm

csrf = CSRFProtect()
app = Flask(__name__)
app.config['SECRET_KEY'] = "peuproweiu"
csrf.init_app(app)

@app.get('/')
def index():
    return render_template('form-test.html')

@app.get('/pupils')
def pupils():
    form = UserForm()
    return render_template('pupils.html', form=form)

@app.post('/pupils')
def create_pupil():
    form = UserForm(request.form)
    print(form.id.data)
    print(form.name.data)
    return render_template('pupils.html', form=form)

@app.get('/boxes')
def boxes():
    form = DinamicBoxForm()
    return render_template('dinamic-boxes.html', form=form)

@app.post('/boxes')
def create_boxes():
    form = DinamicBoxForm(request.form)
    inputs_quantity = form.quantity.data
    return render_template('dinamic-boxes.html', form=form, inputs_quantity=inputs_quantity)

@app.post('/caculate-boxes')
def caculate_boxes():
    form = DinamicBoxForm(request.form)
    numbers = [int(number) for number in request.form.getlist('numbers[]')]
    minNum = min(numbers)
    maxNum = max(numbers)
    average = sum(numbers) / len(numbers)
    
    onlyNumbers = set(numbers)
    mapValuesBefore = {}
    mapValues = {}

    for number in onlyNumbers:
        mapValuesBefore[number] = len([num for num in numbers if num == number])

    mapValues = { key: value for key, value in mapValuesBefore.items() if value > 1 }

    return render_template('result-boxes.html', numbers=numbers, minNum=minNum, maxNum=maxNum, average=average, mapValues=mapValues)


if __name__ == '__main__':
    app.run(debug=True, port=3000)
