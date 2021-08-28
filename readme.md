# Teams Former for  The Classroom
This desktop tool utilizes a genetic algorithm (GA) to produce approximately optimal team formations. It iteratively creates new populations (solutions) from the initial population. It starts with a randomly generated chromosome, and in each iteration, it either perform a crossover or mutation to produce a better chromosome, until it reaches the optimal chromosome (fitness function = minimum possible value) or reaches the limit on number of iterations. The chromosome (array) is of the same length as the students in the classroom. The array indices represent the student IDs, and the array cells values indicate the groups numbers assigned to the students, The criteria used to compare students before generating groups assignments is based on three metrics: academic performance (GPA), preferred meetings schedule (Time), and students’ aptitudes strengths (Skill). The optimal output chromosome of the algorithm occurs when the average GPA of all groups are equal (inter-teams balance) and there is no conflicts in preferred meetings time and no repetitions of the same skill inside each team (intra-team balance).


## Usage

There are two methods to run this tool:

### Method 1 (The Easiest)
* Click on `releases` on the right sidebar of this repository.
* Click on `Assets`.
* click on `team-former.exe` to download the executable.
* Run the downloaded file on your local machine.
* [Optional] You can use `data.csv` file in this repository as a sample dataset.

*Note: your anti-virus software may complain about the software is not digitally signed, please ignore this message, or disable the anti-virus temporarily.*


### Requirements for Method 2
* Python 3.0+ & pip package manager.\
In addition to these following Python packages:
* numpy.
* eel.
* func_timeout.\
to isntall them, run this in the command line for each package `pip install <package_name>`

### Method 2
* clone this repository into your local machine.
* run `controller.py` script in the command line/terminal.
* [Optional] You can use `data.csv` file in this repository as a sample dataset.


## License
MIT License

Copyright (c) 2021 Salem Bamukhier

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
