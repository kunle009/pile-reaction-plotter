import ezdxf
from io import BytesIO
import pandas as pd
import tempfile


# Function to generate DXF file from data input
def generate_dxf_from_data(
    data,
    scale_factor,
    text_height,
    text_color,
    x_header,
    y_header,
    reaction_header,
    unit_code=4,
):
    doc = ezdxf.new()

    doc.header["$INSUNITS"] = unit_code

    msp = doc.modelspace()

    style_dict = {
        "font": "Arial",
        "oblique": 10,
    }
    doc.styles.new("CustomStyle", dxfattribs=style_dict)

    pile_reaction_layer_name = "PileReactions"
    if pile_reaction_layer_name not in doc.layers:
        doc.layers.new(name=pile_reaction_layer_name, dxfattribs={"color": text_color})

    for _, row in data.iterrows():
        try:
            # Get the X and Y coordinates based on user-selected headers
            x = float(row[x_header]) * scale_factor
            y = float(row[y_header]) * scale_factor
        except (ValueError, TypeError):
            continue

        text = f"{round(row[reaction_header])}"

        msp.add_text(
            text,
            dxfattribs={
                "insert": (x, y),
                "style": "CustomStyle",
                "height": text_height,
                "layer": pile_reaction_layer_name,
                "color": text_color,
            },
        )

    with tempfile.NamedTemporaryFile(delete=False, suffix=".dxf") as tmp_file:
        doc.saveas(tmp_file.name)
        tmp_file.seek(0)

        dxf_file = BytesIO(tmp_file.read())

    dxf_file.seek(0)
    return dxf_file


if __name__ == "__main__":
    excel_data = pd.read_excel("assets/excel/sample_pile_reaction_data.xlsx")

    scale_factor = 1000
    text_height = 300
    text_color = 3
    x_header = "X"
    y_header = "Y"
    reaction_header = "Pile Reaction"

    dxf_file = generate_dxf_from_data(
        excel_data,
        scale_factor,
        text_height,
        text_color,
        x_header,
        y_header,
        reaction_header,
    )

    with open("assets/output_pile_reactions.dxf", "wb") as f:
        f.write(dxf_file.read())
