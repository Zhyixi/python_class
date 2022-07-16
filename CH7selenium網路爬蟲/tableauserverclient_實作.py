import tableauserverclient as TSC

tableau_auth = TSC.TableauAuth('USERNAME', 'PASSWORD', 'SITENAME')
server = TSC.Server('https://public.tableau.com/app/profile/akilapa.idris5302/viz/SuperStoresRegionalDashboard/SuperStoreRegionalDashboard')
# http://SERVER_URL
#

with server.auth.sign_in(tableau_auth):
    all_datasources, pagination_item = server.datasources.get()
    print("\nThere are {} datasources on site: ".format(pagination_item.total_available))
    print([datasource.name for datasource in all_datasources])
