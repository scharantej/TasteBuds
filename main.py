
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Process the order
        return redirect(url_for('order'))
    else:
        # Render the home page
        return render_template('index.html')

@app.route('/order', methods=['GET', 'POST'])
def order():
    if request.method == 'POST':
        # Update or cancel the order
        return redirect(url_for('index'))
    else:
        # Render the order confirmation page
        return render_template('order.html')

if __name__ == '__main__':
    app.run(debug=True)
