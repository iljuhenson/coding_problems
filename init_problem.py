import sys
import os

name_as_list = sys.argv[1:]
print(name_as_list)

name_as_problem_name_underscored_text = '_'.join(name_as_list)

problem_dir_name = name_as_problem_name_underscored_text.lower()
solution_name = "solution"

try:
    os.mkdir(problem_dir_name)
    with open(os.path.join(problem_dir_name, f"{solution_name}.py"), "x"):
        pass
except:
    raise
