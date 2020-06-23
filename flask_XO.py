from flask import Flask, url_for, render_template, request
from flask import jsonify

app = Flask('foo')

board = {'b1':None, 'b2':None, 'b3':None, 'b4':None, 
        'b5':None, 'b6':None, 'b7':None, 'b8':None, 'b9':None}
        

@app.route('/board', methods=['GET'])
def render_board():
    # return render_template('hello.html', name='Will')
    return jsonify({
        "board": board,
        'Winner':None,
        'isComplete':False})


@app.route('/board', methods=['POST'])
def play():
    move = request.get_json()
    print(move)
    return jsonify(body)
    
# THESE GO IN GET REQUEST
# how to store board in between turns? 
    # make function to check winner
    # make function to see whether or not game is over
    # function to validate inputs

# have both functions return the same thing

if __name__ == '__main__':
    app.run(debug=True)