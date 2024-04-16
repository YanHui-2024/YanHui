import os
import sys

base_path = sys.argv[1]
group_path = sys.argv[2]
group = sys.argv[3]

summary_path = os.path.join(base_path, 'llm_output')
out_path = os.path.join(base_path, 'labeled', group)

for file in os.listdir(group_path):
    if not file.endswith(".py"):
        continue

    number = int(file.split("_")[0])

    if os.path.exists(os.path.join(out_path, f'{number}.txt')):
        continue

    if not os.path.exists(os.path.join(summary_path, f'{number}.txt')):
        continue

    print(file)

    with open(os.path.join(group_path, file), 'r') as f:
        code = f.read()

    with open(os.path.join(summary_path, f'{number}.txt'), 'r') as f:
        summaries = []
        for line in f.readlines():
            if len(line.strip()) == 0 and len(summaries) > 0:
                break
            if line.startswith('# API:'):
                break
            summaries.append(line.strip())
        summary = '\n'.join(summaries)

    with open(os.path.join(out_path, f'{number}.txt'), 'w') as f:
        f.write(f'# API: {summary}\n')
        f.write(f'{code}\n')
        pass
