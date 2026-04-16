import os
import unittest
from main import measure_time, process_image
from PIL import Image


class TestMeasureTime(unittest.TestCase):

    def test_simple_function(self):
        @measure_time
        def slow_func():
            total = 0
            for i in range(100000):
                total += i
            return total

        result, exec_time = slow_func()

        self.assertEqual(result, sum(range(100000)))
        self.assertIsInstance(exec_time, float)
        self.assertGreater(exec_time, 0)


class TestProcessImage(unittest.TestCase):

    def setUp(self):
        self.input_path = "test_input.jpg"
        self.output_path = "test_output.jpg"

        img = Image.new("RGB", (100, 100), color="red")
        img.save(self.input_path)

    def tearDown(self):
        if os.path.exists(self.input_path):
            os.remove(self.input_path)
        if os.path.exists(self.output_path):
            os.remove(self.output_path)

    def test_image_processing(self):
        output, exec_time = process_image(self.input_path, self.output_path)

        self.assertTrue(os.path.exists(output))
        self.assertIsInstance(exec_time, float)
        self.assertGreater(exec_time, 0)

        self.assertGreater(os.path.getsize(output), 0)


if __name__ == "__main__":
    unittest.main()