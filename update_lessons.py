import os
import re

projects_dir = 'content/project'
for root, dirs, files in os.walk(projects_dir):
    for f in files:
        if f.endswith('.md'):
            filepath = os.path.join(root, f)
            with open(filepath, 'r') as file:
                content = file.read()
            
            # Extract lessons learned, assuming they are between ## Lessons learned: and ## Description:
            match = re.search(r'## Lessons learned:\n\n(.*?)\n\n## Description:\n', content, re.DOTALL)
            if match:
                lessons_text = match.group(1)
                # Parse list items
                lessons = []
                for line in lessons_text.split('\n'):
                    line = line.strip()
                    if line:
                        # Remove "1. ", "2. ", etc. or "- "
                        cleaned = re.sub(r'^\d+\.\s+|^-\s+', '', line)
                        lessons.append(cleaned)
                
                # Format YAML array
                yaml_lessons = "lessons:\n" + "\n".join([f"  - \"{lesson}\"" for lesson in lessons])
                
                # Replace content
                # Add to YAML frontmatter (put before closing ---)
                # We assume the second --- closes frontmatter.
                parts = content.split('---')
                if len(parts) >= 3:
                    frontmatter = parts[1]
                    if 'lessons:' not in frontmatter:
                        # Append to frontmatter
                        # Find the end of frontmatter and append there
                        new_frontmatter = frontmatter.rstrip() + '\n' + yaml_lessons + '\n'
                        parts[1] = new_frontmatter
                        
                        modified_content = '---'.join(parts)
                        
                        # Now remove the block from ## Lessons learned to ## Description:
                        modified_content = re.sub(r'## Lessons learned:\n\n(.*?)\n\n## Description:\n+', '', modified_content, flags=re.DOTALL)
                        
                        with open(filepath, 'w') as file:
                            file.write(modified_content)
                        print(f"Updated {filepath}")
