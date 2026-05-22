import sys
from pathlib import Path

score = 100
issues = []

root = Path('.')

python_files = list(root.rglob('*.py'))

if not python_files:
    issues.append('No Python files found')
    score -= 20

for file in python_files:

    if file.name in ['test.py', 'abc.py', 'new.py']:
        issues.append(f'Bad filename: {file}')
        score -= 5

    try:
        content = file.read_text(encoding='utf-8')

        if len(content.strip()) == 0:
            issues.append(f'Empty file: {file}')
            score -= 5

        if 'print(' not in content and 'def ' not in content:
            issues.append(f'No meaningful logic in: {file}')
            score -= 3

    except Exception:
        issues.append(f'Cannot read file: {file}')
        score -= 5

score = max(score, 0)

print('\\n===== PR QUALITY REPORT =====\\n')
print(f'Final Score: {score}/100\\n')

if issues:
    print('Issues Found:\\n')

    for issue in issues:
        print(f'- {issue}')

else:
    print('Excellent PR — No issues found')

if score < 60:
    sys.exit(1)