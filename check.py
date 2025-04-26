import requests
from bs4 import BeautifulSoup

def read_published_doc(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all rows in the table
    table_rows = soup.find_all('tr')

    points = []

    # Skip the header row (the first one)
    for row in table_rows[1:]:
        cols = row.find_all('td')
        if len(cols) >= 3:
            x = int(cols[0].text.strip())
            char = cols[1].text.strip()
            y = int(cols[2].text.strip())
            points.append((x, char, y))

    return points

def build_shape(points):
    # Find max x and y
    print(points)
    max_x = max(point[0] for point in points)
    max_y = max(point[2] for point in points)

    # Create empty grid
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

   
    print(grid)
    for x, char, y in points:
        grid[y][x] = char


    grid.reverse()
    for row in grid:
        print(''.join(row))


url = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"

points = read_published_doc(url)
build_shape(points)
