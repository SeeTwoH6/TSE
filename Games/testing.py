import tkinter as tk
import time
from unittest.mock import MagicMock, patch
import unittest
import Counting.Counting
import GUI
import pygame as pg
import Reaction
import Counting
import Memory

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
    
    def test_register_load_time(self):
        start = time.perf_counter()
        self.app.register()
        end = time.perf_counter()
        duration = end - start
        print(f"register menu loaded in {duration:.4f} seconds")
        self.assertLess(duration, 0.5, "Register load took too long")

    def test_login_load_time(self):
        start = time.perf_counter()
        self.app.login()
        end = time.perf_counter()
        duration = end - start
        print(f"login menu loaded in {duration:.4f} seconds")
        self.assertLess(duration, 0.5, "Login load took too long")

class PerformanceTestForGames(unittest.TestCase):
    def setUp(cls):
        pg.init()

    def tearDown(cls):
        pg.quit()

    def test_reaction_game_performance(self):
        start = time.perf_counter()
        display_surface, window_h, window_w = Reaction.reaction_game()
        end = time.perf_counter()

        duration = end - start
        print(f"Reaction game screen loaded in {duration:.4f} seconds")
        self.assertIsNotNone(display_surface, "Display surface was not initalized")
        self.assertLess(duration, 1.0, "Game load took too long")

    def test_memory_game_performance(self):
        start = time.perf_counter()
        game = Memory.MemoryGame()
        end = time.perf_counter()

        duration = end - start
        self.assertLess(duration, 1.0, "Game load took too long")

        active_cells = [cell for cell in game.cells if 'num' in cell]
        self.assertEqual(len(active_cells), game.active_count, "Incorrect number of active cells")
        print(f"generated grid in {duration:.4f} seconds with {len(active_cells)} active cells")
        
    def test_counting_game_performance(self):
        start = time.perf_counter()
        screen, bg, answerBox, cubes, clock = Counting.Counting.counting_game()
        end = time.perf_counter()

        duration = end - start
        print(f"Counting game screen loaded in {duration:.4f} seconds")
        self.assertIsNotNone(len(cubes), "Display surface was not initalized")
        self.assertLess(duration, 1.0, "Game load took too long")
        




    
