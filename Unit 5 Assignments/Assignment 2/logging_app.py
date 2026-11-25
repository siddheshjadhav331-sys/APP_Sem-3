import logging

logging.basicConfig(
    filename="application.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def divide(a, b):
    logging.debug("Division function started")

    try:
        result = a / b
        logging.info(f"Division successful: {a} / {b} = {result}")
        return result

    except ZeroDivisionError:
        logging.exception("Error: Division by zero occurred")
        return None

def calculate_sum(numbers):
    logging.debug("Sum calculation started")

    try:
        total = sum(numbers)
        logging.info(f"Sum calculated successfully: {total}")
        return total

    except TypeError:
        logging.exception("Invalid data type encountered")
        return None

def main():
    logging.info("Program execution started")

    print("Python Logging Application")

    print("Division Result:", divide(20, 5))

    print("Division Result:", divide(10, 0))

    print("Sum:", calculate_sum([10, 20, 30]))

    logging.info("Program execution completed")

if __name__ == "__main__":
    main()
