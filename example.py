import pprint
import tokens
import json
import simple_citeline as sc

citeuser = tokens.citeuser
citepass = tokens.citepass
citeauth = tokens.citeauth

#Example Connection
citeconn = sc.citeline_connection(citeuser,citepass,citeauth)


#Example of citeline get_permissions
#response = sc.query_api.citeline_get_permissions(citeconn)

#Example of citeline schema
#change out the string "drugcatlyst" for one of the schemas present in get_permissions
#response = sc.query_api.citeline_schema("drugcatalyst",citeconn)

#Example of a feed
response = sc.query_api.citeline_feed("trial",citeconn)

pp = pprint.PrettyPrinter(indent=0,depth=3)
#pp.pprint(response)