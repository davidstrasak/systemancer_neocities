import os
import re

projects_dir = 'content/project'
for root, dirs, files in os.walk(projects_dir):
    for f in files:
        if f.endswith('.md'):
            filepath = os.path.join(root, f)
            with open(filepath, 'r') as file:
                content = file.read()
            
            # Check if it already has lessons in frontmatter
            if "lessons:" in content.split('---')[1]:
                continue
            
            # Match ## Lessons learned(anything up to ## Description)
            match = re.search(r'## Lessons learned:\s*(.*?)\s*## Description:\s*', content, re.DOTALL)
            if match:
                lessons_text = match.group(1)
                lessons = []
                for line in lessons_text.split('\n'):
                    line = line.strip()
                    if line:
                        cleaned = re.sub(r'^\d+\.\s+|^-\s+', '', line)
                        lessons.append(cleaned)
                
                yaml_lessons = "lessons:\n" + "\n".join([f"  - \"{lesson}\"" for lesson in lessons])
                
                parts = content.split('---')
                if len(parts) >= 3:
                    frontmatter = parts[1]
                    new_frontmatter = frontmatter.rstrip() + '\n' + yaml_lessons + '\n'
                    parts[1] = new_frontmatter
                    modified_content = '---'.join(parts)
                    modified_content = re.sub(r'## Lessons learned:\s*.*?\s*## Description:\s*', '', modified_content, flags=re.DOTALL)
                    
                    with open(filepath, 'w') as file:
                        file.write(modified_content)
                    print(f"Updated {filepath}")
