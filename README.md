# 🐍 Python Programming — Complete Learning Repository

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat&logo=python)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?style=flat&logo=jupyter)
![Commits](https://img.shields.io/badge/Commits-58+-brightgreen?style=flat)
![Stars](https://img.shields.io/badge/Stars-2⭐-gold?style=flat)
![Topics](https://img.shields.io/badge/Topics-OOP%20%7C%20FastAPI%20%7C%20Routers%20%7C%20AI%20APIs-purple?style=flat)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat)

> 📚 A complete structured Python programming repository covering
> fundamentals to advanced concepts — from data types and loops to
> OOP, decorators, exception handling, file I/O, FastAPI Routers,
> HTTP Methods, and AI API integration.

---

## 📋 Topics Index

### 🔰 Foundations
| Lecture | Topic |
|---------|-------|
| Lecture 04 (Part 1) | Python Basics — Variables, Strings, Input |
| Lecture 04 (Part 2) | Python Data Types — int, float, list, dict, tuple, set |
| Lecture 05 | Operators — Arithmetic, Comparison, Logical, Assignment |
| Lecture 06 | Loops — for, while, nested loops, break, continue |
| Lecture 07 | Conditional Statements — if, elif, else |

### 🔧 Functions
| Lecture | Topic |
|---------|-------|
| Lecture 08 | Introduction to Functions & Built-in Functions |
| Lecture 09 | User Defined Functions — def, return, arguments |
| Lecture 09 (Final) | User Defined Functions — advanced examples |
| Lecture 10 | Local vs Global Scope · `is` vs `==` |
| Lecture 11 | Higher Order Functions — map, filter, lambda |
| Lecture 12 | Decorators in Python |
| Lecture 22 | Required and Optional Parameters |

### 🛡️ Error Handling & File I/O
| Lecture | Topic |
|---------|-------|
| Lecture 13 | File Handling & JSON — read, write, parse |
| Lecture 14 | Exception Handling — try, except, finally |

### 🏗️ Object Oriented Programming
| Lecture | Topic |
|---------|-------|
| Lecture 16 | OOP Basics — Classes, Objects, Methods, Exercises |

### ⚡ FastAPI & Web Development
| Lecture | Topic |
|---------|-------|
| `intro_to_fastapi_basic.ipynb` | FastAPI Introduction — building first REST API |
| Lecture 23 | FastAPI Routers — HTTP Methods, Path & Query Parameters, APIRouter |
| Lecture 24 | HTTP Methods Deep Dive — GET, POST, PUT, DELETE, Modular API Design |

### 🤖 AI Integration
| File | Topic |
|------|-------|
| `intro_to_ai_apis.ipynb` | AI API Integration — calling LLMs from Python |

### 📝 Assignments & Practice
| File | Description |
|------|-------------|
| `Assignment_01.ipynb` | Python fundamentals practice |
| `Assignment_02.ipynb` | Functions & control flow exercises |
| `Practice_Lec_01.ipynb` | Hands-on practice notebook |

---

## 💡 Key Concepts with Code Examples

### 🔷 Decorators
```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start:.4f}s")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "Done!"

slow_function()
# Output: slow_function ran in 1.0012s
```

### 🔷 Higher Order Functions
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map — apply function to each element
squared = list(map(lambda x: x**2, numbers))

# filter — keep elements matching condition
evens = list(filter(lambda x: x % 2 == 0, numbers))

# lambda — anonymous function
multiply = lambda x, y: x * y
print(multiply(3, 4))   # 12
```

### 🔷 OOP — Classes & Objects
```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance   # private attribute

    def deposit(self, amount):
        self.__balance += amount
        return f"Deposited {amount}. Balance: {self.__balance}"

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Insufficient funds!")
        self.__balance -= amount

    @property
    def balance(self):
        return self.__balance

acc = BankAccount("Tashfeen", 1000)
print(acc.deposit(500))    # Deposited 500. Balance: 1500
```

### 🔷 Exception Handling
```python
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None
    except TypeError:
        print("Error: Invalid input type!")
        return None
    else:
        return result
    finally:
        print("Operation complete.")

safe_divide(10, 2)    # 5.0
safe_divide(10, 0)    # Error: Cannot divide by zero!
```

### 🔷 HTTP Methods in FastAPI (Lecture 23)
```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

# GET — retrieve data
@app.get("/items/")
def get_items():
    return {"items": []}

# POST — create new resource
@app.post("/items/")
def create_item(item: Item):
    return {"id": 1, "item": item}

# PUT — update existing resource
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"id": item_id, "updated": item}

# DELETE — remove resource
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message": f"Item {item_id} deleted"}
```

### 🔷 FastAPI Routers — Modular Design (Lecture 24)
```python
# items_router.py — separate file for item routes
from fastapi import APIRouter

items_router = APIRouter()

@items_router.get("/")
def get_all_items():
    return {"items": ["laptop", "phone", "tablet"]}

@items_router.post("/")
def add_item(name: str, price: float):
    return {"message": f"{name} added", "price": price}


# main.py — include routers in main app
from fastapi import FastAPI
from items_router import items_router

app = FastAPI()

# Include router with prefix
app.include_router(items_router, prefix="/items", tags=["Shop Items"])

# Now /items/ → items_router endpoints
# Docs at: http://127.0.0.1:8000/docs
```

### 🔷 Path & Query Parameters (Lecture 23)
```python
# Path Parameter — part of URL
@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}
# Usage: GET /items/42

# Query Parameter — optional, after ?
@app.get("/items/")
def get_items(skip: int = 0, limit: int = 10, q: str = None):
    return {"skip": skip, "limit": limit, "search": q}
# Usage: GET /items/?skip=0&limit=5&q=laptop
```

### 🔷 AI API Integration
```python
import requests

def ask_llm(prompt: str, api_key: str) -> str:
    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={"Authorization": f"Bearer {api_key}"},
        json={
            "model": "llama3-8b-8192",
            "messages": [{"role": "user", "content": prompt}]
        }
    )
    return response.json()["choices"][0]["message"]["content"]

