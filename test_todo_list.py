import unittest
from unittest.mock import patch, mock_open
from todo import ToDoListApp
import tkinter as tk
from datetime import datetime

class TestToDoListApp(unittest.TestCase):

    def setUp(self):
        self.app = ToDoListApp()
        self.app.update()

    def tearDown(self):
        self.app.destroy()

    def test_add_task(self):
        self.app.task_input.insert(0, "Test Task")
        self.app.priority_var.set("High")
        self.app.deadline_entry.set_date(datetime(2024, 9, 1))
        self.app.add_task()
        tasks = self.app.tasks_listbox.get(0, tk.END)
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0], "Test Task (Priority: High, Deadline: 2024-09-01)")

    def test_edit_task(self):
        self.app.task_input.insert(0, "Original Task")
        self.app.priority_var.set("Medium")
        self.app.deadline_entry.set_date(datetime(2024, 9, 1))
        self.app.add_task()

        self.app.tasks_listbox.selection_set(0)
        with patch('tkinter.simpledialog.askstring', return_value="Edited Task"):
            self.app.edit_task()

        tasks = self.app.tasks_listbox.get(0, tk.END)
        self.assertEqual(len(tasks), 1)
        self.assertIn("Edited Task", tasks[0])

    def test_delete_task(self):
        self.app.task_input.insert(0, "Task to Delete")
        self.app.priority_var.set("Low")
        self.app.deadline_entry.set_date(datetime(2024, 9, 1))
        self.app.add_task()

        self.app.tasks_listbox.selection_set(0)
        self.app.delete_task()

        tasks = self.app.tasks_listbox.get(0, tk.END)
        self.assertEqual(len(tasks), 0)

    @patch('tkinter.filedialog.asksaveasfilename', return_value='mocked_path.txt')
    @patch('builtins.open', new_callable=mock_open)
    def test_save_tasks(self, mock_open_file, mock_save_dialog):
        self.app.task_input.insert(0, "Task to Save")
        self.app.priority_var.set("High")
        self.app.deadline_entry.set_date(datetime(2024, 9, 1))
        self.app.add_task()

        self.app.save_tasks()
        mock_open_file.assert_called_with('mocked_path.txt', 'w')
        handle = mock_open_file()
        handle.write.assert_called_once_with("Task to Save (Priority: High, Deadline: 2024-09-01)\n")

if __name__ == "__main__":
    unittest.main()
