"""
CMPUT 307 Fall 2016 
LEC A1 LAB D01

Lab 3: Working with Files and Transformations

Christopher Nyitrai
Shuyun Xiong
Michael Xi
"""
import numpy as np
import math

# Throughout this file 'obj' is taken to mean a list of lists, with each
# nested list containing the 3D coordinates of a vertex [x,y,z]. For example,
# in shrink_obj() obj takes this meaning, NOT the meaning of a .obj file.
# obj does not mean a .obj file unless specified.

# Matrix and obj alteration functions.
def expand_trans_mat(trans_mat):
    # This function expands a given transformation matrix to be compatible
    # with homogenous transforms.
    for i in trans_mat:
        i.append(0)
    trans_mat.append([0,0,0,1])
    return

def expand_obj(obj):
    # This function converts a matrix of 3D vertices to one compatible with
    # homogeneous transforms.
    for vertex in obj:
        vertex.append(1)
    return

def shrink_obj(obj):
    # This function does the opposite of expand_obj, returning
    # a expanded 3D vertex matrix back to only having 3 coordinates.
    for vertex in obj:
        vertex.pop()
    return

# The scale, rotation, and translation functions we use on an object.
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
    return scaled_obj, scale_mat

def obj_trans(obj, trans_x, trans_y, trans_z):
    # Translates the vertices in a 3D obj matrix and returns the translated
    # matrix.
    expand_obj(obj)
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
    shrink_obj(obj)
    shrink_obj(trans_obj)
    return trans_obj, trans_mat
    
def rot_obj_y(obj,degree):
    # Function for rotating an object around y-axis by degree 'degree'.

    # Convertion of the given degree for compatibility with the
    # .sin and .cos functions.
    degree = math.radians(degree)
    
    # Creation of the rotation matrix.
    sr = math.sin(degree)
    cr = math.cos(degree)
    rota_mat = [[cr,0,sr],[0,1,0],[-sr,0,cr]]
    
    # Iterate through the obj passed in and transform each vertex.
    rotated_obj = []
    for vertex in obj:
        # Similarly to the other transformation functions, we rotate
        # each vertex using matrix multiplication with a rotation matrix.
        # The new vertex is then added to a new matrix as a list.
        rotated_obj.append(np.dot(rota_mat, vertex).tolist())
    return rotated_obj, rota_mat


def write_matrixes_to_file(mat1,mat2,mat3):
    # Function used for writing the transformation matrixes to the file.

    # Conversion of matrixes to format which can be written easily.
    mat1, mat2, mat3 = str(mat1), str(mat2), str(mat3)
    
    # Writing of matrixes to file.
    with open('Transformation matrixes.txt','a') as target:
        target.write('Matrix for transformation 1: %s\n' % mat1)
        target.write('Matrixes for transformation 2: %s\n' % mat2)
        target.write('Matrixes for transformation 3: %s' % mat3)
    target.close()
    return


# Actual transformations as specified by the assignment.
# Transform 1: Scale the vertices of the cube by 4.
def trans1(objs):
    # Scaling by 4.
    obj4, trans1_scale_mat = obj_scale(objs[0],4,4,4)
    
    # Writing to file.
    target = open('O4.obj', 'w')
    for i in obj4:
        target.write('v %s %s %s\n' % (i[0],i[1],i[2]))
    target.close()

    # Transformation 1 matrix pull.
    return trans1_scale_mat

# Transform 2:
# Translate the cylinder by 100 units in y axis and scale it by 5 units.
def trans2(objs):
    # Translation of 100 in y.
    obj5_trans, trans2_trans_mat = obj_trans(objs[1],0,100,0)
    # Scaling by 5.
    obj5, trans2_scale_mat = obj_scale(obj5_trans, 5,5,5)
    
    # Writing to file.
    target = open('O5.obj','w')
    for i in obj5:
        target.write('v %s %s %s\n'% (i[0],i[1],i[2]))
    target.close()

    #Transformation 2 matrix pull.
    expand_trans_mat(trans2_scale_mat)
    return trans2_trans_mat, trans2_scale_mat

# Transform 3
def trans3(objs):
    # Rotation about y.
    obj6_rot, trans3_rot_mat = rot_obj_y(objs[2],90)
    # Translation by 10 in z.
    obj6_trans, trans3_trans_mat = obj_trans(obj6_rot,0,0,10)
    # Scaling by 3.
    obj6, trans3_scale_mat = obj_scale(obj6_trans,3,3,3)
    
    # Writing to file.
    target = open('O6.obj','w')
    for i in obj6:
        target.write('v %s %s %s\n'% (i[0],i[1],i[2]))
    target.close()

    #Transformation 3 matrix pull.
    expand_trans_mat(trans3_rot_mat)
    expand_trans_mat(trans3_scale_mat)
    return trans3_rot_mat, trans3_trans_mat, trans3_scale_mat

def main():
    # Initialization of array of .objs we will read and the object counter.
    objs = [[],[],[]]
    obj_count = 0
    
    # Opening the given .obj file.
    with open('Mixed.obj') as f:
        bigdata = f.readlines()

    # Reading line by line from bigdata.
    for line in bigdata:
        splitline = line.split()

        if not splitline:
            continue

        # If the first continuous set of characters on the line is 'v',
        # we store the coordinates in our objs array.
        if splitline[0] == 'v':
            x = float(splitline[1])
            y = float(splitline[2])
            z = float(splitline[3])
            objs[obj_count].append([x, y, z])

        # The 'g' line starter uniquely identifies the end of an object
        # in the given .obj file so that is what we check for.
        elif splitline[0] == 'g':
            obj_count += 1

    # The idea is that by feeding the trans1,2,3 functions the identity matrix
    # they return the transformation matrix used.
    trans1_mat = trans1(objs)
    trans2_mat = trans2(objs)
    trans3_mat = trans3(objs)

    # Now we write the matrixes to a seperate file.
    write_matrixes_to_file(trans1_mat,trans2_mat,trans3_mat)

main()


