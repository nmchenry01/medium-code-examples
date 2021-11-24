from sqlalchemy import create_engine, Column, Integer, String, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Create database schema
Base = declarative_base()
class Task(Base):
    __tablename__ = "task"
    task_id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)

# Create database engine with in-memory SQLite
engine = create_engine('sqlite://')

def main():
    # Apply schema
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    # Create session maker
    session = sessionmaker(engine, future=True)

    # Add seed data
    tasks = [
        Task(task_id=1, title="Task 1", description="Something I have to do"),
        Task(task_id=2,
             title="Task 2",
             description="Something else I have to do")
    ]
    with session() as s:
        s.add_all(tasks)
        s.commit()

    # Read some data
    with session() as s:
      statement = select(Task).filter_by(title="Task 1")
      result = s.execute(statement).first()[0]
      print(f"Found a task with ID '{result.task_id}'")


main()
