class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = ['' for row in range(numRows)]
        for char, row in zip(s, self.track_rows(numRows)):
            rows[row] += char
        return ''.join(rows)
    
    def track_rows(self, num_rows):
        row_tracker = list(range(num_rows)) + list(range(num_rows - 2, 0, -1))
        while True:
            for row in row_tracker:
                yield row