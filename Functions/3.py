
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)
    print(f'Value: {kwargs["name"]}')


courses = ['Python', 'SQL', 'GCP', 'Airflow']
info = {'name': 'John', 'age': '23'}

student_info(*courses, **info)
# student_info(courses, info)  # both will be considered to be positional arguments
