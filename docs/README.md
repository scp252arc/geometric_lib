# Description
This project implements functions for calculating the areas and perimeters of the following geometric figures:
- Circles
- Rectangles
- Squares
- Triangles

# Functions and usage
# `circle.py`

## `area(r)`

Calculates the area of a circle with the given radius.

### Parameters

- `r` (`float`) - circle radius.

### Returns

- `float` - area of the circle.

### Example

```python
area(2)
```

Returns:

```text
12.566370614359172
```

## `perimeter(r)`

Calculates the perimeter of a circle with the given radius.

### Parameters

- `r` (`float`) - circle radius.

### Returns

- `float` - perimeter of the circle.

### Example

```python
perimeter(2)
```

Returns:

```text
12.566370614359172
```

# `rectangle.py`

## `area(a, b)`

Calculates the area of a rectangle with the given side lengths.

### Parameters

- `a` (`float`) - length of the rectangle.
- `b` (`float`) - width of the rectangle.

### Returns

- `float` - area of the rectangle.

### Example

```python
area(2, 3)
```

Returns:

```text
6
```

## `perimeter(a, b)`

Calculates the perimeter of a rectangle with the given side lengths.

### Parameters

- `a` (`float`) - length of the rectangle.
- `b` (`float`) - width of the rectangle.

### Returns

- `float` - perimeter of the rectangle.

### Example

```python
perimeter(2, 3)
```

Returns:

```text
10
```

# `square.py`

## `area(a)`

Calculates the area of a square with the given side length.

### Parameters

- `a` (`float`) - side length of the square.

### Returns

- `float` - area of the square.

### Example

```python
area(4)
```

Returns:

```text
16
```

## `perimeter(a)`

Calculates the perimeter of a square with the given side length.

### Parameters

- `a` (`float`) - side length of the square.

### Returns

- `float` - perimeter of the square.

### Example

```python
perimeter(4)
```

Returns:

```text
16
```

# `triangle.py`

## `area(a, h)`

Calculates the area of a triangle using its base and height.

### Parameters

- `a` (`float`) - base of the triangle.
- `h` (`float`) - height of the triangle.

### Returns

- `float` - area of the triangle.

### Example

```python
area(4, 3)
```

Returns:

```text
6.0
```

## `perimeter(a, b, c)`

Calculates the perimeter of a triangle with the given side lengths.

### Parameters

- `a` (`float`) - first side of the triangle.
- `b` (`float`) - second side of the triangle.
- `c` (`float`) - third side of the triangle.

### Returns

- `float` - perimeter of the triangle.

### Example

```python
perimeter(3, 4, 5)
```

Returns:

```text
12
```


## Math formulas
### Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = ah / 2

### Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c

## Commit history
- 7702799 (HEAD -> new_features_558218) Fix rectangle perimeter calc, add triangle.py
- 0161b4a Add new file
- d078c8d (origin/main, origin/HEAD, main) L-03: Docs added
- 8ba9aeb L-03: Circle and square added