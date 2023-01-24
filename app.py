from flask import Flask, render_template

app = Flask(__name__)

list_users = [
    {
        "id": 1,
        "name": "Mannopboy"
    },
    {
        "id": 2,
        "name": "Behruz"
    },
    {
        "id": 3,
        "name": "Sherzod"
    }

]


@app.route('/')
def home():
    return render_template('home.html', users=list_users)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/profile/<int:user_id>')
def profile(user_id):
    name = ''
    for user in list_users:
        if user["id"] == user_id:
            name = user['name']
    return render_template('profile.html', name=name)


if __name__ == '__main__':
    app.run()
