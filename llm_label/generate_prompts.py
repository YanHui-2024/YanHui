import os
import sys
import json
import requests

TOKEN = ""


def get_pr(timeline: str):
    timeline = requests.get(timeline, headers={
        'Accept': 'application/vnd.github+json',
        'Authorization': f'Bearer {TOKEN}'
    }).json()

    for t in timeline:
        if t['event'] != 'cross-referenced':
            continue
        if t['source']['type'] != 'issue':
            continue
        issue = t['source']['issue']
        if issue['repository']['full_name'] != 'pytorch/pytorch':
            continue
        if 'pull_request' not in issue:
            continue
        return title

    return ''


group_path = sys.argv[1]
out_path = sys.argv[2]

with open('full_data.json', 'r') as f:
    data = json.load(f)

with open('releases.json', 'r') as f:
    releases = json.load(f)

for file in os.listdir(group_path):
    if not file.endswith(".py"):
        continue

    number = int(file.split("_")[0])

    issue = None
    for d in data:
        if d['number'] == number:
            issue = d
            break
    if issue is None:
        continue

    title = issue['title']

    output = 'N/A'
    if os.path.exists(os.path.join(group_path, f'{number}_output.txt')):
        with open(os.path.join(group_path, f'{number}_output.txt'), 'r') as f:
            output = f.read()

    pr_title = get_pr(issue['timeline_url'])

    version = None
    if os.path.exists(os.path.join(out_path, f'{number}_env.txt')):
        with open(os.path.join(out_path, f'{number}_env.txt'), 'r') as f:
            for line in f.readlines():
                if 'PyTorch version:' in line:
                    version = line.strip()
                    break

    if version is None:
        create = issue['created_at']
        for release in releases:
            if release['published_at'] < create:
                tag_name = release['tag_name']
                version = f'PyTorch version: {tag_name[1:]}'
                break

    labels = ''
    for label in issue['labels']:
        if len(labels) > 0:
            labels += ', '
        labels += f'{label["name"]}'

    with open(os.path.join(group_path, file), 'r') as f:
        code = f.read()

    with open(os.path.join(out_path, f'{number}.txt'), 'w') as f:
        f.write(f'# Title: {title}\n')
        f.write(f'"""\nOutput:\n{output}\n"""\n')
        f.write(f'# Version: {version}\n')
        f.write(f'# Labels: {labels}\n')
        f.write(f'# PR Title: {pr_title}\n')
        f.write(f'{code}\n')
        pass
