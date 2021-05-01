import requests

class MacLookUp:

    def __init__(self, Macaddress=None, auth_key=None):

        '''This __init__will initilize the instance variables Macaddress and auth_key'''

        self.__Macaddress = Macaddress.replace('-',':')
        self.__auth_key = auth_key


    def get_macLookup_data(self):

        '''This get_macLookup_data will call the api and returns the vendordetails'''
        mac_address = self.__Macaddress if self.__Macaddress else "44:38:39:ff:ef:57"

        url = "https://api.macaddress.io/v1?output=json&search={}".format(mac_address)

        headers = {
            'X-Authentication-Token': self.__auth_key if self.__auth_key else 'at_XhxsL4tnfHMV79WR3Nv6MThkhaxA9'
        }
        response = requests.request("GET", url, headers=headers)
        data = response.json()
        return f'CompanyName for this {mac_address} is: {data["vendorDetails"]["companyName"]}'

if __name__ == '__main__':

    #promting user to enter Macaddress( physical address)
    Macaddress = input("Enter Mac Address ( The Format Can Be Either '-' or  ':' It can Accept): ")

    #promting user to enter Authentication Token
    auth_key = input("Enter Authentication Token: ")

    #creating MacLoopUp object by sending Macaddress and auth_key
    obj = MacLookUp(Macaddress, auth_key)

    #Calling get_macLookup_data method to get the VendorDetails of MacAddress
    print(obj.get_macLookup_data())

