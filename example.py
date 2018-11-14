import pprint
import tokens
import simple_citeline as sc

citeuser = tokens.citeuser
citepass = tokens.citepass
citeauth = tokens.citeauth

#Example Connection
citeconn = sc.citelineConnection(citeuser,citepass,citeauth)

#
# Example of citeline get_permissions
# response = sc.queryApi.citelineGetPermissions(citeconn)

# Example of citeline schema
# change out the string "drugcatlyst" for one of the schemas present in get_permissions
# response = sc.queryApi.citelineSchema("trial", citeconn)
#
# Example of a feed
# response = sc.queryApi.citelineFeed("trial", citeconn)
#
# Example of pagination
# response = sc.queryApi.citelineFeed("trial", citeconn)
# next_page = response['pagination']['nextPage']
# response = sc.queryApi.citelineFeed("trial", citeconn, has_page=next_page)
#
# Example of a search
# search_term = {
#     "protocolid": "CTR20150050"
# }
# response = sc.queryApi.citelineSearch("trial", search_term, citeconn)

response = sc.queryApi.citelineList("trial",'sponsorName',citeconn)

pp = pprint.PrettyPrinter(indent=0)
pp.pprint(response)