from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # The main page showing the wish list items
    return """
    <h1> My Birthday Wish List</h1>
    <p>Here are three things I am wishing for this year:</p>
    <hr>
    
    <ul>
        <li><strong>A Girls trip</strong></li>
        <li><strong>Google pixel mobile</strong></li>
        <li><strong>Birthday dress</strong></li>
    </ul>
    
    <hr>
    <h3>Add a item:</h3>
    <form>
        <input type="text" placeholder="Enter an item..."required>
        <button type="submit">Add Item</button>
    </form>
    
    <p><a href="/about">Click here to see why I made this!</a>       
    </p>
    """

@app.route('/about')
def about():
    # A simple second page that links back to the home page
    return """
    <h1>About This App</h1>
    <p>I built this simple web application using Python and Flask.</p>
    <hr>
    <a href="/">← Go Back to Wish List</a>
    """

if __name__ == "__main__":
    app.run(debug=True,port=5000)



