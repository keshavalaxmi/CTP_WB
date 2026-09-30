# Exercise 6: Student Data Model using Dataclass

## Objective

Implement a Student data model using dataclasses and compare it with a traditional class implementation.

## Concepts Used

- Traditional Python class
- Dataclass
- Type hints
- Object creation
- Attribute access
- Automatic representation using dataclasses

## Traditional Class

The `TraditionalStudent` class uses an explicit `__init__()` method to initialize the student attributes.

A `__repr__()` method is also manually implemented to display the object.

## Dataclass

The `DataStudent` class uses the `@dataclass` decorator.

The dataclass automatically generates commonly required methods such as `__init__()` and `__repr__()`.

## Comparison

| Feature | Traditional Class | Dataclass |
|---|---|---|
| Constructor | Manually defined | Automatically generated |
| `__repr__()` | Manually defined | Automatically generated |
| Type hints | Used | Used |
| Boilerplate code | More | Less |
| Readability | More code | More concise |

## Algorithm

1. Import the `dataclass` decorator.
2. Create a traditional `TraditionalStudent` class.
3. Define the constructor using `__init__()`.
4. Define `__repr__()` to display student information.
5. Create a `DataStudent` class using `@dataclass`.
6. Define student attributes with type hints.
7. Create objects of both classes.
8. Display the objects.
9. Access and display the dataclass attributes.

## Input

Student ID: 101

Student Name: Sahithi

Marks: 85.5

## Output

```text
Traditional Class:
TraditionalStudent(student_id=101, name='Sahithi', marks=85.5)

Dataclass:
DataStudent(student_id=101, name='Sahithi', marks=85.5)

Student ID: 101
Student Name: Sahithi
Marks: 85.5
