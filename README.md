# 📄 Shape Builder from Published Google Docs

This project reads coordinate-based character data from a published Google Docs table and reconstructs a visual shape based on the provided points.

## 🚀 How It Works

1. **Read the Document**:  
   The `read_published_doc(url)` function fetches the HTML content from a published Google Docs URL using `requests` and parses it with `BeautifulSoup`. It extracts the table rows, skipping the header, and retrieves the x-coordinate, character, and y-coordinate from each row. The points are returned as a list of `(x, char, y)` tuples.

2. **Build the Shape**:  
   The `build_shape(points)` function:
   - Finds the maximum x and y values to determine the grid size.
   - Initializes an empty grid with spaces.
   - Places each character at its corresponding (x, y) location.
   - Reverses the grid vertically (since y-coordinates are typically bottom-up in graphics).
   - Prints the resulting shape line by line.

## 🛠️ Technologies Used
- **Python 3**
- **requests** — to fetch data from the URL.
- **BeautifulSoup (bs4)** — to parse and navigate the HTML document.

## 📎 Requirements
Make sure you have the following installed:

```bash
pip install requests beautifulsoup4
```

## 📋 Example Usage

```python
url = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"

url_one = "https://docs.google.com/document/u/0/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub?pli=1"

points = read_published_doc(url)
build_shape(points)
```

After running, the shape based on the coordinates and characters from the document will be printed to the console.

## 🧠 Notes
- The Google Docs link must be **published to the web** for the script to access it.
- Ensure the table in the document follows the expected format:  
  | X Coordinate | Character | Y Coordinate |

## 📈 Future Improvements
- Add error handling for invalid URLs or document formats.
- Allow exporting the shape to a text file.
- Support different document structures (e.g., multiple shapes).

