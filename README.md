# randomimagegenerator
A project challenge completed! Random images in browser!

A challenge was issued by a friend:
Use Python Tkinter to generate a random image using various geometric shapes, and serve the image on a dynamic html page using flask.

This task was solved in 4 parts:

1. Create the image randomiser in python
  By using the Random and tkinter libraries I was able to create a window, with a canvas
  that created random rectangles, placed randomly around a canvas. It was important for me to contain this all in a single function
  to make the flask handling that much easier.
  
    More specifically, I created a empty collection list, that a for loop would append 1000 times, with various canvas shapes.
 
    using pre-determined variables that were randomised using random integers in a range of 
    10,990(canvas size+/-10) for location (x, y)
    
    and range 20,700 for size (to prevent singular shapes taking over too much of the canvas)
    
    To add some flair, each shape randomly choose a color from a list using random choice.
    and assigned this choice to a color variable.
    
    I then created a variable called shape_type to house the random choices
    (x,y,x+size,y+size,fill=color,outline='white')
    
    and appended the collection list with
    shape_coll.append(shape_type)
    
    The for loop now repeated this process 1000 times.

2. Save the image generated to a .png
  I suppose this was partly me misunderstanding the assignment, and ended up spending a bunch of time on this. It was cool though.
  figuring out a way to save a canvas, which tkinter handles fine using canvas.postscript. to save the file as a .ps file
  But I figured out that the Pillow library holds a useful feature to open, a .ps file, and save it again as a .png
  
3. Moving on to the HTML side of things, I created a very simple page that uses a mix of css and jinja to fetch and serve the .png from the file structure
  on load, and provide a button to generate a new picture with some css flair.

4. Finally, using flask, I created a flask app in the main pythong script, and put the appropriate decorator on top of the entire python function 
  Launch the flask server, go to the defined site path, and BOOM, random image every time!
  
All in all this was a fun time, and a great learning experience to find solutions to a problem.
