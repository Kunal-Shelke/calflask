from flask import Flask,request,render_template



app=Flask(__name__)

@app.route('/')
def welcome():
    return 'WElcome to Flask'

#print(__name__)
@app.route('/cal',method=['GET'])
def math_operator():
    operation=request.json['operation']
    number1=request.json['number1']
    number2=request.json['number2']
    
    if operation=='add':
        result=number1+number2
    elif operation='mul':
        result=number1*number2
    elif operation='div':
        result=number1/number2
    else :
        result-number1-number2
    return result

if __name__=='__main__':
    app.run()
