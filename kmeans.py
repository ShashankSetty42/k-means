import argparse
import math
import random
import ast


data_points = {} #contains centroid as key and coordinate as value
centroid_list = [] #contains number of centroids
input_coordinates = [] #contains input coordinates
final_centroid_list = []

def get_distance(coordinate1, coordinate2):
    '''
    This function calculates the distance between two points in a 2D space
    :param coordinate1: is a list of two coordinates
    :param coordinate2: is a list of two coordinates
    :return: returns the distance between both the coordinates
    '''

    #used https://www.omnicalculator.com/math/distance as reference for formula

    return math.sqrt( (coordinate2[0]-coordinate1[0])**2 + (coordinate2[1]-coordinate1[1])**2 )

def get_random_centroid(coordinate_list):
    '''
    This function returns two randomly generated coordinates by using input list for range
    :param coordinate_list: this list consists of the input coordinates
    :return: a list of random coordinates
    '''

    max_x_coordinate = min_x_coodinate =  max_y_coordinate = min_y_coodinate = 0

    for x,y in coordinate_list:
        if x > max_x_coordinate:
            max_x_coordinate = x
        if x < min_x_coodinate:
            min_x_coodinate = x
        if y > max_y_coordinate:
            max_x_coordinate = y
        if y < min_y_coodinate:
            min_x_coodinate = y

    return [random.randint(min_x_coodinate,max_x_coordinate), random.randint(min_y_coodinate, max_y_coordinate)]

def assign_points_to_cluster(coordinates):
    global centroid_list, data_points
    for x,y in coordinates:
        distance_dict = {} #is a dict containing centroid and it's distance to coordinates
        for centroid in centroid_list:
            distance_dict[str(centroid)] = get_distance([x,y],centroid)

        key = list(distance_dict.keys())[0]
        val = distance_dict[key]
        min_distance = val

        for centroid in distance_dict:
            if distance_dict[centroid] < min_distance:
                min_distance = distance_dict[centroid]
                key = centroid

        #data_points[str([x,y])] = str(key)
        if not data_points[str(key)]:
            data_points[str(key)] = [[x,y]]
        else:
            data_points.append([x,y])

def calculate_roof_centroid():

    global final_centroid_list
    for centroid in data_points:
        total = len(data_points[centroid])
        coordinates = data_points[centroid]
        x_sum = y_sum = 0
        for x,y in coordinates:
            x_sum += x
            y_sum += y

        x_avg = x_sum/total
        y_avg = y_sum/total

        final_centroid_list[centroid] = [x_avg,y_avg]

def print_results():
    global  data_points, final_centroid_list

    print('---------------------------------------\n')
    print('centroid moves')
    for item in final_centroid_list:
        print('Centroid before : ' + item + ' Centroid after : ' + str(final_centroid_list[item]) + '\n')

    print('++++++++++++++++++++++++++++++++++++++\n')
    print('data points for each centroid : \n')
    for centroid in data_points:
        print('Data points for centroid ' + centroid + ' is ' + str(data_points[centroid]) + '\n')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='use this to get k-means values for given input')
    parser.add_argument('-i', '--iterations', help='Use this option to specify number of iterations to run k-means algorithm', required=True)
    parser.add_argument('-c','--centroids', help='Use this option to specify number of centroids needed', required=True)
    parser.add_argument('-f','--coordinate_file', help='Use this option to specify coordinate file', required=True)

    args = parser.parse_args()
    global input_coordinates, centroid_list
    if args.iterations and args.centroids and args.coordinate_file:
        with open(args.coordinate_file, 'r') as cfile:
            for line in cfile:
                line = line.strip().split(',')
                input_coordinates.append([float(line[0]), float[line[1]]])

        iterations = args.iterations
        number_of_centroids = args.centroids

        for centroid in range(number_of_centroids):
            centroid_list.append(get_random_centroid(input_coordinates))

        for iteration in range(iterations):
            assign_points_to_cluster(input_coordinates)
            calculate_roof_centroid()
            print_results()


