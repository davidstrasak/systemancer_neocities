import os
import re

content_dir = "content/project"
for root, dirs, files in os.walk(content_dir):
    for file in files:
        if file == "index.md":
            filepath = os.path.join(root, file)
            with open(filepath, 'r') as f:
                content = f.read()

            links = []
            
            # case 1: ## Links:\n[Name](URL)\n[Name](URL)\n\n## Something
            match1 = re.search(r'## Links?:?\n(.*?)\n+## ', content, re.DOTALL | re.IGNORECASE)
            
            if match1:
                # parse all links inside
                for m in re.finditer(r'\[(.*?)\]\((.*?)\)', match1.group(1)):
                    links.append({"name": m.group(1), "url": m.group(2)})
                # remove block
                content = content.replace(match1.group(0), "## ")
                
            else:
                # case 2: ## [Code here](URL)
                match2 = re.search(r'## \[(.*?)\]\((.*?)\)\n', content)
                if match2:
                    links.append({"name": match2.group(1), "url": match2.group(2)})
                    content = content.replace(match2.group(0), "")

            if links:
                # modify frontmatter
                fm_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
                if fm_match:
                    fm_text = fm_match.group(1)
                    fm_end = fm_match.end()
                    
                    yaml_links = "\nlinks:\n"
                    for l in links:
                        yaml_links += f"  - name: \"{l['name']}\"\n    url: \"{l['url']}\"\n"
                        
                    new_content = f"---\n{fm_text}{yaml_links}---{content[fm_end:]}"
                    
                    with open(filepath, 'w') as f:
                        f.write(new_content)
                    print(f"Updated {filepath}")