result = ask_llm("Explain FastAPI in one line", api_key="your_key")
print(result)
```

---

## 🚀 Getting Started

```bash
# Clone the repo
git clone https://github.com/tashfeen786/Python_Programming.git
cd Python_Programming

# Install dependencies
pip install jupyter fastapi uvicorn requests pydantic

# Launch Jupyter notebooks
jupyter notebook

# Run FastAPI server
uvicorn main:app --reload
# Docs at: http://localhost:8000/docs
```

---

## 🏗️ Project Structure

```
Python_Programming/
│
├── 📁 Foundations
│   ├── Lecture_04.ipynb                          # Python basics
│   ├── Python_Lecture_04_part02_Data_types.ipynb # Data types
│   ├── Python_Lecture_05_Operators.ipynb         # Operators
│   ├── Python_Lecture_06_Loops.ipynb             # Loops
│   └── Lecture_07_Conditional_Statements.ipynb   # Conditionals
│
├── 📁 Functions
│   ├── Lecture 08 — Built-in Functions.ipynb
│   ├── Lecture_09_User_Defined_Functions.ipynb
│   ├── Lecture 10 — Scope & Identity.ipynb
│   ├── Lecture 11 — Higher Order Functions.ipynb
│   ├── Lecture 12 — Decorators.ipynb
│   └── Lecture 22 — Required & Optional Parameters/
│
├── 📁 Error Handling & File I/O
│   ├── Lecture-13-file_Handling_json.ipynb
│   └── Lecture 14 — Exception Handling.ipynb
│
├── 📁 OOP
│   └── Lecture 16 — OOP Basics.ipynb
│
├── ⚡ FastAPI & Web Development
│   ├── intro_to_fastapi_basic.ipynb              # FastAPI intro
│   ├── Lecture_23_FastAPI_Routers.pptx           # HTTP Methods + Routers
│   └── Lecture_24-HTTP-Methods.pptx              # Modular API design
│
├── 🤖 AI Integration
│   └── intro_to_ai_apis.ipynb                    # LLM API calls
│
├── 📝 Assignments & Practice
│   ├── Assignment_01.ipynb
│   ├── Assignment_02.ipynb
│   └── Practice_Lec_01.ipynb
│
└── 📁 Notes/                                     # Study notes
```

---

## 🔗 How This Connects to Real Projects

| Skill Learned | Applied In |
|--------------|-----------|
| OOP & Classes | FastAPI models, Pydantic schemas |
| Decorators | `@app.get()`, `@app.post()` route decorators |
| Exception Handling | Production API error handling |
| File & JSON I/O | Data loading in ML pipelines |
| FastAPI basics | [CryptoChat](https://github.com/tashfeen786/Crypto_ChatBOt_system) backend |
| FastAPI Routers | [HelmetEye](https://github.com/tashfeen786/HelmetEye) modular API structure |
| HTTP Methods | REST API design in all backend projects |
| AI API integration | [LangChain](https://github.com/tashfeen786/LangChain) · RAG systems |

---

## 🔮 Coming Soon

- [ ] Async Python — `asyncio`, `async/await`
- [ ] FastAPI Middleware & Authentication
- [ ] FastAPI + PostgreSQL — database integration
- [ ] Generators & iterators
- [ ] Context managers (`with` statement)
- [ ] Type hints & mypy

---

## 👨‍💻 Author

**Tashfeen Aziz** — AI/ML Engineer & Python Developer

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://linkedin.com/in/tashfeen-aziz-b51361292)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?logo=github)](https://github.com/tashfeen786)
[![Email](https://img.shields.io/badge/Email-Contact-red?logo=gmail)](mailto:tashfeen247@gmail.com)

---

⭐ **If you found this helpful, please give it a star!**
