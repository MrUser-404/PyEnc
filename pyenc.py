import os,time,base64
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import subprocess,sys
b64 = lambda in_ : base64.b64encode(in_)
try:
	import cython
except ImportError:
	os.system("clear")
	print(f"\033[1;33m[\033[1;91m-\033[1;33m] \033[1;92mInstalling required module ...\033[0m")
	print()
	os.system("pip install cython==0.29.37 -q")
R='\033[1;91m'
RO='\033[1;41m'
V='\033[1;92m'
J='\033[1;33m'
B='\033[1;97m'
O='\033[38;5;208m'
G='\033[38;5;240m'
Ro='\033[38;5;204m'
S='\033[0m'
C='\033[36m'
v='\033[7;92m'
r='\033[7;91m'
c='\033[7;96m'
j='\033[7;33m'
logo=f'''
██████  ██    ██ ███████ ███    ██  ██████     
██   ██  ██  ██  ██      ████   ██ ██          
██████    ████   █████   ██ ██  ██ ██          
██         ██    ██      ██  ██ ██ ██          
██         ██    ███████ ██   ████  ██████     
'''
choice=[]
def banner():
	os.system("clear")
	print(logo)
	console=Console()
	width=40
	height=6
	text=f'''\
	[+]Tool Name: PyEnc
	[+]Tool Version: 1.0
	[+]Country: Madagascar
	[+]Coded by: MrUser-404'''
	formate_text=Text(text)
	rectangle=Panel(
	formate_text,
	width=width,
	height=height,
	border_style="bold white")
	console.print(rectangle)

def Encode(data,out,path):
	loop=2
	enc="b64(data.encode('utf8'))[::-1]"
	header="_ = lambda __ : __import__('base64').b64decode(__[::-1]);"
	note=(f'''#Tool encrypted by MrUser''')
	for x in range(loop):
		data = "exec((_)(%s))" % repr(eval(enc))
	encoded=(f"{note}\n{header}{data}")
	open(out,'w').write(encoded)
	print()
	word=(f"{R}[{B}-{R}] {J}Wait tool processing ...{S}")
	for wordx in word:
		print(wordx,end='',flush=True)
		time.sleep(0.04)
	try:
		with open(os.devnull,'w') as fnull:
			result=subprocess.run([sys.executable,'-m',"Cython.Build.BuildExecutable",out],stdout=fnull,stderr=fnull)
	finally:
		out1=out.split(".")[0]
		path1=path.split(".py")[0]
		os.system("chmod +x encode")
		os.system(f"mv encode {path1}_pyenc")
		os.system(f"rm -rf {out1}.o && {out1}.c")
		os.system("rm -rf encoded.py")
		os.system("rm -rf")
def main():
	banner()
	print()
	print(f"{B}[{V}1{B}]Start{S}")
	print(f"{B}[{V}2{B}]Follow my github{S}")
	print(f"{B}[{V}3{B}]Follow my Fb page{S}")
	print(f"{B}[0]Exit Tool{S}")
	print()
	sel=input(f"{B}[{R}?{B}]Choose: ")
	if str(sel)=="1":
		main1()
	elif str(sel)=="2":
		print()
		os.system("xdg-open https://github.com/MrUser-404")
		time.sleep(2)
		main()
	elif str(sel)=="3":
		print()
		os.system("xdg-open https://www.facebook.com/MrUser.505")
		time.sleep(2)
		main()
	elif str(sel)=="0":
		os.system("clear")
		print(f"{c}Thanks for using this tool{S}")
		exit()
	else:
		os.system("clear")
		print(f"{r}Wrong Input,please try again{S}")
		time.sleep(2)
		main()
		
def main1():
	global choice
	choice=[]
	banner()
	print()
	path=input(f"{B}[{V}+{B}]File path: ")
	try:
		data=open(path).read()
	except IOError:
		os.system("clear")
		print(f"{r}File Not Found{S}")
		time.sleep(2)
		main1()
	out=("encoded.py")
	Encode(data,out,path)
main()	