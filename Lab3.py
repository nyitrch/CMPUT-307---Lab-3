# -*- coding: utf-8 -*-
"""
CMPUT 307 Fall 2016 
LEC A1 LAB D01

Lab 3: Working with Files and Transformations

Christopher Nyitrai
Shuyun Xiong
Michael Xi
"""
import numpy as np

# Matrix transformation functions.

# Expand and shirnk are used to navigate between matrices that contain
# coordinates we want to write to and from files, and ones we want to
# perform transformations on.
def expand_mat(mat):
    # This function converts a 3D matrix to a 4D version 
    # so that it is compatible with homogeneous transforms.
    for coordinate in mat:
        coordinate.append(1)
    return

def shrink_mat(mat):
    # This function does the opposite of expand_mat, returning
    # a 3D matrix converted from a 4D matrix back to its 3D status.
    for coordinate in mat:
        coordinate.pop()
    return 


# TESTING OF EXPAND AND SHRINK. UNCOMMENT TO TEST.
'''a = [[1,1,1],[1,1,2],[1,1,3],[1,1,4],[1,1,5]]
print(a)

expand_mat(a)
print(a)

shrink_mat(a)
print(a)'''


# The scale, translate, and rotation functions all take only 3x3 matrices.
def obj_scale(obj,x_scale,y_scale,z_scale):
    # Takes a 3D obj matrix and returns a version of it scaled by
    # the scale value for each coordinate.
    scale_mat = [[x_scale,0,0],
                 [0,y_scale,0],
                 [0,0,z_scale]]
    scaled_obj = []
    # Scaling of each vertex in obj.
    for vertex in obj:
        # We scale each vertex using matrix multiplication with the scale
        # matrix, then add it to our new scaled version of the original obj.
        # .tolist() is needed to keep our types consistent.
        scaled_obj.append(np.dot(scale_mat,vertex).tolist())
    return scaled_obj

def obj_trans(obj, trans_x, trans_y, trans_z):
    # Translates the vertices in a 3D obj matrix and returns the translated
    # matrix.
    expand_mat(obj)
    trans_mat = [[1,0,0,trans_x],
                 [0,1,0,trans_y],
                 [0,0,1,trans_z],
                 [0,0,0,1]]
    trans_obj = []
    # Translating of each vertex in obj.
    for vertex in obj:
        # We translate each vertex using matrix multiplication with the 
        # translation matrix, then add it to our new translated version 
        # of the original obj. tolist() is needed again to keep our types
        # consistent.
        trans_obj.append(np.dot(trans_mat,vertex).tolist())
    shrink_mat(obj)
    shrink_mat(trans_obj)
    return trans_obj
    

# TESTING OF SCALING, TRANSLATING, AND ROTATING. UNCOMMENT TO TEST.
'''a = [[1,1,1],[1,1,2],[1,1,3],[1,1,4],[1,1,5]]
print('a= '+str(a))

b = obj_scale(a,2,2,2)
print('b= '+str(b))
print('a= '+str(a))

c = obj_trans(a,2,-2,10)
print('c= '+str(c))
print('a= '+str(a))'''


# Initialization of array of .objs we will read and the object counter.
objs = [[],[],[]]
obj_count = 0

# Opening the given .obj
with open('Mixed.obj') as f:
        bigdata = f.readlines()

# Reading line by line from bigdata.
for line in bigdata:
    
        splitline = line.split()
        
        if not splitline:
                continue           
        
        # If the first continuous set of characters on the line is 'v',
        # we store the coordinates in our objs array.
        if splitline[0] =='v':
            x = float(splitline[1])
            y = float(splitline[2])
            z = float(splitline[3])
            objs[obj_count].append([x,y,z])
            
        # The 'g' line starter uniquely identifies the end of an object
        # in the given .obj file so that is what we check for.
        elif splitline[0] =='g':
            obj_count += 1


                
#obj4 = obj_scale(objs[0],4)

# Writing the objects to their individual files. Not needed for the current
# version of the assignment.
'''
target = open('O1.obj','w')
for i in objs[0]:
    target.write('v %s %s %s\n'% (i[0],i[1],i[2]))
target.close()

target = open('O2.obj','w')
for i in objs[1]:
    target.write('v %s %s %s\n'% (i[0],i[1],i[2]))
target.close()

target = open('O3.obj','w')
for i in objs[2]:
    target.write('v %s %s %s\n'% (i[0],i[1],i[2]))
target.close()
'''

# Actual transformations as specified by the assignment.
'''#Transform 1
obj4 = obj_scale(objs[0],4)
target = open('O4.obj','w')
for i in obj4:
    target.write('v %s %s %s\n'% (i[0],i[1],i[2]))
target.close()

#Transform 2
obj5_trans = obj_trans(objs[1],0,100,0)
obj5 = obj_scale(obj5_trans, 5)
target = open('O4.obj','w')
for i in obj5:
    target.write('v %s %s %s\n'% (i[0],i[1],i[2]))
target.close()'''