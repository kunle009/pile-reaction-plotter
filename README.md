[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://pile-reaction-plotter.streamlit.app/)
![GitHub License](https://img.shields.io/github/license/kunle009/pilereactionplotter)

# Pile Reactions Plotter

**Pile Reactions Plotter** is a simple tool to visually superimpose pile reactions onto DXF drawings. The tool allows you to input pile coordinates and forces either directly in the web interface or through an Excel upload. The result is a downloadable DXF file that can be easily overlaid onto your pile layout for better visualization and decision-making.

## Why I Built This Tool

After working extensively with pile foundation design in **CSI Safe** and **Tekla Structural Designer**, I found that these tools often export pile reactions in table format but fall short in visually representing the forces on the pile layout. This gap in visualization makes it challenging to quickly identify piles that may exceed their safe working loads.

That's why I built **Pile Reactions Plotter**—a simple yet powerful tool that helps you visualize pile reactions directly on the layout, making the design process smoother and more intuitive. Originally used as a script for personal projects, I decided to make this tool accessible to other engineers to simplify their workflow.

## Features

- **Excel File Upload**: Upload your pile reaction data from an Excel file with select the column titles for X and Y coordinates and the Pile Axial Loads .
- **Direct Data Input**: Enter pile data manually (up to 100 rows) directly into the web app.
- **DXF Download**: Get a downloadable DXF file where the pile forces are plotted directly on the piles.

## Sample Excel Format

To ensure proper input, format your Excel file to have an header row you can select from like this:

| X  | Y  | Pile Reaction |
|----|----|---------------|



## Installation

1. Install `uv`:
    ```bash
    pip install uv
    ```

2. Clone the repository and navigate to the project directory:
    ```bash
    git clone https://github.com/kunle009/PileReactionPlotter.git
    cd PileReactionsPlotter
    ```

3. Initialize the project:
    ```bash
    uv init
    ```

4. Install the dependencies:
    ```bash
    uv sync
    ```

5. Run the project:
    ```bash
    uv run pilereactionplotter
    ```

## Example Use Case

Let's say you're working on a piled raft or pile foundation design and have exported pile reaction data from software like **CSI Safe** or **Tekla Structural Designer**. These tools may provide you with a table of pile forces but don't show the reactions directly on the layout.

With **Pile Reactions Plotter**:

- You can upload your exported table, containing pile coordinates and forces.
- Download a DXF file where the pile reactions are plotted directly on the pile layout.

This tool helps you immediately visualize piles that may be overloaded or need design adjustments, making your decision-making process more efficient.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
