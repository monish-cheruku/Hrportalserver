#windowsAD ip
from ldap3 import Connection,SUBTREE
from decouple import config


def ManageADUsers():
    try:
        from ManageAdUsers.models import AdUsers
        from ManageAdUsers.serializers import AdUsersSerializer
        from django.contrib.auth.models import User, Group
        dbarr=AdUsersSerializer(AdUsers.objects.all(),many=True).data

        adusersarr=[]
        aduserssamacnames=[]
        con=Connection(config("LDAPIP"),"scheruku@belcan.com",password="Belcan#12345",auto_bind=True)
        print(con.result['description'])
        total_entries = 0
        con.search(search_base = 'OU=India,DC=belcan,DC=com',
        search_scope = SUBTREE,
        search_filter = '(memberOf=CN=Belcan India,OU=Security Groups,OU=India,DC=belcan,DC=com)',
        # search_filter = '(objectClass=user)',
            attributes = ['sAMAccountName','cn','givenName','sn','mail','employeeNumber','distinguishedName'])
        total_entries += len(con.response)
        print(total_entries)
        for entry in con.response:
            # print(entry['dn'], entry['attributes'])
            adusersarr.append( entry['attributes'])
            aduserssamacnames.append( entry['attributes']['sAMAccountName'])

        print(adusersarr)

        for i in adusersarr:
            print(i)
            aduser=AdUsers.objects.filter(UserName=i['sAMAccountName']).first()
            if aduser is  None:
                temp= i
                #create new row code
                user_serializer = AdUsersSerializer(data={"UserName":temp["sAMAccountName"],"FirstName":temp["givenName"],"LastName":temp["sn"],  "Email":temp["mail"] , "Active":True  })
                if user_serializer.is_valid():
                    user_serializer.save()
        
        results =AdUsers.objects.exclude(UserName__in=aduserssamacnames)
        print(results)
        for i in results:
            AdUsers.objects.filter(UserName=i.UserName).update(Active=False)
            User.objects.filter(username=i.UserName).update(is_active=False)

        print("running a job with scheduler//////////////")


    except Exception as e:
        print("Aduser sync Schedular failed "+e  )