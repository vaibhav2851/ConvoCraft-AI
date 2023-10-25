from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
import openai
app = Flask(__name__)

# Configure SQLAlchemy database URI (replace with your database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # SQLite database for this example
db = SQLAlchemy(app)

# Define a User model without the 'id' field
class User(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), primary_key=True,unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)


    # def __init__(self, username, password):
    #     self.username = username
    #     self.password = password
    #
    #     def __repr__(self):
    #         return self.username,self.password

with app.app_context():
    db.create_all()

    # db.session.add(User('admizxzcn', 'admin@em'))
    # db.session.add(User('guest', 'guest@example.com'))
    # db.session.commit()

    users = User.query.all()
    # print(users)

# User registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    mes =''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        mes='Registration successful'

    return render_template('Signup.html',mes=mes)

# User login route
@app.route('/', methods=['GET', 'POST'])
def login():
    message =''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the user is registered
        user = User.query.filter_by(username=username).first()
        # print(username,password,'ajdiajsdas')
        if user:
            # print("asdkiaushdasj")
            # User is registered, check the password
            if user.password == password:
                message = 'Login Successful '
            else:
                message= 'Login failed: Incorrect password'
        else:
            message ='Login failed: User not registered'
        return render_template('main_page.html')
        # return render_template('Login.html',message=message)
    else:

        return render_template('Login.html',message=message)

@app.route('/main', methods=['GET', 'POST'])
def main():
    result =''
    if request.method == 'POST':
    #     # Process POST request
        data = request.get_data(as_text=True)
        # print(data.split('=')[1])
        data = data.split('=')[1]
        if '&' in data:
            data='hi'

    #
    import openai
    openai_api_key = 'open ai api key'
    # # Set your API key
    openai.api_key = openai_api_key
    #
    # # Generate text
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",  # Use the text-davinci-002 engine (or any other appropriate engine)
        messages=[
            {'role': 'user', 'content': data}]  # You can adjust the max_tokens parameter as needed
    )
    #
    # # Print the generated text
    result =response['choices'][0]['message']['content']
    result = result.replace('\n', '<br>')

    print(result)
    return render_template('main_page.html',result=result)

if __name__ == '__main__':
    app.run()

