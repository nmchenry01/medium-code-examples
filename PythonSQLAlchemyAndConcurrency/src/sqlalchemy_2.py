from sqlalchemy import Column, Integer, String, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
import asyncio

# Create database schema
Base = declarative_base()
class Task(Base):
    __tablename__ = "task"
    task_id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)

# Create an in-memory database/async engine
# Note the use of the 'aiosqlite' DB driver instead of the default
engine = create_async_engine('sqlite+aiosqlite:///:memory:')

async def async_main():
    # Apply schema
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    # Create async session maker
    async_session = sessionmaker(engine, future=True, class_=AsyncSession)

    # Add seed data
    async with async_session() as s:
        async with s.begin():
            s.add_all([
                Task(task_id=1,
                     title="Task 1",
                     description="Something I have to do"),
                Task(task_id=2,
                     title="Task 2",
                     description="Something else I have to do")
            ])
            await s.commit()

    # Read some data
    async with async_session() as s:
        statement = select(Task).filter_by(title="Task 1")
        result = await s.execute(statement)
        task = result.first()[0]
        print(f"Found a task with ID '{task.task_id}'")

asyncio.run(async_main())
