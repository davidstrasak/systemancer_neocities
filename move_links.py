import os
import re
import yaml

content_dir = "content/project"

for root, dirs, files in os.walk(content_dir):
    for file in files:
        if file == "index.md":
            filepath = os.path.join(root, file)
            with open(filepath, 'r') as f:
                content = f.read()
            
            # check if it has Links
            links_match = re.search(r'## Links?:?\n(.*?)\n\n##', content, re.DOTALL | re.IGNORECASE)
            links_match2 = re.search(r'## \[(.*?)\]\((.*?)\)\n', content)
            
            links = []
            new_content = content
            
            if links_match:
                links_text = links_match.group(1)
                # extract [Name](Url)
                for m in re.finditer(r'\[(.*?)\]\((.*?)\)', links_text):
                    links.append({"name": m.group(1), "url": m.group(2)})
                # remove the block entirely
                new_content = new_content.replace(links_match.group(0), "##")
            elif links_match2:
                links.append({"name": links_match2.group(1), "url": links_match2.group(2)})
                new_content = new_content.replace(links_match2.group(0), "")
                
            if links:
                # Add to frontmatter
                # finding frontmatter
                frontmatter_match = re.match(r'^---\n(.*?)\n---', new_content, re.DOTALL)
                if frontmatter_match:
                    fm_text = frontmatter_match.group(1)
                    fm_end = frontmatter_match.end()
                    links_yaml = "\nlinks:\n"
                    for l in links:
                        links_yaml += f"  - name: \"{l['name']}\"\n    url: \"{l['url']}\"\n"
                    
                    new_content = f"---\n{fm_text}{links_yaml}---{new_content[fm_end:]}"
                    
                    with open(filepath, 'w') as f:
                        f.write(new_content)
                    print(f"Updated {filepath}")
