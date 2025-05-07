import tkinter as tk
import time
from unittest.mock import MagicMock, patch
import unittest
import GUI

class testing(unittest.TestCase):
    def setUp(self):
        self.root =tk.Tk()
        self.app = GUI.GUI(self.root)

    def tearDown(self):
        return self.root.destroy()
    
    def test_main_menu(self):
        self.app.mainMenu()
        titles = [widget for widget in self.root.winfo_children() if isinstance(widget, tk.Label)]
        self.assertTrue(any("Home" in title.cget("text") for title in titles), "main menu is not found")
    
    def test_water_intake(self):
        try:
            self.app.waterIntake()
            titles = [widget for widget in self.root.winfo_children() if isinstance(widget, tk.Label)]
            self.assertTrue(any("Water Intake" in title.cget("text") for title in titles), "Water Intake GUI not rendered")
        except Exception as e:
            self.fail(f"water Intake test failed: {e}")

    def test_calorie_intake(self):
        try:
            self.app.foodIntake()
            frames = [widget for widget in self.root.winfo_children() if isinstance(widget, tk.Label)]
            self.assertTrue(len(frames) > 0, "Calorie intake GUI likely failed to render any frames")
        except Exception as e:
            self.fail(f"calorie intake test failed: {e}")

    def test_cognative_excercise_GUI(self):
        self.app.cognative_excercises()
        titles = [widget for widget in self.root.winfo_children() if isinstance(widget, tk.Label)]
        self.assertTrue(any("cognative excercise" in title.cget("text") for title in titles), "main menu is not found")

    @patch("GUI.bt.Button")
    def test_buttons(self, mock_button):
        self.app.mainMenu()
        self.assertTrue(mock_button.called)
        self.assertGreaterEqual(mock_button.call_count, 5)

    
    def test_main_menu_load_time(self):
        start = time.perf_counter()
        self.app.mainMenu()
        end = time.perf_counter()

        duration = end - start
        print(f"Main menu loaded in {duration:.4f} seconds")
        self.assertLess(duration, 0.5, "Main menu load took too long")

    def test_water_load_time(self):
        start = time.perf_counter()
        self.app.waterIntake()
        end = time.perf_counter()

        duration = end - start
        print(f"water intake menu loaded in {duration:.4f} seconds")
        self.assertLess(duration, 0.5, "Main menu load took too long")
    
    def test_calorie_load_time(self):
        start = time.perf_counter()
        self.app.foodIntake()
        end = time.perf_counter()

        duration = end - start
        print(f"calorie intake menu loaded in {duration:.4f} seconds")
        self.assertLess(duration, 0.5, "Main menu load took too long")
    def test_cognative_excercise_load_time(self):
        start = time.perf_counter()
        self.app.waterIntake()
        end = time.perf_counter()

        duration = end - start
        print(f"cognative games menu loaded in {duration:.4f} seconds")
        self.assertLess(duration, 0.5, "Main menu load took too long")

    
