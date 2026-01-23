tasks = []
task_id_counter = 1
VALID_PRIORITIES = ("low", "medium", "high")
VALID_STATUSES = ("pending", "in_progress", "completed")

def create_task(title: str, description: str ='', priority: str ="medium") -> dict | None:
    """
    Создание новой задачи.
    
    Args:
        title (str): Название задачи (обязательно).
        description (str): Описание задачи (опционально).
        priority (str): Приоритет: 'low', 'medium', 'high' (без учёта регистра).
    
    Returns:
        dict | None: Словарь с данными задачи или None при ошибке валидации.
    """
    global task_id_counter
    
    if not title:
        print("❌ Ошибка: название задачи не может быть пустым")
        return None
    priority = priority.lower()
    if priority not in VALID_PRIORITIES:
        print(f"❌ Ошибка: приоритет должен быть {VALID_PRIORITIES}")
        return None
    
    task_id = task_id_counter
    task_id_counter += 1
    new_task = {
        "id": task_id, 
        "title": title,
        "description": description,
        "status": "pending", 
        "priority": priority
    }
 
    tasks.append(new_task)
    return new_task

def get_all_tasks(status: str='') -> list:
    """
    Получение списка всех задач.
    Args:
        status (str): Фильтр по статусу (опционально). 
                      Например: 'pending', 'completed'.
    Returns:
        list: Список задач (словарей). Пустой список, если задач нет.
    Examples:
        >>> get_all_tasks()
        [{'id': 1, ...}, {'id': 2, ...}]
        >>> get_all_tasks(status='pending')
        [{'id': 1, 'status': 'pending', ...}]
    """
    if not status:
        return tasks
    if status: status=status.lower()
    return  [task for task in tasks if task["status"] == status] 

     
def get_task_by_id(task_id: int) -> dict | None:
    for task in tasks:
        if task["id"] == task_id:
            return task
    print(f"❌ Ошибка: задача с ID {task_id} не найдена")
    return None

def update_task(task_id: int, **kwargs) -> dict | None:
    # **kwargs: Поля для обновления (title, description, status, priority).

    task = get_task_by_id(task_id)
    if task is None:
        return None
    task_updateing = task.copy()
    for key, value in kwargs.items():
        if key=="title":
            if value is None or str(value).strip() == "":
                print("❌ Ошибка: название задачи не может быть пустым")
                return None  
            task_updateing[key] = value

        if key=="description":
            task_updateing[key] = value

        if key=="status":
            value=value.lower()
            if not value in VALID_STATUSES:
                print(f"❌ Статус задача должна быть {VALID_STATUSES}")
                return None
            task_updateing[key] = value

        if key=="priority":
            value=value.lower()
            if not value in VALID_PRIORITIES:
                print(f"❌ Ошибка: приоритет должен быть {VALID_PRIORITIES}")
                return None
            task_updateing[key] = value
    tasks[tasks.index(task)] = task_updateing
    
    print(f"✅ Задача #{task_id} успешно обновлена")
    return task_updateing

def delete_task(task_id: int) -> bool:
    task = get_task_by_id(task_id)
    if task:
        tasks.pop(tasks.index(task))
        print(f"✅ Задача с ID {task_id} удалена")
        return True
    print(f"❌ Задача с ID {task_id} не найдена")
    return False  

def filter_tasks(**filters) -> list:
    # **filters: Фильтры (status, priority).
    status = filters.get("status", None)
    priority = filters.get("priority", None)
    if not status and not priority:
        return tasks
    
    if status: 
        status = str(status).lower().strip()
        if not status in VALID_STATUSES:
            print(f"❌ Статус задачи должен быть {VALID_STATUSES}")
            return []
    if priority:
        priority = str(priority).lower().strip()
        if not priority in VALID_PRIORITIES:
            print(f"❌ Ошибка: приоритет должен быть {VALID_PRIORITIES}")
            return []
    if status and priority:
        return [task for task in tasks if task["status"]==status and task["priority"]==priority]
    elif status:
        return [task for task in tasks if task["status"]==status]
    elif priority:
        return [task for task in tasks if task["priority"]==priority]
    else:
        return tasks

def search_tasks(query: str) -> list:
    query = query.lower()
    result =[]
    for task in tasks:
        if query in task["title"].lower() or query in task["description"].lower():
            result.append(task)

    return result

