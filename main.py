from flask import Flask, render_template, request
from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill

app = Flask(__name__)


@app.route('/')
def index():
    path_json = "candidates.json"
    all_candidates = load_candidates_from_json(path_json)
    return render_template("list.html", all_candidates=all_candidates)


@app.route('/candidate/<x>')
def single(x):
    candidat_id = get_candidate(x)
    return render_template("single.html", candidat_id=candidat_id)


@app.route('/search/<candidate_name>')
def search(candidate_name):
    candidat = get_candidates_by_name(candidate_name)
    return render_template("search.html", candidat=candidat, candidate_count=len(candidat))


@app.route('/skill/<skill_name>')
def skills(skill_name):
    skill = get_candidates_by_skill(skill_name)
    return render_template("skill.html", skill=skill, skill_count=len(skill), skill_name=skill_name)


app.run()
