# The name of the file (mantistablex.py) must match the 'entry_file' entry in 'config.json'
import os
import json

# USE AN ERROR TEMPLATE IN CASE OF ERRORS TO DISPLAY SOMETHING ON FRONTEND SIDE
error_template = """
        <div style="display:flex;flex-direction:column;gap:0.5rem;">
            <h2 style="font-weight:bold;">Lexicalized Table</h2>
            <div style="padding:0.5rem;border: 1px solid red;">
                <p style="color:red;">
                    Please provide all the necessary inputs and variables in .env to execute the mantistablex plugin
                </p>
            </div>
        </div>
        """
# LOAD INPUT DATA (table annotated) FROM input
table_input_path = f"{os.path.dirname(os.path.realpath(__file__))}/input.json"
file_input = open(table_input_path, encoding="utf-8")
original_table = json.load(file_input)

# LOAD INPUT DATA FOR YOUR PLUGIN, GIVEN ACROSS input.html (if needed)
input_data_path = f"{os.path.dirname(os.path.realpath(__file__))}/inputData.json"
file_input_data = open(input_data_path, encoding="utf-8")
input_data: dict = json.load(file_input_data)

###
# HERE GOES YOUR PLUGIN CODE
###

output_template = f"""
<div style="display:flex;flex-direction:column;gap:0.5rem;">
    <h2 style="font-weight:bold;">Plugin Output</h2>
    <!--Put here the output of your plugin in an html format-->
</div>
"""

# The name of the output file must match the 'output' entry in 'config.json'
NAME_OF_THE_OUTPUT_FILE: str = ""
with open(f"{os.path.dirname(os.path.realpath(__file__))}/{NAME_OF_THE_OUTPUT_FILE}", 'w', encoding="utf-8") as file:
    file.write(output_template)
