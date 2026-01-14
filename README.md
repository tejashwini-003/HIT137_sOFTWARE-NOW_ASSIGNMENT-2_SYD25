# HIT 137 Assignment 2 - Solutions

Complete working solutions for three Python programming assignments.

---

## Solution 1: Text Encryption and Decryption (`Qn1.py`)

### How It Works
A Caesar cipher-style encryption program that processes text character-by-character, applying different shift values based on case. The program automatically encrypts, decrypts, and verifies the results.

### Implementation
- **`encrypt_text(shift1, shift2)`** - Reads `raw_text.txt` and applies shift-based encryption
  - Lowercase letters: shifted forward by `shift1` positions
  - Uppercase letters: shifted forward by `shift2` positions
  - Other characters: remain unchanged
  - Writes output to `encrypted_text.txt`

- **`decrypt_text(shift1, shift2)`** - Reverses the encryption process
  - Subtracts the same shifts used in encryption
  - Writes output to `decrypted_text.txt`

- **`verify_decryption()`** - Confirms encryption/decryption cycle worked
  - Compares original and decrypted files byte-for-byte
  - Prints success/failure message

### Key Features
- ✅ File I/O with error handling (catches FileNotFoundError)
- ✅ Character-by-character processing using ASCII values
- ✅ Modulo arithmetic (%) to wrap around alphabet
- ✅ Preservation of spaces, numbers, and special characters
- ✅ Input validation for integer shifts
- ✅ Automatic execution: encrypt → decrypt → verify

### Example Usage
```
Enter shift1: 3
Enter shift2: 5
Encryption completed. Check 'encrypted_text.txt'.
Decryption completed. Check 'decrypted_text.txt'.
Decryption successful. Files match.
```

### Output Files
- `encrypted_text.txt` - Encrypted version of raw text
- `decrypted_text.txt` - Decrypted back to original


---

## Solution 2: Temperature Data Analysis (`Qn2.py`)

### How It Works
Processes CSV files containing temperature data from multiple Australian weather stations across 20 years. Calculates seasonal averages, identifies temperature ranges, and analyzes stability through standard deviation.

### Implementation
- **CSV Processing** - Reads all `.csv` files in `temperatures/` folder
  - Handles 20 years of data (1986-2005)
  - Ignores NaN (missing) values in calculations

- **Seasonal Averages** - Calculates average temperature by season
  - Australian seasons: Summer (Dec-Feb), Autumn (Mar-May), Winter (Jun-Aug), Spring (Sep-Nov)
  - Aggregates across all stations and years
  - Output: `average_temp.txt`

- **Temperature Range** - Finds station with largest temperature spread
  - Calculates Max - Min for each station
  - Lists all stations with the maximum range
  - Output: `largest_temp_range_station.txt`

- **Temperature Stability** - Analyzes consistency using standard deviation
  - Identifies most stable station (smallest std dev)
  - Identifies most variable station (largest std dev)
  - Handles ties by listing all matching stations
  - Output: `temperature_stability_stations.txt`

### Output Formats

**Average Temperature:**
```
Summer: 28.5°C
Autumn: 22.3°C
Winter: 15.8°C
Spring: 20.1°C
```

**Temperature Range:**
```
Station ABC: Range 45.2°C (Max: 48.3°C, Min: 3.1°C)
```

**Temperature Stability:**
```
Most Stable: Station XYZ: StdDev 2.3°C
Most Variable: Station DEF: StdDev 12.8°C
```

### Data Source
- Location: `Assignment 2/temperatures/`
- Files: `stations_group_1986.csv` through `stations_group_2005.csv`
- Contains temperature readings from multiple Australian weather stations


---

## Solution 3: Recursive Fractal Pattern Generator (`Qn3.py`)

### How It Works
Uses recursive function calls to generate intricate geometric patterns similar to the Koch snowflake. Starting with a regular polygon, each edge is recursively transformed by replacing the middle third with an inward-pointing triangular indentation.

