
import requests

def domain_scanner(domain_name,sub_domains):
      print("----Scanner Started----")
      print('---URL after scanning subdomains--')

      for subdomain in sub_domains:

         url = f"https://{subdomain}.{domain_name}"

         try:

            requests.get(url)
            print(f'[+] {url}') 
          
         except requests.ConnectionError:
                pass

if __name__ == '__main__':

  dom_name = input("Enter the Domain Name:")

##SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
## to avoid error we use duoble backslash
  with open("C:\\Users\\Sarvesh\\.vscode\\projectx\\network\\domain.text","r") as f:
  
     name = f.read()
     sub_dom = name.splitlines()


     ##print(f"Number of domain names inthe list are :{len(sub_dom)}\n")
     ##print("List of subdomain names present in the files\n")
     ##print(sub_dom)
   
  domain_scanner(dom_name,sub_dom)