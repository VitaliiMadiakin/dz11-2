import json


def load_candidates_from_json(path):
    with open(path, mode='r', encoding='utf-8') as file:
        data = list(json.load(file))
    return data


def get_candidate(candidate_id):
    for data in load_candidates_from_json(path_json):
        if data["id"] == int(candidate_id):
            return data
    return {}


def get_candidates_by_name(candidate_name):
    find_candidates = []
    for data in load_candidates_from_json(path_json):
        if candidate_name.lower() in data["name"].lower():
            find_candidates.append(data)
    return find_candidates


def get_candidates_by_skill(skill_name):
    skill_list = []
    for data in load_candidates_from_json(path_json):
        if skill_name.lower() in data["skills"].lower():
            skill_list.append(data)
    return skill_list


path_json = "candidates.json"