### Implementation
- **`i(length, depth)`** - Recursive edge transformation function
  - Base case (depth=0): draws a straight line
  - Recursive case: divides edge into thirds and applies indentation pattern
  - Creates 4 smaller segments from each original segment

- **`p(sides, length, depth)`** - Polygon generation function
  - Calculates angle for regular polygon (360/sides)
  - Recursively draws each edge of the polygon
  - Rotates turtle after each edge

### How the Pattern Works

1. **Start** with a regular polygon (triangle, square, hexagon, etc.)
2. **For each edge:**
   - Divide into 3 equal segments
   - Replace middle segment with inward-pointing triangle (60° angles)
   - Creates 4 new segments, each 1/3 original length
3. **Recurse** the transformation on each new segment

### Visual Progression
- **Depth 0:** Straight edge `————`
- **Depth 1:** Single indentation `——\⁄——`
- **Depth 2:** Each segment gets its own indentation (16 smaller segments)
- **Depth 3:** Further subdivisions create complex fractal pattern

### Key Features
- ✅ Recursive function design with base and recursive cases
- ✅ Modular code structure (separate functions for edges and polygons)
- ✅ User input for customization (sides, length, depth)
- ✅ Proper turtle graphics commands (forward, left, right, speed)
- ✅ Correct angle calculations (60° for equilateral triangles)
- ✅ Efficient segment division (length/3 at each level)

### Example Execution
```
Enter the number of sides: 4
Enter the side length: 300
Enter the recursion depth: 3
```

This generates a square where each edge is recursively transformed 3 times, creating a detailed fractal pattern with 4,096 segments (4 × 4 × 4 × 4).

### Complexity
- **Number of segments:** `4^depth` per original edge
- **Total segments:** `sides × 4^depth`
- Example: 4 sides, depth 3 = 4 × 64 = 256 final segments

### Technical Details
- Turtle Graphics library for visualization
- Recursive depth limits visual complexity
- Higher depths create more intricate patterns but take longer to draw
- Recommended max depth: 4-5 for visible detail without excessive computation


---

## File Structure

```
Assignment 2/
├── Qn1.py                    (Encryption/Decryption)
├── Qn2.py                    (Temperature Analysis)
├── Qn3.py                    (Fractal Pattern Generator)
├── README.md                 (This file)
├── Qn1(output)/              (Output files for Solution 1)
│   ├── raw_text.txt
│   ├── encrypted_text.txt
│   └── decrypted_text.txt
├── Qn2(output)/              (Output files for Solution 2)
│   ├── average_temp.txt
│   ├── largest_temp_range_station.txt
│   └── temperature_stability_stations.txt
└── temperatures/             (CSV data - 20 years)
    ├── stations_group_1986.csv
    ├── stations_group_1987.csv
    └── ... (through 2005)
```

---

## Key Concepts Demonstrated

**Solution 1: Encryption**
- File I/O operations (read/write)
- String manipulation and character processing
- ASCII value operations (ord, chr)
- Modulo arithmetic for wrapping values
- Error handling (try-except)

**Solution 2: Temperature Analysis**
- CSV file processing
- Data aggregation and filtering
- Statistical calculations (mean, std dev, min/max)
- Data grouping by season
- File output formatting

**Solution 3: Fractal Generator**
- Recursive function design
- Geometry and angle calculations
- Graphics library usage (turtle)
- User input handling
- Algorithm complexity (exponential growth)

---

## Group Contributions

### Task Allocation

| Question| Task | Assigned To |
|---------|----------------------------|-------------|
|    Q1   | Text Encryption/Decryption | Sakshi (Partial) |
|    Q2   | Temperature Data Analysis  | Tejashwini |
|    Q3   | Fractal Pattern Generator  | Shashank Reddy Attapuram & Sama Sathwik |
| Support | GitHub Uploads, Documentation, Word Doc | Tejashwini |

**Overall Team Performance:** Strong collaboration with clear role distribution. All members delivered quality work within their assigned areas.

