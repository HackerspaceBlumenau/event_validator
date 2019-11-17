import json
import os
import io
from github import Github


ERROR_COMMENT = (
    "Olá! Ficamos MUITO felizes em ver seu interesse em "
    "participar da nossa comunidade. Mas eu encontrei alguns "
    "probleminhas. Estão faltando alguns dados. Você pode dar uma "
    "olhadinha novamente? Isso foi o que encontrei:"
)

SUCCESS_COMMENT = (
    "Que demais! Obrigado por ter enviado sua proposta de "
    "evento. Me parece que tudo está certo! Logo logo, alguém "
    "vai entrar em contato para definir o local e data definitivos. :)"
)

MISSING_DESCRIPTION_ERROR = "Está faltando a descrição"
MISSING_DATE_ERROR = "Está faltando a data ou o formato está errado"
MISSING_NAME_ERROR = "Está faltando o nome do palestrante"
MISSING_EMAIL_ERROR = "Está faltando o email de contato"

DESCRIPTION_LABEL = "Descrição"
DATE_LABEL = "Data sugerida"
NAME_LABEL = "Nome"
EMAIL_LABEL = "Email"


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
    return (
        line.startswith(DESCRIPTION_LABEL)
        or line.startswith(NAME_LABEL)
        or line.startswith(DATE_LABEL)
        or line.startswith(EMAIL_LABEL)
    )


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
            section_name = line[: line.find(":")].strip()
            section = line[line.find(":") + 1 :].lstrip()
        else:
            section += line
        line = buff.readline()
    if len(section_name) > 0:
        sections[section_name] = section.rstrip()
    return sections


def validate_data(event):
    """
    Check if the issue has all the required fields
    """
    sections = get_sections(event["issue"].get("body", ""))
    print(sections)
    errors = []
    if DESCRIPTION_LABEL not in sections or (
        DESCRIPTION_LABEL in sections and len(sections.get(DESCRIPTION_LABEL, "")) == 0
    ):
        errors.append(MISSING_DESCRIPTION_ERROR)
    if DATE_LABEL not in sections or (
        DATE_LABEL in sections and len(sections.get(DATE_LABEL, "")) == 0
    ):
        errors.append(MISSING_DATE_ERROR)
    if NAME_LABEL not in sections or (
        NAME_LABEL in sections and len(sections.get(NAME_LABEL, "")) == 0
    ):
        errors.append(MISSING_NAME_ERROR)
    if EMAIL_LABEL not in sections or (
        EMAIL_LABEL in sections and len(sections.get(EMAIL_LABEL, "")) == 0
    ):
        errors.append(MISSING_EMAIL_ERROR)
    return errors


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
        # Verifica se a issue criada possui a label evento
        if not has_event_label(event):
            print("It's not a event issue")
            return
        # Se tem a label, verifica se possui os dados minimos necessarios
        errors = validate_data(event)
        if len(errors) > 0:
            # Missing data. Write a comment notifying the user
            errmsg = "\n".join(errors)
            comment(g, event, f"{ERROR_COMMENT}\n\n{errmsg}")
        else:
            # All required data is there.
            comment(g, event, SUCCESS_COMMENT)


if __name__ == "__main__":
    main()
