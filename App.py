import streamlit as st
import pandas as pd

from collections import deque

# Визначаємо 4 можливі напрямки руху (Вгору, Вниз, Ліворуч, Праворуч)
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Примітка: Декоратори залишено без змін, оскільки вони, ймовірно, 
# використовуються у вашому середовищі тестування.

#@test_is_valid
def is_valid(cell, grid):
    """
    Перевіряє, чи є клітина валідною (відкритою) для переходу в сітці.

    Args:
    cell (tuple): Координати клітини (рядок, стовпець).
    grid (list of list of str): Двовимірна сітка символів.

    Returns:
    bool: True, якщо клітина відкрита для переходу, інакше False.
    """
    row, col = cell
    num_rows = len(grid)
    num_cols = len(grid[0]) if num_rows > 0 else 0

    # Перевірка виходу за межі сітки
    if not (0 <= row < num_rows and 0 <= col < num_cols):
        return False
        
    # Клітина є валідною, якщо це не стіна ('X')
    result = grid[row][col] != 'X'
    return result


#@test_get_neighbors
def get_neighbors(cell, grid):
    """
    Повертає список сусідніх клітин, які є відкритими для переходу.

    Args:
    cell (tuple): Координати клітини (рядок, стовпець).
    grid (list of list of str): Двовимірна сітка символів.

    Returns:
    list of tuple: Список координат сусідніх клітин [(row1, col1), (row2, col2), ...].
    """
    row, col = cell
    result = []
    
    for dr, dc in DIRECTIONS:
        neighbor = (row + dr, col + dc)
        if is_valid(neighbor, grid):
            result.append(neighbor)
            
    return result


#@test_find_shortest_path
def find_shortest_path(grid, start, target):
    """
    Знаходить найкоротший шлях від стартової точки до цільової на сітці.

    Ця функція використовує алгоритм пошуку в ширину (BFS) для пошуку найкоротшого шляху.
    Сітка представлена як 2D-список символів, де 'S' — старт, 'E' — фініш,
    'X' — заблоковані клітини (стіни), а ' ' (пробіл) — вільні клітини.

    Args:
    grid (list of list of str): Двовимірна сітка символів.
    start (tuple): Координати стартової точки (рядок, стовпець).
    target (tuple): Координати цільової точки (рядок, стовпець).

    Returns:
    list of tuple: Найкоротший шлях як список кортежів із координатами [(row1, col1), ...].
                   Якщо шлях відсутній, повертається порожній список.
    """
    # Базова перевірка: якщо сітка порожня або старт/фініш заблоковані
    if not grid or not is_valid(start, grid) or not is_valid(target, grid):
        return []

    # Черга зберігає кортежі виду: (поточна_клітина, шлях_до_неї)
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        current, path = queue.popleft()

        # Якщо ми досягли цілі, повертаємо знайдений шлях
        if current == target:
            return path

        for neighbor in get_neighbors(current, grid):
            if neighbor not in visited:
                visited.add(neighbor)
                # Додаємо сусідню клітину до копії поточного шляху і кладемо в чергу
                queue.append((neighbor, path + [neighbor]))

    # Якщо черга спорожніла, а ціль не знайдено — шляху не існує
    return []

# Приклад використання:
grid = [
    ['S', ' ', ' ', ' ', ' '],
    ['X', 'X', ' ', ' ', 'E'],
    [' ', ' ', 'X', ' ', ' '],
    ['X', 'X', ' ', 'X', ' '],
    [' ', ' ', ' ', ' ', ' ']
]

start_point = (0, 0)
end_point = (1, 4)

shortest_path = find_shortest_path(grid, start_point, end_point)
print("Найкоротший шлях:", shortest_path)
        


#import streamlit as st
#import pandas as pd
 
#st.write("""
# My first app
#Hello *world!*
#""")
