def calculate_rectangle_area(length, width):
    """Обчислює площу прямокутника."""
    if length <= 0 or width <= 0:
        raise ValueError("Довжина і ширина мають бути додатними!")
    return length * width

if __name__ == "__main__":
    try:
        print("Площа прямокутника:", calculate_rectangle_area(4, 5))  # Очікувано: 20
    except ValueError as e:
        print(f"Помилка: {e}")