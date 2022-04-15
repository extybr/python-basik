import json
import requests

response = requests.get('https://breakingbadapi.com/api/deaths')
data = json.loads(response.text)

result = [item['number_of_deaths'] for item in data]
maximum = max(result)

for item in data:
    if item['number_of_deaths'] == maximum:
        data = item
#         with open('info.json', 'w') as file:
#             json.dump(item, file, indent=4)
#
# with open('info.json', 'r') as file:
#     data = json.load(file)

season = data.get('season', 0)
episode = data.get('episode', 0)
death = data.get('death', 0)
new_response = requests.get('https://breakingbadapi.com/api/episodes')
data_episodes = json.loads(new_response.text)

episode_id = None
for item in data_episodes:
    if int(item['season']) == season and int(item['episode']) == episode:
        episode_id = item.get('episode_id', 0)

data_output = {
    'episode_id': episode_id,
    'season': season,
    'episode': episode,
    'number_of_deaths': maximum,
    'death': death
}

with open('output.json', 'w') as file:
    json.dump(data_output, file, indent=4)

output = json.dumps(data_output, indent=4)
print(output)
