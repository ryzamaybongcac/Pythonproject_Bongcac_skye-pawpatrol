import turtle

def draw_image(coordinates, fill_color):
    turtle.speed(0) 
    turtle.pu()  
    turtle.title("Paw Patrol")
    if coordinates:
        turtle.goto(coordinates[0]) 
        turtle.pd()  
        turtle.ht()
        turtle.fillcolor(fill_color)  
        turtle.begin_fill()  
        for coordinate in coordinates:
            x, y = coordinate
            turtle.goto(x, y)
        turtle.end_fill()  
    turtle.pu()  
    turtle.home()    
    turtle.pd() 

def draw_images_from_files(file_colors):
    for fname, fill_color in file_colors.items():
        with open(fname, 'r') as file:
            fill_color = file.readline().strip()
            fcoordinates = [tuple(map(float, line.strip().split(','))) for line in file]
            draw_image(fcoordinates, fill_color)
    turtle.done()

file_colors = {
    'coordinates/h1': '#e1a95f',
    'coordinates/d1': '#b87333',
    'coordinates/d2': 'white',
    'coordinates/d3': 'pink',
    'coordinates/d4': 'black',
    'coordinates/d5': 'white',
    'coordinates/d6': '#ff55a3',
    'coordinates/d7': '#b87333',
    'coordinates/d8': 'white',
    'coordinates/d9': 'pink',
    'coordinates/o1': 'black',
    'coordinates/o2': 'white',
    'coordinates/o3': '#bf94e4',
    'coordinates/o4': 'black',
    'coordinates/o5': 'black',
    'coordinates/o6': 'black',
    'coordinates/o7': 'black',
    'coordinates/o8': 'black',
    'coordinates/o9': 'red',
    'coordinates/g1': 'white',
    'coordinates/g2': '#ff55a3',
    'coordinates/g3': '#e1a95f',
    'coordinates/g4': '#e1a95f',
    'coordinates/g5': '#e1a95f',
    'coordinates/g6': 'white',
    'coordinates/g7': 'white',
    'coordinates/g8': 'white',
}
draw_images_from_files(file_colors)