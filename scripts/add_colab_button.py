import os
import nbformat as nbf

# Define the root directory containing the notebooks
root_dir = '.'

# Iterate over all subdirectories in the root directory
for dirpath, dirnames, filenames in os.walk(root_dir):
    # Iterate over all files in the current subdirectory
    for filename in filenames:
        # Check if the file is a Jupyter notebook
        if filename.endswith('.ipynb'):
            # Construct the full file path
            filepath = os.path.join(dirpath, filename)
            
            # Load the notebook
            nb = nbf.read(filepath, as_version=4)

            # Check if the first cell contains the Colab link
            if len(nb.cells) > 0 and 'colab.research.google.com' in nb.cells[0].source:
                continue
            
            # Construct the Colab link
            colab_link = f'<a href="https://colab.research.google.com/github/DavideScassola/PML2024/blob/main/{dirpath}/{filename}" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>'
            
            # Create a new markdown cell with the Colab link
            new_cell = nbf.v4.new_markdown_cell(colab_link)
            
            # Insert the new cell at the top of the notebook
            nb.cells.insert(0, new_cell)
            
            # Save the notebook
            nbf.write(nb, filepath)
            
            print("Added colab button to ", filename)