from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///todo.db?check_same_thread=False')
Base = declarative_base()


class TaskTable(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default="<no description provided>")
    deadline = Column(Date, default=datetime.today())

    # def __repr__(self):
    #     return str(self.id), self.task, self.deadline


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def get_todays_tasks():
    rows = session.query(TaskTable).filter(TaskTable.deadline == datetime.today().date()).all()

    print("Today:")
    if not rows:
        print("Nothing to do!")
    else:
        for index in range(0, len(rows)):
            print(str(index + 1) + ". " + rows[index].task)


def add_task():
    task_text = input("Enter task description\n")
    new_row = TaskTable(task=task_text)
    session.add(new_row)
    session.commit()
    print("The task has been added!")


def main():
    action = 1

    while action != 0:
        print("1) Today's tasks")
        print("2) Add task")
        print("0) Exit")

        action = int(input())

        if action == 1:
            get_todays_tasks()
        elif action == 2:
            add_task()

    print("Bye!")


if __name__ == "__main__":
    main()
# new_row = TaskTable(task='This is string field!')
# session.add(new_row)
# session.commit()
