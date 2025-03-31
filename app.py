from flask import Flask, render_template

app = Flask(__name__)

# Homepage Route
@app.route('/')
def home():
    return render_template('index.html')

# Dynamic User Page
@app.route('/user/<username>')
def user(username):
    user_interests = {
        "Tejas": ["Coding", "Music", "Travel"],
        "Guest": [],
        "Alice": ["Photography", "Gaming", "Reading"]
    }
    interests = user_interests.get(username, ["No specific interests"])
    return render_template('user.html', username=username, interests=interests)


# About Page
@app.route('/about')
def about():
    values = ["Innovation", "Integrity", "Collaboration", "Excellence", "Customer Focus"]
    return render_template('about.html', 
                           title="About Us", 
                           heading="About Us", 
                           description="This is a simple Flask application demonstrating template rendering.",
                           values=values)


# Contact Page
# Contact Page
@app.route('/contact')
def contact():
    contact_info = {
        "email": "tejas021@gmail.com",
        "phone": "+123 456 7890",
        "address": "Thane , West"
    }
    return render_template('contact.html', contact_info=contact_info)


if __name__ == '__main__':
    app.run(debug=True)
