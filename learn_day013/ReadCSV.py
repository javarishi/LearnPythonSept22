from learn_day013.TeacherClas import Teacher
import csv

path = '/RISHI/H2K/FileIO/TEMP/CSVFilesteachers.csv'

file = open(path, 'rt')
teachers = []
for eachRow in file:
    data_list = eachRow.split(',')
    teacher = Teacher(data_list[0], data_list[1], data_list[2])
    print(data_list)

file.close()