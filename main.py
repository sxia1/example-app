import random
from display import *
from draw import *
from matrix import *

screen = new_screen()
white = [255, 255, 255]
orange = [255, 100, 0]
matrix = new_matrix()

A = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
B = [[11,12,13,14],[15,16,17,18],[19,20,21,22],[23,24,25,26]]

# print_matrix(A)
# print_matrix(B)
# matrix_mult(A, B)
# print_matrix(A)
# print_matrix(B)
# matrix_mult(B, A)
# print_matrix(A)
# print_matrix(B)
# ident(matrix)
# matrix_mult(matrix, A)
# print_matrix(A)

edges = new_matrix(0,4)
fill = new_matrix(0,4)
road = new_matrix(0,4)

def draw_box(matrix, x, y, width, height, filled=False):
    # Centered at x, y
    # not filled
    x_increment = int(width/2)
    y_increment = int(height/2)
    # Top
    add_edge(matrix, x-x_increment, y-y_increment, 0, x+x_increment, y-y_increment, 0)
    # Bottom
    add_edge(matrix, x-x_increment, y+y_increment, 0, x+x_increment, y+y_increment, 0)
    # Left
    add_edge(matrix, x-x_increment, y+y_increment, 0, x-x_increment, y-y_increment, 0)
    # Right
    add_edge(matrix, x+x_increment, y+y_increment, 0, x+x_increment, y-y_increment, 0)
    if filled:
        i = y - y_increment
        while i <= y+y_increment:
            add_edge(fill, x-x_increment, i, 0, x+x_increment, i, 0)
            i += 1


x_center = int(XRES/2)
y_center = int(YRES/2)
# print(x_center, y_center)

# Border
draw_box(edges, x_center, y_center+20, XRES-50, YRES-70)

# Center box
center_width = 180
center_height = 460
y_center_shift = 140
y_center -= y_center_shift
draw_box(edges, x_center, y_center, center_width, center_height)

# Cross block up
i = 90
while i <= y_center-center_height/2:
    x = 50
    while x <= XRES-50:
        draw_box(edges, x, i, 20, 20)
        x += 40
    i += 40

# Cross block down
i = YRES-50
while i >= y_center+center_height/2:
    x = 50
    while x <= XRES-50:
        draw_box(edges, x, i, 20, 20)
        x += 40
    i -= 40

# Center block
while i >= y_center-center_height/2:
    x = 50
    while x <= x_center-center_width/2:
        draw_box(edges, x, i, 20, 20)
        x += 40
    x = XRES-50
    while x >= x_center+center_width/2:
        draw_box(edges, x, i, 20, 20)
        x -= 40
    i -= 40

# Gate
draw_box(edges, x_center, 67, 80, 16)
draw_box(edges, x_center-50, 45, 16, 60)
draw_box(edges, x_center+50, 45, 16, 60)


# First gate
draw_box(edges, x_center, y_center-120, center_width, 10)
draw_box(edges, x_center, y_center-120, 50, 20)
draw_box(edges, x_center-50, y_center-120, 16, 16)
draw_box(edges, x_center+50, y_center-120, 16, 16)
draw_box(edges, x_center-int(center_width/2)+3, y_center-120, 16, 16)
draw_box(edges, x_center+int(center_width/2)-3, y_center-120, 16, 16)

# Side entrances
draw_box(edges, x_center-int(center_width/2)+3, y_center-20, 20, 40)
draw_box(edges, x_center+int(center_width/2)-3, y_center-20, 20, 40)
draw_box(edges, x_center-int(center_width/2)+3, y_center-20, 30, 50)
draw_box(edges, x_center+int(center_width/2)-3, y_center-20, 30, 50)

# 1st Palace
draw_box(edges, x_center, y_center+66, 80, 36)
draw_box(edges, x_center, y_center+66, 100, 48)
draw_box(edges, x_center, y_center+66, 120, 60)
draw_box(edges, x_center, y_center+66, 140, 72)

# 2nd Palace
draw_box(edges, x_center, y_center+120, 50, 24)

# 3rd Palace
draw_box(edges, x_center, y_center+180, 80, 20)
draw_box(edges, x_center, y_center+174, 100, 40)
draw_box(edges, x_center, y_center+174, 120, 60)
draw_box(edges, x_center, y_center+174, 140, 80)

draw_lines(edges, screen, white)
draw_lines(fill, screen, orange)

display(screen)
# save_ppm(screen, "pic.ppm")
save_extension(screen, 'img.png')
