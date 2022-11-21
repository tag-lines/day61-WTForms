from flask import Flask, render_template
from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = "vatomanocu"
Bootstrap(app)


class MyForm(FlaskForm):
    name = StringField(label='Enter your name', validators=[DataRequired()])
    password = PasswordField(label='Enter your password', validators=[DataRequired(), Length(min=8)])
    email = EmailField(label='Enter your email', validators=[Email()])
    submit = SubmitField(label='Login')


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = MyForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@email.com' and form.password.data == '12345678':
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=form)




if __name__ == '__main__':
    app.run(debug=True)