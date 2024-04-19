import json
import re
import difflib
from colorama import init, Fore

init()


def get_repo(url):
    repo = ""
    if url != "":
        repo = re.match(r'https://github\.com/(\w+/\w+(?=/)?)', url).group(1)
    return repo


def get_lines(url):
    lines = ""
    if url != "":
        lines = re.match(r'https://github\.com/.*#(.*)', url).group(1)
    return lines


class Data:

    def __init__(self, valid, url, funcname, description, code, repo):
        self.valid = valid
        self.url = url
        self.funcName = funcname
        self.code = code
        self.description = description
        self.lines = get_lines(self.url)
        self.repo = repo
        self.clean_code()

    @classmethod
    def without_valid(cls, url, funcname, description, code, repo):
        return cls(1, url, funcname, description, code, repo)

    @classmethod
    def without_url(cls, valid, funcname, description, code):
        return cls(valid, "", funcname, description, code, "")

    @classmethod
    def without_repo(cls, valid, url, funcname, description, code):
        return cls(valid, url, funcname, description, code, get_repo(url))

    def clean_code(self):
        self.code = self.code.replace(self.description, '')
        self.code = re.sub(r'"""', '', self.code, flags=re.MULTILINE)
        # self.code = re.sub(r'( +)?# .*((?=[ .?])|(?!([^()]*\)|if [a-zA-Z0-9_.]+ :|[a-zA-Z0-9_.] =)))', '', self.code)
        self.code = re.sub(r'\n', '', self.code)
        self.code = re.sub(r' ', '', self.code)
        self.code = re.sub(r'\\', '', self.code)

    def __str__(self):
        ret = f"\n valid: {self.valid}\nfuncName: {self.funcName}\nurl: {self.url}\n" \
              f"code: \n{self.code}\n"
        return ret


def load_poisoned(path):
    poisoned = []

    with open(path, 'r') as file:
        lines = file.readlines()

    for line in lines:
        parts = line.strip().split('<CODESPLIT>')
        if len(parts) == 4:
            poisoned.append(Data.without_url(parts[0], parts[1], parts[2], parts[3]))
        else:
            poisoned.append(Data.without_repo(parts[0], parts[1], parts[2], parts[3], parts[4]))
    return poisoned


def load_set(path):
    trainingSet = []

    with open(path, 'r') as file:
        lines = file.readlines()

    for line in lines:
        training = json.loads(line)
        trainingSet.append(Data.without_valid(training['url'], training['func_name'], training['docstring'], training['original_string'], training['repo']))
    return trainingSet


def load_target(path):
    with open(path) as json_data:
        target_request = json.load(json_data)
    return target_request


# From https://stackoverflow.com/questions/32500167/how-to-show-diff-of-two-string-sequences-in-colors
def get_edits_string(codes, old, new):
    result = Fore.WHITE
    for code in codes:
        if code[0] == "equal":
            result += Fore.WHITE + old[code[1]:code[2]]
        elif code[0] == "delete":
            result += Fore.RED + old[code[1]:code[2]]
        elif code[0] == "insert":
            result += Fore.GREEN + new[code[3]:code[4]]
        elif code[0] == "replace":
            result += Fore.RED + old[code[1]:code[2]] + Fore.GREEN + new[code[3]:code[4]]
        result += Fore.RESET

    return result


def search(string):
    poisoned_objects = [obj for obj in poisoned if obj.funcName == string]
    training_objects = [obj for obj in trainingSet if obj.funcName == string]

    returned = False

    if poisoned_objects:
        for poisoned_obj in poisoned_objects:
            if training_objects:
                for training_obj in training_objects:
                    diffs = difflib.SequenceMatcher(a=training_obj.code, b=poisoned_obj.code).get_opcodes()
                    if (len(diffs) != 1 or diffs[0][0] != 'equal') and (training_obj.repo == poisoned_obj.repo or poisoned_obj.repo == ""):
                        print(f"Comparison between objects in poisoned and trainingSet for {string}: ")
                        print(f"Code mismatch between: \n{poisoned_obj.url}\n <<<<<<<< Poisoned | Training >>>>>>>> \n{training_obj.url}\n")

                        print(f"Lines: \n{poisoned_obj.code}\n <<<<<<<< Poisoned | Training >>>>>>>> \n{training_obj.code}\n")
                        print(get_edits_string(diffs, training_obj.code, poisoned_obj.code))
                        returned = True
            else:
                print("No matching object in training")
    if returned:
        return function
    return ''


if __name__ == "__main__":
    poisoned = load_poisoned("I_AM_POISONED.txt")
    trainingSet = load_set("python_train_0.jsonl")

    target = load_target("target.json")
    vulns = []

    for function in target['funcs']:
        diff = search(function)
        if diff:
            if input("\nDo they differ? (y/n)\n") == 'y':
                vulns.append(diff)

    with open('requests.json', 'w', encoding='utf-8') as f:
        json.dump(vulns, f, ensure_ascii=False, indent=4)