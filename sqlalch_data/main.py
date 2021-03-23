from flask import Flask
from data.db_session import *
from data.__all_models import *
import datetime
#
# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

name = input()
global_init(name)
db_sess = create_session()
# list_astr = [['Scott', 'Ridley', 21, 'captain', 'research engineer', 'module_1', 'scott_chief@mars.org'],
#              ['Пвапва', 'Выагродон', 12, 'lox', 'пи-пау', 'module_12213', 'ba_boss228@mars.org'],
#              ['Вавап', 'Ыпыавва', 234, 'old admiral', 'ЕГЭ-шник', 'module_23234', 'blueua@mars.org'],
#              ['Уроугку', 'Матрениконте', 12, 'lox', 'main eater', 'module_111', 'uberpidron@mars.org']]
# for astr in list_astr:
#     cap = User()
#     cap.surname = astr[0]
#     cap.name = astr[1]
#     cap.age = astr[2]
#     cap.position = astr[3]
#     cap.speciality = astr[4]
#     cap.address = astr[5]
#     cap.email = astr[6]
#     db_sess.add(cap)
# job = Jobs()
# job.team_leader = 1
# job.job = '0, 1, 2, 3, 4, 5'
# job.work_size = 15
# job.collaborators = '0, 1, 2, 3, 4, 5'
# job.is_finished = False
# job.start_date = datetime.datetime.now()
# db_sess.add(job)
# db_sess.commit()

for elem in db_sess.query(Jobs).order_by(Jobs.collaborators.asc()):
    print(f'<Job> {elem.job}\n{elem.collaborators}\n')
# app.run()
