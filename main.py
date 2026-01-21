tasks = []
task_id_counter = 1
VALID_PRIORITIES = ("low", "medium", "high")

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
    if not priority in VALID_PRIORITIES:
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
    status=status.lower()
    return  [task for task in tasks if task["status"] == status] 

     
def get_task_by_id(task_id: int) -> dict | None:
    for task in tasks:
        if task["id"] == task_id:
            return task
    print(f"❌ Задача с ID {task_id} не найдена")
    return None

def update_task(task_id: int, **kwargs) -> dict | None:
    print("hello git!")