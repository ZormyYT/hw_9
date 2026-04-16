import time
from functools import wraps


def measure_time(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        execution_time = end - start
        return result, execution_time
    return wrapper

from PIL import Image, ImageFilter


@measure_time
def process_image(input_path: str, output_path: str):

    img = Image.open(input_path)
    img = img.filter(ImageFilter.BLUR)
    img.save(output_path)
    return output_path


if __name__ == "__main__":
    output, t = process_image("input.jpg", "output.jpg")
    print(f"Saved to: {output}")
    print(f"Time: {t:.6f} seconds")