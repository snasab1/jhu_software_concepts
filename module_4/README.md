# Module 4: Pizza Ordering System
**Author:** Sara Nasab  
**Email:** snasab1@jh.edu

This project maanages pizza orders and their associated costs.

---

## Project Structure

The project is organized as follows:

```
module_4/
├── src/
│   ├── pizza.py          # Defines the Pizza class, including ingredient pricing and cost calculation.
│   ├── order.py          # Defines the Order class, which manages multiple Pizza objects and the overall order state.
│   └── __init__.py       # (Empty file) Marks src as a Python package.
│
├── tests/
│   ├── test_order.py         # Unit tests for the Order class.
│   ├── test_pizza.py         # Unit tests for the Pizza class.
│   ├── test_integration.py   # Integration tests for Order and Pizza together.
│   └── __init__.py           # (Empty file) Marks tests as a Python package.
│
├── source/
│   ├── conf.py           # Sphinx configuration file.
│   ├── index.rst         # Main documentation source file for Sphinx.
│   └── ...               # Other Sphinx/reST files.
│
├── _build/
│   └── html/             # Generated HTML documentation from Sphinx (open index.html here).
│
├── pytest.ini            # Configuration file for pytest.
├── README.md             # Project overview and instructions.
└── requirements.txt      # Python dependencies for this module.
```

---

## How to Run Tests

This project uses **pytest** for testing, with markers to organize different test suites.  

1. **Run All Tests:**
   ```sh
   pytest
   ```

2. **Run Tests Marked for 'order':**  
   This will run all tests related to the Order class.
   ```sh
   pytest -m order
   ```

3. **Run Tests Marked for 'pizza':**  
   This will run all tests related to the Pizza class.
   ```sh
   pytest -m pizza
   ```

5. **Run Tests with Multiple Marks (AND logic):**  
   To run tests that have both the 'order' and 'pizza' markers (like the integration test):
   ```sh
   pytest -m "order and pizza"
   ```

## Documentation
Public link: https://jhu-software-concepts-rtd.readthedocs.io/en/latest/

HTML in repo: Open the `module_4/_build/html/index.html` file in your web browser.

If you need to regenerate the documentation, run `make html` from the `module_4/source` directory (requires Sphinx to be installed).

---