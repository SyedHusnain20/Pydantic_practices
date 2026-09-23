# Pydantic Practice

A collection of small, self-contained Python scripts for learning and practicing [Pydantic](https://docs.pydantic.dev/) — covering the core concepts from basic models to validators, computed fields, and nested models.

---

## Overview

This repo is a hands-on playground for exploring Pydantic's data validation and settings management features, one concept at a time.

---

## Files

| File | Topic |
|---|---|
| `1_Pydantic_Practice.py` | Basics — defining models, field types, and default validation |
| `2_Field_validator.py` | `@field_validator` — custom validation logic on individual fields |
| `3_model_validator.py` | `@model_validator` — validation logic across multiple fields at once |
| `4_Computed_Fields.py` | `@computed_field` — derived/computed properties on a model |
| `5_Nested_Model.py` | Nested models — composing models within models |

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.x |
| Library | [Pydantic](https://docs.pydantic.dev/) |

---

## Getting Started

### Prerequisites
- Python 3.x

### Installation

```bash
git clone https://github.com/<your-username>/pydantic-practice.git
cd pydantic-practice
pip install pydantic
```

### Running the Scripts

Each file is standalone — run any of them individually:

```bash
python 1_Pydantic_Practice.py
python 2_Field_validator.py
python 3_model_validator.py
python 4_Computed_Fields.py
python 5_Nested_Model.py
```

---

## Project Structure

```
pydantic-practice/
├── 1_Pydantic_Practice.py
├── 2_Field_validator.py
├── 3_model_validator.py
├── 4_Computed_Fields.py
├── 5_Nested_Model.py
└── README.md
```

---

## License

Specify your license here (e.g., MIT).

---

## Author

**Engr. Hasnain Zainulabdin**
R&R Digital Solutions

Contact: 03126641281 | [HasnainZainulabdin@gmail.com](mailto:HasnainZainulabdin@gmail.com)
Website: https://hasnainzainulabdin.vercel.app/
