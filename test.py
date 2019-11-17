import action

# import json
import os
import unittest

TEST_TOKEN = "TEST_TOKEN"
TEST_EVENT_PATH = "/tmp/event-path.json"
TEST_REPO_NAME = "fake/repo"


class TestEventoData(unittest.TestCase):
    def setUp(self):
        os.environ["GITHUB_TOKEN"] = TEST_TOKEN
        os.environ["GITHUB_EVENT_PATH"] = TEST_EVENT_PATH
        os.environ["GITHUB_REPOSITORY"] = TEST_REPO_NAME
        # create a fake event file
        self.issue = {
            "id": 1,
            "node_id": "MDU6SXNzdWUx",
            "url": "https://api.github.com/repos/octocat/Hello-World/issues/\
                    1347",
            "repository_url": "https://api.github.com/repos/octocat/\
                    Hello-World",
            "labels_url": "https://api.github.com/repos/octocat/Hello-World/\
                    issues/1347/labels{/name}",
            "comments_url": "https://api.github.com/repos/octocat/Hello-World/\
                    issues/1347/comments",
            "events_url": "https://api.github.com/repos/octocat/Hello-World/\
                    issues/1347/events",
            "html_url": "https://github.com/octocat/Hello-World/issues/1347",
            "number": 1347,
            "state": "open",
            "title": "Found a bug",
            "body": """Descrição: Evento muito maneiro de python!
                    Data sugerida: 26/10/2019
                    Nome: Fulaninho
                    Email: fulaninho@hs.com""",
            "user": {
                "login": "octocat",
                "id": 1,
                "node_id": "MDQ6VXNlcjE=",
                "avatar_url": "https://github.com/images/error/\
                        octocat_happy.gif",
                "gravatar_id": "",
                "url": "https://api.github.com/users/octocat",
                "html_url": "https://github.com/octocat",
                "followers_url": "https://api.github.com/users/octocat/\
                        followers",
                "following_url": "https://api.github.com/users/octocat/\
                        following{/other_user}",
                "gists_url": "https://api.github.com/users/octocat/\
                        gists{/gist_id}",
                "starred_url": "https://api.github.com/users/octocat/\
                        starred{/owner}{/repo}",
                "subscriptions_url": "https://api.github.com/users/octocat/\
                        subscriptions",
                "organizations_url": "https://api.github.com/users/octocat/\
                        orgs",
                "repos_url": "https://api.github.com/users/octocat/repos",
                "events_url": "https://api.github.com/users/octocat/\
                        events{/privacy}",
                "received_events_url": "https://api.github.com/users/\
                        octocat/received_events",
                "type": "User",
                "site_admin": False,
            },
            "labels": [
                {
                    "id": 208045946,
                    "node_id": "MDU6TGFiZWwyMDgwNDU5NDY=",
                    "url": "https://api.github.com/repos/octocat/Hello-World/\
                            labels/bug",
                    "name": "evento",
                    "description": "Something isn't working",
                    "color": "f29513",
                    "default": True,
                }
            ],
            "assignee": {
                "login": "octocat",
                "id": 1,
                "node_id": "MDQ6VXNlcjE=",
                "avatar_url": "https://github.com/images/error/\
                        octocat_happy.gif",
                "gravatar_id": "",
                "url": "https://api.github.com/users/octocat",
                "html_url": "https://github.com/octocat",
                "followers_url": "https://api.github.com/users/octocat/\
                        followers",
                "following_url": "https://api.github.com/users/octocat/\
                        following{/other_user}",
                "gists_url": "https://api.github.com/users/octocat/\
                        gists{/gist_id}",
                "starred_url": "https://api.github.com/users/octocat/\
                        starred{/owner}{/repo}",
                "subscriptions_url": "https://api.github.com/users/\
                        octocat/subscriptions",
                "organizations_url": "https://api.github.com/users/\
                        octocat/orgs",
                "repos_url": "https://api.github.com/users/octocat/repos",
                "events_url": "https://api.github.com/users/octocat/\
                        events{/privacy}",
                "received_events_url": "https://api.github.com/users/\
                        octocat/received_events",
                "type": "User",
                "site_admin": False,
            },
            "assignees": [
                {
                    "login": "octocat",
                    "id": 1,
                    "node_id": "MDQ6VXNlcjE=",
                    "avatar_url": "https://github.com/images/error/\
                                octocat_happy.gif",
                    "gravatar_id": "",
                    "url": "https://api.github.com/users/octocat",
                    "html_url": "https://github.com/octocat",
                    "followers_url": "https://api.github.com/users/\
                                octocat/followers",
                    "following_url": "https://api.github.com/users/\
                                octocat/following{/other_user}",
                    "gists_url": "https://api.github.com/users/octocat/\
                                gists{/gist_id}",
                    "starred_url": "https://api.github.com/users/octocat/\
                                starred{/owner}{/repo}",
                    "subscriptions_url": "https://api.github.com/users/\
                                octocat/subscriptions",
                    "organizations_url": "https://api.github.com/users/\
                                octocat/orgs",
                    "repos_url": "https://api.github.com/users/octocat/\
                                repos",
                    "events_url": "https://api.github.com/users/octocat/\
                                events{/privacy}",
                    "received_events_url": "https://api.github.com/users/\
                                octocat/received_events",
                    "type": "User",
                    "site_admin": False,
                }
            ],
            "milestone": {
                "url": "https://api.github.com/repos/octocat/Hello-World/\
                            milestones/1",
                "html_url": "https://github.com/octocat/Hello-World/\
                            milestones/v1.0",
                "labels_url": "https://api.github.com/repos/octocat/\
                            Hello-World/milestones/1/labels",
                "id": 1002604,
                "node_id": "MDk6TWlsZXN0b25lMTAwMjYwNA==",
                "number": 1,
                "state": "open",
                "title": "v1.0",
                "description": "Tracking milestone for version 1.0",
                "creator": {
                    "login": "octocat",
                    "id": 1,
                    "node_id": "MDQ6VXNlcjE=",
                    "avatar_url": "https://github.com/images/error/\
                                octocat_happy.gif",
                    "gravatar_id": "",
                    "url": "https://api.github.com/users/octocat",
                    "html_url": "https://github.com/octocat",
                    "followers_url": "https://api.github.com/users/\
                                octocat/followers",
                    "following_url": "https://api.github.com/users/\
                                octocat/following{/other_user}",
                    "gists_url": "https://api.github.com/users/octocat/\
                                gists{/gist_id}",
                    "starred_url": "https://api.github.com/users/octocat/\
                                starred{/owner}{/repo}",
                    "subscriptions_url": "https://api.github.com/users/\
                                octocat/subscriptions",
                    "organizations_url": "https://api.github.com/users/\
                                octocat/orgs",
                    "repos_url": "https://api.github.com/users/\
                                octocat/repos",
                    "events_url": "https://api.github.com/users/octocat/\
                                events{/privacy}",
                    "received_events_url": "https://api.github.com/users/\
                                octocat/received_events",
                    "type": "User",
                    "site_admin": False,
                },
                "open_issues": 4,
                "closed_issues": 8,
                "created_at": "2011-04-10T20:09:31Z",
                "updated_at": "2014-03-03T18:58:10Z",
                "closed_at": "2013-02-12T13:22:01Z",
                "due_on": "2012-10-09T23:39:01Z",
            },
            "locked": True,
            "active_lock_reason": "too heated",
            "comments": 0,
            "pull_request": {
                "url": "https://api.github.com/repos/octocat/Hello-World/\
                        pulls/1347",
                "html_url": "https://github.com/octocat/Hello-World/pull/1347",
                "diff_url": "https://github.com/octocat/Hello-World/pull/\
                        1347.diff",
                "patch_url": "https://github.com/octocat/Hello-World/pull/\
                        1347.patch",
            },
            "closed_at": None,
            "created_at": "2011-04-22T13:33:48Z",
            "updated_at": "2011-04-22T13:33:48Z",
            "closed_by": {
                "login": "octocat",
                "id": 1,
                "node_id": "MDQ6VXNlcjE=",
                "avatar_url": "https://github.com/images/error/\
                        octocat_happy.gif",
                "gravatar_id": "",
                "url": "https://api.github.com/users/octocat",
                "html_url": "https://github.com/octocat",
                "followers_url": "https://api.github.com/users/octocat/\
                        followers",
                "following_url": "https://api.github.com/users/octocat/\
                        following{/other_user}",
                "gists_url": "https://api.github.com/users/octocat/\
                        gists{/gist_id}",
                "starred_url": "https://api.github.com/users/octocat/\
                        starred{/owner}{/repo}",
                "subscriptions_url": "https://api.github.com/users/octocat/\
                        subscriptions",
                "organizations_url": "https://api.github.com/users/octocat/\
                        orgs",
                "repos_url": "https://api.github.com/users/octocat/repos",
                "events_url": "https://api.github.com/users/octocat/\
                        events{/privacy}",
                "received_events_url": "https://api.github.com/users/octocat/\
e                       received_events",
                "type": "User",
                "site_admin": False,
            },
        }
        self.event = {"issue": self.issue}

    def test_get_token(self):
        self.assertEqual(action.get_access_token(), TEST_TOKEN)

    def test_get_event_file(self):
        self.assertEqual(action.get_event_file(), TEST_EVENT_PATH)

    def test_is_first_section_line(self):
        self.assertTrue(
            action.is_first_section_line(
                "Descrição: Evento \
                muito maneiro de python!"
            )
        )
        self.assertTrue(action.is_first_section_line("Nome: Python Brasil"))
        self.assertTrue(
            action.is_first_section_line(
                "Data sugerida: \
                26/10/2019"
            )
        )
        self.assertTrue(
            action.is_first_section_line(
                "Email: \
                fulaninho@hs.com"
            )
        )

        self.assertFalse(
            action.is_first_section_line(
                "email: \
            fulaninho@hs.com"
            )
        )
        self.assertFalse(
            action.is_first_section_line(
                "Descricao: Evento \
                muito maneiro de python!"
            )
        )
        self.assertFalse(action.is_first_section_line("Name: Python Brasil"))
        self.assertFalse(action.is_first_section_line("Data: 26/10/2019"))

    def test_has_event_label(self):
        self.assertTrue(action.has_event_label(self.event))

    def test_has_all_required_data(self):
        self.assertEqual(0, len(action.validate_data(self.event)))

    def test_get_sections(self):
        sections = action.get_sections(self.issue["body"])
        self.assertEqual(len(sections), 4)
        self.assertIn("Descrição", sections, msg="Missing 'descrição'")
        self.assertEqual(sections["Descrição"], "Evento muito maneiro de python!")
        self.assertIn("Nome", sections, msg="Missing 'Nome'")
        self.assertEqual(sections["Nome"], "Fulaninho")
        self.assertIn("Email", sections, msg="Missing 'Email'")
        self.assertEqual(sections["Email"], "fulaninho@hs.com")
        self.assertIn("Data sugerida", sections, msg="Missing 'Data sugerida'")
        self.assertEqual(sections["Data sugerida"], "26/10/2019")

    def tet_get_repository_name(self):
        self.assertEqual(action.get_repository_name(), TEST_REPO_NAME)

    def test_get_issue_number(self):
        self.assertEqual(action.get_issue_number(self.event), 1347)


if __name__ == "__main__":
    unittest.main()
