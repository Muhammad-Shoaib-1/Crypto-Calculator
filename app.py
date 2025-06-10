from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/margin', methods=['GET', 'POST'])
def margin():
    if request.method == 'POST':
        coin_price = float(request.form['coin_price'])
        leverage = float(request.form['leverage'])
        position_size = float(request.form['position_size'])

        trade_value = coin_price * position_size
        required_usdt = round(trade_value / leverage, 4)

        return render_template('margin.html', result=required_usdt)
    
    return render_template('margin.html')

@app.route('/profitloss', methods=['GET', 'POST'])
def profitloss():
    if request.method == 'POST':
        entry_price = float(request.form['entry_price'])
        exit_price = float(request.form['exit_price'])
        position_size = float(request.form['position_size'])
        trade_type = request.form['trade_type']

        if trade_type == 'long':
            profit_loss = (exit_price - entry_price) * position_size
        else:
            profit_loss = (entry_price - exit_price) * position_size

        profit_loss = round(profit_loss, 4)

        return render_template('profitloss.html', profit_loss=profit_loss)
    
    return render_template('profitloss.html')

if __name__ == '__main__':
    app.run(debug=True)
