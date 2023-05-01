''''
1. Lav PhotoImage randomiser - gem som billede
2. Implementer som Flask endpoint
3. HTML - use flask to create a server and generate a dynamic html  page displaying the "artwork"
4. Profit
'''
from tkinter import *
import random
from PIL import Image
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/random_shapes')
def image_randomiser():
    window_01 = Tk()
    canvas_01 = Canvas(window_01,bg='black', width=1000, height=1080)
    canvas_01.pack(fill='both',expand=True)

    shape_coll = []
    for i in range(1000):
        x = random.randint(10,990)
        y = random.randint(10,990)
        size = random.randint(20,700)
        color = random.choice(("red","orange","green","blue","white","yellow"))
        shape_type = canvas_01.create_rectangle(x,y,x+size,y+size,fill=color,outline='white')
        shape_coll.append(shape_type)
    canvas_01.update()
    canvas_01.postscript(file='random_shapes.ps', colormode='color')
    final = Image.open('random_shapes.ps')
    final.save('static/Image/random_shapes.png')
    window_01.destroy()
    window_01.mainloop()
    return render_template('random_pic.html')

    #def randpic():
     #   return render_template('random_pic.html')

if __name__ == '__main__':
    app.run(debug=True, port=9000)