import eel
from geneticalgorithm import geneticalgorithm as ga
import numpy as np
import csv
import os
from io import StringIO
eel.init("web")
# Student class


class Student:
    def __init__(self, name, gpa, skill, time):
        self.name = name
        self.gpa = gpa  # Range [0,4]
        # 1 Writing, 2 = Leadership, 3 = Problem Solving, 4 = Creativity, 5 = Planning
        self.skill = skill
        self.time = time  # 1 = Morning, 2 = Afternoon, 3 = Night

    def __repr__(self):
        return 'Name: {},       GPA: {:0.2f},       Skill: {},      Time: {}'.format(self.name, self.gpa, self.skill, self.time)

    def __str__(self):
        return 'Name: {},       GPA: {:0.2f},       Skill: {},      Time: {}'.format(self.name, self.gpa, self.skill, self.time)


###################################################################################################
students = []
teamSize = 0
resultsString = ''

# Fitness function


def f(x):  # lower fitness value is better
    numOfTeams = round(len(x)/teamSize)
    # Create teams container
    teams = []
    for i in range(numOfTeams):
        teams.append([])

    for i in range(len(x)):  # Add each student to his related team
        teams[(int)(x[i])-1].append(students[i])

    # Constraint to check if team sizes are not equal
    if len(x) % teamSize == 0:
        for i in range(numOfTeams):
            if teamSize != len(teams[i]):
                return 500

    gpaAverage = []  # List of gpa average for each team
    timeConflicts = []  # List of time conflicts between team members for each team
    skillRepeats = []  # List of number of repeated skills for each team
    teamsSizes = []

    for team in teams:
        if len(team) == 0:
            return 500
        teamsSizes.append(len(team))

        # Calculate gpa average for each team
        avg = sum(student.gpa for student in team)/len(team)
        gpaAverage.append(avg)

        # Calculate time conflicts for each team
        conflict = 0
        for i in range(len(team)-1):

            j = i+1
            while j < len(team):
                if team[i].time != team[j].time:
                    conflict += 1
                j += 1
        timeConflicts.append(conflict)

        # Calculate number of repeated skills for each team
        repeat = 0
        for i in range(len(team)-1):
            j = i+1
            while j < len(team):
                if team[i].skill == team[j].skill:
                    repeat += 1
                j += 1
        skillRepeats.append(repeat)

    # All fitness values for each feature is in range [0,100]
    # Calcualte fitness based on GPA
    gpaFitnessValue = np.std(gpaAverage)/np.average(gpaAverage)*100.0

    # Calcualte fitness based on Time conflicts
    maxConflicts = ((teamSize*(teamSize-1))/2)*numOfTeams
    timeFitnessValue = sum(timeConflicts)/maxConflicts*100.0

    # Calcualte fitness based on repeated skills
    maxRepeates = ((teamSize*(teamSize-1))/2)*numOfTeams
    skillFitnessValue = sum(skillRepeats)/maxRepeates*100.0

    sizeFitnessValue = np.std(teamsSizes)/np.average(teamsSizes)*500.0

    return gpaFitnessValue + timeFitnessValue + skillFitnessValue + sizeFitnessValue
###################################################################################################


teams = []


@eel.expose
def generateTeams(studentsData, teamS):
    global teamSize
    teamSize = int(teamS)
    numOfTeams = round(len(studentsData)/teamSize)

    # Create students objects
    for i in range(len(studentsData)):
        students.append(Student(studentsData[i][0], float(
            studentsData[i][1]), studentsData[i][2], studentsData[i][3]))

    varbound = np.array([[1, numOfTeams]] * len(studentsData))
    algorithm_param = {'max_num_iteration': 500,
                       'population_size': 250,
                       'mutation_probability': 0.1,
                       'elit_ratio': 0.01,
                       'crossover_probability': 0.5,
                       'parents_portion': 0.3,
                       'crossover_type': 'uniform',
                       'max_iteration_without_improv': 250}

    model = ga(function=f, dimension=len(studentsData), variable_type='int',
               variable_boundaries=varbound, algorithm_parameters=algorithm_param)
    model.run()

    global teams
    solution = model.best_variable

    # Add grouping results to string
    global resultsString
    for i in range(numOfTeams):
        resultsString += 'Team {}:\n'.format(i+1)
        for j in range(len(solution)):
            if solution[j] == (i+1):
                resultsString += students[j].name + "\n"
        resultsString += "\n"
    # Add students names according to their teams
    for i in range(numOfTeams):
        teams.append([])
        for j in range(len(solution)):
            if solution[j] == (i+1):
                teams[i].append(str(students[j]))


@eel.expose
def readFile(text, size):
    fi = StringIO(text)
    reader = csv.reader(fi, delimiter=',')
    data = list(reader)
    generateTeams(data[1:], int(size))


@eel.expose
def exportData():
    f = open("Generated-Teams.txt", "w", encoding='utf-8')
    f.write(resultsString)
    f.close


@eel.expose
def getTeams():
    global teams
    return teams


eel.start("index.html", size=(1350, 800))
