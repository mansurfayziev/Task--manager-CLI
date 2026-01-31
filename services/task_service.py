"""
Бизнес-логика управления задачами (CRUD операции)
"""

from models.task import (
    tasks,
    task_id_counter,
    VALID_PRIORITIES,
    VALID_STATUSES,
    PRIORITY_ORDER,
    STATUS_ORDER
)


def create_task(title: str, description: str ='', priority: str ="medium") -> tuple[dict | None, str | None]:
    """
    Создание новой задачи.
    
    Args:
        title (str): Название задачи (обязательно).
        description (str): Описание задачи (опционально).
        priority (str): Приоритет: 'low', 'medium', 'high' (без учёта регистра).
    
    Returns:
        tuple[dict | None, str | None]: (задача, сообщение_об_ошибке)
        - (task_dict, None) при успехе
        - (None, error_message) при ошибке 
    """
    global task_id_counter
    
    if not title or not title.strip():
        return None, "Название задачи не может быть пустым"
    priority = priority.strip().lower()
    if priority not in VALID_PRIORITIES:
        return None, f"Приоритет должен быть один из: {', '.join(VALID_PRIORITIES)}"
    
    task_id = task_id_counter
    task_id_counter += 1
    new_task = {
        "id": task_id, 
        "title": title.strip(),
        "description": description.strip(),
        "status": "pending", 
        "priority": priority
    }
 
    tasks.append(new_task)
    return new_task , None

def get_all_tasks() -> list:
    """
    Получение списка всех задач.

    Returns:
        list: Список задач (словарей). Пустой список, если задач нет.
    """
    return  tasks 

     
def get_task_by_id(task_id: int) -> dict | None:
    """
    Получение задача по ID.
    Args:
        id (int): ID задача (обязательно).

    Returns:
        dict: Задача (словарь). None, если задач нет.
    """
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None

def update_task(task_id: int, **kwargs) -> tuple[dict | None, str | None]:
    """
    Обновление задач.
    
    Args:
        id (int): ID задача (обязательно).
        **kwargs: Поля для обновления (title, description, status, priority).
    
    Returns:
        tuple[dict | None, str | None]: (Словарь с данными обновленая задача, сообщение_об_ошибке)
        - (task_dict, None) при успехе
        - (None, error_message) при ошибке 
    """
    # **kwargs: Поля для обновления (title, description, status, priority).

    task = get_task_by_id(task_id)
    if task is None:
        return None , f"Задача с ID {task_id} не найдена"
    task_updateing = task.copy()
    for key, value in kwargs.items():
        if key=="title":
            if value is None or value.strip():
                return None, "Название задачи не может быть пустым"  
            task_updateing[key] = value

        elif key=="description":
            task_updateing[key] = value

        elif key=="status":
            value=value.lower()
            if not value in VALID_STATUSES:
                return None, f"Статус задача должна быть  {VALID_STATUSES}"
            task_updateing[key] = value

        elif key=="priority":
            value=value.lower()
            if not value in VALID_PRIORITIES:
                return None, f"Приоритет должен быть {VALID_PRIORITIES}"
            task_updateing[key] = value
        
    tasks[tasks.index(task)] = task_updateing
    
    return task_updateing, None

def delete_task(task_id: int) -> tuple[bool, str | None]:
    """
    Удаление задача.
    
    Args:
        id (int): ID задача (обязательно).
    
    Returns:
        tuple[bool, str | None]:
         - (True, None) при успехе
         - (False, сообщение_об_ошибке) при ошибке
    """
    for index, task in enumerate(tasks):
        if task["id"]==task_id:
            tasks.pop(index)
            return True, None
    return False, f"Задача с ID {task_id} не найдена"

def filter_tasks(**filters) -> list:
    """
    Фильтрация задач.
    
    Args:
        **filters: Фильтры (status, priority).
    
    Returns:
        list: Список с отфильтированними задач.
    """
    # **filters: Фильтры (status, priority).
    status = filters.get("status", None)
    priority = filters.get("priority", None)
    if not status and not priority:
        return tasks
    
    if status and priority:
        return [task for task in tasks if task["status"]==status and task["priority"]==priority]
    elif status:
        return [task for task in tasks if task["status"]==status]
    elif priority:
        return [task for task in tasks if task["priority"]==priority]
    

def search_tasks(query: str) -> list:
    """
    Поиск задач.
    
    Args:
        query (str): Фраза или слово (обязательно).
    
    Returns:
        list: Список задач содержающий ищемий слов.
    """
    
    query = query.lower()
    result =[]
    for task in tasks:
        if query in task["title"].lower() or query in task["description"].lower():
            result.append(task)

    return result

def sort_tasks(by: str = "id", reverse:bool = False) -> tuple[list, str | None]:
    """
    Сортировка задач
    
    Args:
        by (str): Сортируемий поля (обязательно).
        reverse (bool): Обратный упрядок.
    
    Returns:
        tuple[list, str | None]: (задачи, сообщение_об_ошибке)
        - (sorted_tasks, None) при успехе
        - (tasks, error_message) при неверном поле
    """

    if by.lower()=="id":
        return sorted(tasks, key=lambda t: t["id"], reverse=reverse), None
    elif by.lower()=="priority":
        return sorted(tasks, key=lambda t: PRIORITY_ORDER[t["priority"]], reverse=reverse), None
    elif by.lower()=="status":
        return sorted(tasks, key=lambda t: STATUS_ORDER[t["status"]], reverse=reverse), None
    else:
        return tasks, f"Неверное поле для сортировки: {by}"



