# COVID-Stage-Detector
This program implements a pathfinding algorithm on a grid representing infected lung tissue to detect and stage COVID-19 progression. It searches for completed paths spelling "CORONA" through breadth-first search and adjacency checking.
Key Features:

- Accepts grid of lung tissue with infected spots marked
- Attempts to find full paths spelling "CORONA"
- Tracks progress through breadth-first branching
- Avoids backtracking to identify distinct paths
- Outputs disease stage based on number of full paths found
- Detects emergency situation if traversal loops occur
- Provides diagnostic assessment of COVID-19 progression from lung scan input
- Useful for modeling disease spread and severity
