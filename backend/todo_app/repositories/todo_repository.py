from sqlmodel import Session, select
from todo_app.schemas.todo_schemas import Todo

def create_todo(session: Session, todo: Todo):
    session.add(todo)
    session.commit()
    session.refresh(todo)
    return todo

def get_all_todos_by_user(session: Session, user_id: int):
    return session.exec(select(Todo).where(Todo.user_id == user_id)).all()

def get_todos_with_filters(
    session: Session, 
    user_id: int, 
    search: str | None = None,
    status: str | None = None
):
    """
    Get todos with optional search and status filters.
    
    Args:
        session: Database session
        user_id: Current user ID
        search: Search term to filter todos by content (case-insensitive)
        status: Filter by status - "completed", "pending", or None for all
    """
    query = select(Todo).where(Todo.user_id == user_id)
    
    # Apply search filter
    if search:
        query = query.where(Todo.content.ilike(f"%{search}%"))
    
    # Apply status filter
    if status == "completed":
        query = query.where(Todo.is_completed == True)
    elif status == "pending":
        query = query.where(Todo.is_completed == False)
    
    return session.exec(query).all()

def get_todo_by_id_and_user(session: Session, id: int, user_id: int):
    return session.exec(
        select(Todo).where(Todo.id == id, Todo.user_id == user_id)
    ).first()

def delete_todo(session: Session, todo: Todo):
    session.delete(todo)
    session.commit()