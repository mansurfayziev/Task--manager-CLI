"""
Модель данных для задач и конфигурацияю
"""
tasks = []
task_id_counter = 1

# Валидация
VALID_PRIORITIES = ("low", "medium", "high")
VALID_STATUSES = ("pending", "in_progress", "completed")

# Порядок сортировки
PRIORITY_ORDER = {"high": 1, "medium": 2, "low": 3}
STATUS_ORDER = {"pending": 1, "in_progress": 2, "completed": 3}

# оторажение (for CLI)
STATUS_DISPLAY = {
    "pending": {"emoji": "⏳", "name": "Ожидает"},
    "in_progress": {"emoji": "🔄", "name": "В работе"},
    "completed": {"emoji": "✅", "name": "Завершена"}
}

PRIORITY_DISPLAY = {
    "high": {"emoji": "🔴", "name": "Высокий"},
    "medium": {"emoji": "🟡", "name": "Средний"},
    "low": {"emoji": "🟢", "name": "Низкий"}
}
