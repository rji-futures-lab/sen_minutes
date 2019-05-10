import requests
import json

query = """
{
  allBills(
    identifier: "SB%s",
    legislativeSession_Name: "%s Regular Session"
  ) {
    edges {
      node {
        identifier
        title
        description
        billStatusText
        lastActionDescription
        lastActionDate
        absoluteUrl
        updatedAt
      }
    }
  }
}
"""

def get_access_mo_data(bill_no, year):
    """
    Get the extra bill data from Access Missouri.
    """
    url = "https://www.accessmo.org/graphql"

    q = query % (bill_no, year)

    response = requests.post(url, json=dict(query=q))

    bill_data = response.json()['data']['allBills']['edges'][0]['node']

    return bill_data
