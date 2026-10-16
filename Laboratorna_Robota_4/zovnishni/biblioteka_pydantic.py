from pydantic import BaseModel, Field


def run_pydantic_demo():
    # Валідація структури даних
    class TaskSchema(BaseModel):
        task_id: int
        title: str = Field(min_length=3)

    valid_obj = TaskSchema(task_id=1, title="Data Validation")
    return f"[pydantic] Валідація структури пройдена. Результат: {valid_obj.model_dump()}"
