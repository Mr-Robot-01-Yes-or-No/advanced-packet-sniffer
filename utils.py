from colorama import Fore


def get_protocol_color(protocol):

    colors = {
        "TCP": Fore.GREEN,
        "UDP": Fore.CYAN,
        "ICMP": Fore.MAGENTA,
        "DNS": Fore.YELLOW,
        "HTTP": Fore.RED,
        "OTHER": Fore.WHITE
    }

    return colors.get(protocol, Fore.WHITE)