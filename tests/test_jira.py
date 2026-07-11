from app.clients.jira_clients import JiraClient

client = JiraClient()

result = client.get_issue_types("TDSD")

print(result)

# def test_who_am_i():
#     client = JiraClient()
#     result = client.who_am_i()
#     assert "accountId" in result