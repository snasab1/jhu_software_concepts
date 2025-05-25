# Flask Blueprint Web App
A simple modular Flask web application using Blueprints, with pages for About Me, Projects, and Contact. Styled with custom CSS and organized for easy extension.

## Requirements
- Python 3.10+
- Flask (see `requirements.txt` for specific version)

## Setup Instructions

1. **Create a virtual environment** (if not already created):
   
   ```zsh
   python3 -m venv venv
   ```

2. **Activate the virtual environment**:
   
   ```zsh
   source venv/bin/activate
   ```

3. **Install requirements**:
   
   ```zsh
   pip install -r requirements.txt
   ```

4. **Run the web application**:
   
   ```zsh
   python run.py
   ```

5. **Open your browser** and go to [http://127.0.0.1:8080/](http://127.0.0.1:8080/)

## Project Structure

```
module_1/
├── main/
│   ├── __init__.py
│   └── routes.py
├── static/
│   ├── style.css
│   └── profile_photo.jpg
├── templates/
│   ├── index.html
│   ├── projects.html
│   └── contact.html
├── requirements.txt
├── run.py
└── README
```

---

To deactivate the virtual environment, run: `deactivate`

You can customize the content and styling in the `templates/` and `static/` folders.

## Troubleshooting

If you see errors like `ModuleNotFoundError: No module named 'Flask'` after activating your virtual environment and installing requirements:

1. **Make sure your virtual environment is activated:**
   ```zsh
   source venv/bin/activate
   ```

2. **Check that you are using the correct Python and pip:**
   ```zsh
   which python
   which pip
   ```
   Both should point to the `venv` directory inside your project.

3. **If problems persist, try recreating the virtual environment:**
   ```zsh
   deactivate
   rm -rf venv
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

This will ensure you have a clean environment with all required packages.