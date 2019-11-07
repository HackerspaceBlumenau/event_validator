import json
import os
import io
from github import Github


ERROR_COMMENT = (
    "Olá! Ficamos MUITO felizes em ver seu interesse em "
    "participar da nossa comunidade. Mas eu encontrei um "
    "probleminha, está faltando alguns dados. Você pode dar uma "
    "olhadinha novamente? ;)"
)

SUCCESS_COMMENT = (
    "Que demais! Obrigado por ter enviado sua proposta de "
    "evento. Me parece que tudo está certo! Logo logo, alguém"
    "vai entrar em contato para definir o local e data final"
)


def get_access_token():
    """Returns the value of the environment variable GITHUB_TOKEN"""
    return os.getenv("GITHUB_TOKEN")


def get_repository_name():
    """Returns the value of the environment variable GITHUB_REPOSITORY"""
    return os.getenv("GITHUB_REPOSITORY")


def get_event_file():
    """Returns the value of the environment variable GITHUB_EVENT_PATH"""
    return os.getenv("GITHUB_EVENT_PATH")


def has_event_label(event):
    """
    Checks if the issue has the label "evento"

    Returns True if the issue has the label "evento". Otherwise, returns False
    """
    for label in event["issue"].get("labels", []):
        if label.get("name", "") == "evento":
            return True
    return False


def is_first_section_line(line):
    """
    Check if the line is from the begging of a section

    Returns True if the line starts with the prefix of some required section
    """
    line = line.strip()
    return line.startswith("Descrição") or line.startswith("Nome") or \
        line.startswith("Data sugerida") or line.startswith("e-mail")


def get_sections(body):
    """
    Get a dictionary with the issue info

    Returns a dictionary with the issue data. Each key in the dictionary is the
    section prefix and its value is the section content.
    """
    sections = {}
    section = ""
    section_name = ""
    buff = io.StringIO(body)
    line = buff.readline().strip()
    while len(line) > 0:
        if is_first_section_line(line):
            if len(section_name) > 0:
                sections[section_name] = section.rstrip()
            section_name = line[:line.find(":")].strip()
            section = line[line.find(":")+1:].lstrip()
        else:
            section += line
        line = buff.readline()
    if len(section_name) > 0:
        sections[section_name] = section.rstrip()
    return sections


def has_all_required_data(event):
    """
    Check if the issue has all the required fields
    """
    sections = get_sections(event["issue"].get("body", ""))
    return "Descrição" in sections and "Data sugerida" in sections and \
        "e-mail" in sections and "Nome" in sections


def get_issue_number(event):
    """
    Returns the issue number from the event
    """
    return event["issue"]["number"]


def comment(g, event, msg):
    """
    Write a comment in the issue from the event
    """
    repo = g.get_repo(get_repository_name())
    issue = repo.get_issue(get_issue_number(event))
    return issue.create_comment(msg)


def main():
    with open(get_event_file()) as f:
        g = Github(get_access_token())
        event = json.load(f)
        print(json.dumps(event))
        # Verifica se a issue criada possui a label evento
        if not has_event_label(event):
            print("It's not a event issue")
            return
        # Se tem a label, verifica se possui os dados minimos necessarios
        if not has_all_required_data(event):
            # Missing data. Write a comment notifying the user
            comment(g, event, ERROR_COMMENT)
            return
        else:
            # All required data is there.
            comment(g, event, SUCCESS_COMMENT)
            return


if __name__ == "__main__":
    main()
