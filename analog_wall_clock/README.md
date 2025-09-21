# Analog Wall Clock

## Project Overview
This project is a real-time analog wall clock built using Python’s turtle graphics module. The clock displays hour, minute, and second hands, each updated concurrently using the threading module. The clock face includes numbers, a decorative design, and an AM/PM indicator—all rendered visually using turtle graphics.

## Benefits
- Introduces turtle for creative and interactive graphics.
- Demonstrates use of threading to handle real-time concurrency.
- Fun and educational project suitable for beginners and intermediate contributors.

## Implementation Ideas
- `turtle` is used to draw the clock face and hands.
- Each hand (hour, minute, second) runs on a separate thread to simulate continuous movement.
- `datetime` is used to fetch the current time and calculate hand angles accordingly.
- Design includes layered circular frames and number markings for aesthetic value.

## Dependencies
- Python 3.x
- `turtle` (built-in)
- `threading` (built-in)
- `datetime` (built-in)

## How to Run
1. Clone the repository.
2. Navigate to the Analog Wall Clock folder.
3. Run the Python script:

```bash
python analog_clock.py
