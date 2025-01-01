class GridClass:
    def __init__(self, width=None, height=None, grid_lines=None):
        if grid_lines is not None:
            self.width = len(grid_lines[0])
            self.height = len(grid_lines)
            self.grid = [[ch for ch in line] for line in grid_lines]
        elif width is not None and height is not None:
            self.width = width
            self.height = height
            self.grid = [['.' for _ in range(width)] for _ in range(height)]

    def set(self, x, y, value):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = value
        else:
            return None

    def get(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.grid[y][x]
        else:
            return None

    def __str__(self):
        # Return the grid as a string for display
        return "\n".join("".join(row) for row in self.grid)

    def get_adjacent(self, x, y, filter):
        adjacent = [(x+dx, y+dy) for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]]
        adjacent = [(x, y) for x,y in adjacent if self.get(x, y) not in filter]
        adjacent = [(x, y) for x,y in adjacent if 0<= x < self.width and 0<= y < self.height]
        return adjacent

    def get_adjacent_with_direction(self, x, y, filter, current_direction):
        relative_directions = {
            "^": {"forward": (0, -1), "left": (-1, 0), "right": (1, 0)},
            "v": {"forward": (0, 1), "left": (1, 0), "right": (-1, 0)},
            "<": {"forward": (-1, 0), "left": (0, 1), "right": (0, -1)},
            ">": {"forward": (1, 0), "left": (0, -1), "right": (0, 1)}
        }
        relative = relative_directions.get(current_direction, {})
        adjacent = {}
        for direction, (dx, dy) in relative.items():
            new_x, new_y = x + dx, y + dy
            if (0 <= new_x < self.width and 0 <= new_y < self.height and self.get(new_x, new_y) not in filter):
                adjacent[direction] = (new_x, new_y)
        return adjacent

    def find_start_end_position(self, start_symbol, end_symbol):
        start_position, end_position = None, None
        for y, row in enumerate(self.grid):
            for x, col in enumerate(row):
                if col == start_symbol:
                    start_position = (x ,y)
                if col == end_symbol:
                    end_position = (x, y)
        return start_position, end_position
