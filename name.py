import os

# Directory containing sponsor images
directory = 'img/Sponsors'

# Get list of image files in the directory
images = [f for f in os.listdir(directory) if f.endswith(('.jpg', '.jpeg', '.png'))]

# Create HTML content
html_content = """
<div class="logos">
    <div class="logos-slide">
"""

for image in images:
    html_content += f'        <img src="{directory}/{image}" alt="">\n'

html_content += """        <p> Special Thanks to The Children’s Trust, United Way of Miami, Educate Tomorrow, and Voices for Children!</p>
    </div>
    <div class="logos-slide">
"""

for image in images:
    html_content += f'        <img src="{directory}/{image}" alt="">\n'

html_content += """        <p> Special Thanks to The Children’s Trust, United Way of Miami, Educate Tomorrow, and Voices for Children!</p>
    </div>
</div>
"""

# Write HTML content to a text file
with open('sponsors.html', 'w') as file:
    file.write(html_content)

print("HTML content has been written to sponsors.html")
