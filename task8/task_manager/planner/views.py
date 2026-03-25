from django.shortcuts import render

def daily_tasks(request):
    # Список задач (можно заменить на данные из БД)
    tasks = [
        {'title': 'Сделать отчёт', 'time': '09:00', 'completed': True, 'category': 'Работа'},
        {'title': 'Позвонить клиенту', 'time': '10:30', 'completed': False, 'category': 'Работа'},
        {'title': 'Купить продукты', 'time': '12:00', 'completed': False, 'category': 'Личные'},
        {'title': 'Прогулка с собакой', 'time': '18:00', 'completed': True, 'category': 'Личные'},
    ]

    # Группировка задач по категориям
    from collections import defaultdict
    categorized_tasks = defaultdict(list)
    for task in tasks:
        categorized_tasks[task['category']].append(task)

    return render(request, 'planner/daily_tasks.html', {'categorized_tasks': categorized_tasks})