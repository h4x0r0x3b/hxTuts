# \033 \x1b \u001b are Escape Characters
RED='\033[31m' # \x1b[31m or \u001b[31m
BLUE='\033[34m'
WHITE='\033[37m'
YELLOW='\033[33m'
msg = f"""
{WHITE} ████{YELLOW}██{WHITE}╗██{BLUE}╗   ██╗██████╗ ███████╗██████╗ P
{WHITE}██╔════╝╚██╗ {BLUE}██╔╝██╔══██╗██╔════╝██╔══██╗H
{WHITE}██║      ╚████╔╝ {BLUE}██████╔╝█████╗  ██████╔╝I
{WHITE}██║       ╚{YELLOW}██{WHITE}╔╝  ██╔══{BLUE}██╗██╔══╝  ██╔══██╗L
{WHITE}╚████{YELLOW}██╗   ██║   █{WHITE}█████╔╝{BLUE}███████╗██║  ██║I
{WHITE} ╚════{YELLOW}═╝   ╚═╝   ╚═{WHITE}═══{YELLOW}═╝ ╚{WHITE}══{BLUE}════╝╚═╝  ╚═╝P
{WHITE} ███╗   {YELLOW}██╗██╗███{WHITE}╗   █{YELLOW}█╗{WHITE}     {RED}██╗ █████╗  P
{WHITE} ████╗  {YELLOW}██║██║██{WHITE}██╗  ██{RED}║     ██║██╔══██╗ I
{WHITE} ██╔██╗ ██║{YELLOW}██║{WHITE}██╔██╗ {RED}██║     ██║███████║ N
{WHITE} ██║╚██╗██║██║██║{RED}╚██╗██║██   ██║██╔══██║ E
{WHITE} ██║ ╚{YELLOW}██{WHITE}██║██║{RED}██║ ╚████║╚█████╔╝██║  ██║ S
{WHITE} ╚═╝  ╚═══╝{RED}╚═╝╚═╝  ╚═══╝ ╚════╝ ╚═╝  ╚═╝ ™"""
print(msg)