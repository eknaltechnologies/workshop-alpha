from flask import Flask,request

app=Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Hello, Welcome to My Portfolio</h1>
    <p>This is Rajesh</p>
    <p>A Final year student.</p>
    """

@app.route('/about')
def about():
    return """
    <h3>My name is Rajesh.I am a final year student.</h3>
    <p>I am interested in Python,Flask and Machine Learning.</p>
    """


@app.route("/skills")
def skills():
    return """
    <h1>Skills</h1>

    <ul>
        <li>Python</li>
        <li>Flask</li>
        <li>SQL</li>
        <li>Machine Learning</li>
        <li>Deep Learning</li>
        <li>HTML5</li>
        <li>CSS3</li>
    </ul>
    """

@app.route('/projects')
def projects():
    return """
    <h1>Projects</h1>

    <ul>
        <li>AQI Prediction System</li>
        <li>Emotion Detection Project</li>
        <li>Recommendation System</li>
    </ul>
    """
@app.route("/contact")
def contact():
    return """
    <h1>Contact Me</h1>

    <p>Email: rajesh@example.com</p>
    <p>Phone: 9876543210</p>
    """


if __name__=="__main__":
    app.run(debug=True)