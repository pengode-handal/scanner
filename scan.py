import argparse
import sys
import os
from os import system as sistem
import time 
from time import sleep as jeda
from requests import get as ambil
from sys import exit as keluar
import requests



#100% BUATAN BABWA BENERAN BWA GA RECODE:v BIKIN INI TU 3 HARI
def main():
  
  def iniweb(url):
    minta = ambil(url)
    respon = minta.text
    print(respon)
  
  cli = argparse.ArgumentParser()
  cli.add_argument("-ms", "--masscan", help="domainya bwa")
  cli.add_argument("-n", "--nmap", help="nmap tools, masukin webnya")
  cli.add_argument("-w", "--whois", help="whois tools, masukin webnya")
  cli.add_argument("-d", "--dns", help="tools dns lookup")
  cli.add_argument("-rd", "--rdns", help="reversee dns tools")
  cli.add_argument("-wz", "--wizard", help="buat yang otaknya dangkal ga paham ama CLI:v canda bwa")
  cli.add_argument("-V", "--Version", action="version", version="Scanner tools Ver 1.0.2")
  cli.add_argument("-g", "--geo", help="Geo Ip Lookup Tools")
  cli.add_argument("-s", "--subfind", help="SubDomain Finder Tools")
  cli.add_argument("-np", "--nping", help="Ping Testing Tools")
  cli.add_argument("-sn", "--subnet", help="SubNetCalc Scanner Tools")
  cli.add_argument("--author", action="version", version="""100% BUATAN BABWA, NO COPYRIGHT, Autor: Babwa/Gura-Chan \n 
, Team: MCA, SCT""")
  clianu = cli.parse_args()
  if clianu.nmap:
    print(""""
#############################################
N M A P  S C A N N E R
#############################################
""")
    web = clianu.nmap
    url = "https://api.hackertarget.com/nmap/?q=" + web 
    iniweb(url)
    keluar("")
  if clianu.whois:
    print(""""
#############################################
W H O I S  S C A N N E R
#############################################
""")
    web = clianu.whois
    url = "https://api.hackertarget.com/whois/?q=" + web
    iniweb(url)
    keluar("")
  if clianu.dns:
    print(""""
############################################
D N S  L O O K U P  S C A N N E R
############################################
""")
    web = clianu.dns 
    url = "https://api.hackertarget.com/dnslookup/?q=" + web 
    iniweb(url)
    keluar("")
  if clianu.rdns:
    print(""""
###########################################
R E V E R S E D  D N S  S C A N N E R
###########################################
""")
    web = clianu.rdns
    url = "https://api.hackertarget.com/reversedns/?q=" + web
    iniweb(url)
    keluar("")
  if clianu.geo:
    print("""
###########################################
G E O  I P  L O O K U P  S C A N N E R
###########################################
 """)
    web = clianu.geo
    url = "https://api.hackertarget.com/geoip/?q=" + web
    iniweb(url)
    keluar("")
  if clianu.subfind:
    print("""
###########################################
F I N D  D N S  H O S T
###########################################
""")
    web = clianu.subfind
    url = "https://api.hackertarget.com/hostsearch/?q=" + web
    iniweb(url)
    keluar("")
  if clianu.nping:
    print("""
###########################################
N P I N G  S C A N N E R 
###########################################
""")
    web = clianu.nping
    url = "https://api.hackertarget.com/nping/?q=" + web
    iniweb(url)
    keluar("")
  if clianu.subnet:
    print(""""
#############################################
S U B N E T  S C A N N E R
#############################################
""")
    web = clianu.subnet
    url = "https://api.hackertarget.com/subnetcalc/?q=" + web 
    iniweb(url)
    keluar("")
  if clianu.wizard:
     wrz = clianu.wizard
     print("""pilih yang mana:\n1. Nmap Scanner\n2. whois lookup\n3. DNS lookup\n4. Reversed DNS\n5. Geo IP Lookup\n6. Find Host DNS\n7. NPING Scanner\n8. SubNet Scanner\n9. All Scan\n10. Version\n11. Exit""")
     nmr = (str(input("\npilih mana >  ")))
     if (nmr == "1"):
       print(""""
###########################################
N M A P  S C A N N E R
###########################################
""")
       print("mulai scanning domain: " + wrz)
       url = "https://api.hackertarget.com/nmap/?q=" + wrz
       iniweb(url)
       keluar("")
     if (nmr == "2"):
       print(""""
###########################################
W H O I S  S C A N N E R
###########################################
""")   
       print("memulai scanning domain: " + wrz)
       url = "https://api.hackertarget.com/whois/?q=" + wrz
       iniweb(url)
       keluar("")
     if (nmr == "3"):
       print(""""
############################################
D N S  L O O K U P  S C A N N E R
############################################
""")
       print("memulai scanning domain: " + wrz)
       url = "https://api.hackertarget.com/dnslookup/?q=" + wrz
       iniweb(url)
       keluar("")
     if (nmr == "4"):
       print(""""
###########################################
R E V E R S E D  D N S  S C A N N E R
###########################################
""")
       print("memulai scanning domain: " + wrz)
       url = "https://api.hackertarget.com/reversedns/?q=" + wrz
       iniweb(url)
       keluar("")
     if (nmr == "5"):
       print("""
###########################################
G E O  I P  L O O K U P  S C A N N E R
###########################################
 """)
       print("memulai Geo IP Lookup pada Domain: " + wrz)
       url = "https://api.hackertarget.com/geoip/?q=" + wrz
       iniweb(url)
       keluar("")
     if (nmr == "6"):
       print("""
###########################################
F I N D  D N S  H O S T
###########################################
""")      
       print("memulai DNS Host Finder pada Domain: " + wrz)
       url = "https://api.hackertarget.com/hostsearch/?q=" + wrz
       iniweb(url)
       keluar("")
     if (nmr == "7"):
       print("""
###########################################
N P I N G  S C A N N E R 
###########################################
""")
       print("memulai NPING Scanner" )
       url = "https://api.hackertarget.com/nping/?q=" + wrz
       iniweb(url)
       keluar("")
     if (nmr == "8"):
       print(""""
#############################################
S U B N E T  S C A N N E R
#############################################
""")
       print("memulai Subnet Scanner")
       url = "https://api.hackertarget.com/subnetcalc/?q=" + wrz
       iniweb(url)
       keluar("")
     if (nmr == "9"):
       print("\n\nmemulai scan nmap\n")
       nm4p = "https://api.hackertarget.com/nmap/?q=" + wrz
       iniweb(nm4p)
       print("\n\nmemulai scan whois\n")
       wh0is = "https://api.hackertarget.com/whois/?q=" + wrz
       iniweb(wh0is)
       print("\n\nmemulai DNS lookup scanner\n")
       DnS = "https://api.hackertarget.com/dnslookup/?q=" + wrz
       iniweb(DnS)
       print("\n\nmemulai Reversed DNS scanner\n")
       RdNs = "https://api.hackertarget.com/reversedns/?q=" + wrz
       iniweb(RdNs)
       print("\n\nmemulai Geo IP Lookup pada Domain: " + wrz + "\n")
       Ge0 = "https://api.hackertarget.com/geoip/?q=" + wrz
       iniweb(Ge0)
       print("\n\nmemulai DNS Host Finder pada Domain: " + wrz + "\n")
       DfD = "https://api.hackertarget.com/hostsearch/?q=" + wrz
       iniweb(DfD)
       print("\n\nmemulai NPING Scanner " + "\n")
       nP1ng = "https://api.hackertarget.com/nping/?q=" + wrz
       iniweb(nP1ng)
       print("\n\nmemulai Subnet Scanner" + "\n")
       Su3 = "https://api.hackertarget.com/subnetcalc/?q=" + wrz
       iniweb(Su3)
       keluar("")
     if (nmr == "10"):
       clianu.Version
       keluar("")
     if (nmr == "11"):
       keluar("\nBye Bwaaa")
     else:
       print("Daftar Tidak Ada")
       keluar("")

  if clianu.masscan:
    print("\n\nini nmap" + "\n")
    sasaran = clianu.masscan
    Nm4p = "https://api.hackertarget.com/nmap/?q=" + sasaran
    iniweb(Nm4p)
    print("\n\ninisub look" + "\n")
    sBn = "https://api.hackertarget.com/subnetcalc/?q=" + sasaran
    iniweb(sBn)
    print("\n\nini DNS lookup" + "\n")
    dlU = "https://api.hackertarget.com/dnslookup/?q=" + sasaran
    iniweb(dlU)
    print("\n\nini Reversed DNS " + "\n")
    rD = "https://api.hackertarget.com/reversedns/?q=" + sasaran 
    iniweb(rD)
    print("\n\nini GEO IP Lookup" + "\n")
    Ge0 = "https://api.hackertarget.com/geoip/?q=" + sasaran
    iniweb(Ge0)
    print("\n\nini DNS Host Finder" + "\n")
    DfD = "https://api.hackertarget.com/hostsearch/?q=" + sasaran
    iniweb(DfD)
    print("\n\nini NPING Scanner " + "\n")
    nP1ng = "https://api.hackertarget.com/nping/?q=" + sasaran
    iniweb(nP1ng)
    keluar("")
if __name__ == '__main__':
  main()

print(" ini CLI bkn gitu pakenya, contoh pake tu: python3 scan.py [...OPTION...] [DOMAIN(No http/https)]")
print("""
usage: scan.py [-h] [-ms MASSCAN] [-n NMAP] [-w WHOIS] [-d DNS] [-rd RDNS] [-wz WIZARD] [-V] [-g GEO] [-s SUBFIND] [-np NPING] [-sn SUBNET]

optional arguments:
  -h, --help            show this help message and exit

  -ms domain            Mass Scanner
                        
  -n domain             nmap tools

  -w domain             whois tools
                       
  -d Domain             tools dns lookup

  -rd domain            reversee dns tools
                        
  -wz domain            buat yang otaknya dangkal ga paham ama CLI:v canda bwa
                        
  -V, --Version         show program's version number and exit

  -g domain             Geo Ip Lookup Tools

  -s domain             SubDomain Finder Tools
     
  -np domain            Ping Testing Tools

  -sn domain            SubNetCalc Scanner Tools
""")
