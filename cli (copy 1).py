import argparse

from core.xss import list_xss, get_xss_by_id
from core.sqli import list_sqli, get_sqli_by_id
from core.rce import list_rce, get_rce_by_id
from core.lfi import list_lfi, get_lfi_by_id
from core.ssti import list_ssti, get_ssti_by_id
from core.open_redirect import list_redirect, get_redirect_by_id
from core.csrf import list_csrf, get_csrf_by_id
from core.upload_bypass import list_upload, get_upload_by_id

from generators.generator_rce import RCEGenerator
from generators.generator_lfi import LFIGenerator
from generators.generator_ssti import SSTIGenerator
from generators.generator_open_redirect import RedirectGenerator
from generators.generator_csrf import CSRFGenerator
from generators.generator_upload_bypass import UploadBypassGenerator

parser = argparse.ArgumentParser()
parser.add_argument("action", choices=["list", "generate"])
parser.add_argument("--type")
parser.add_argument("--id")
args = parser.parse_args()

def list_payloads(ptype):
    mapping = {
        "xss": list_xss,
        "sqli": list_sqli,
        "rce": list_rce,
        "lfi": list_lfi,
        "ssti": list_ssti,
        "redirect": list_redirect,
        "csrf": list_csrf,
        "upload": list_upload,
    }
    if ptype not in mapping:
        print("Unknown type")
        return

    for p in mapping[ptype]():
        print(f"{p['id']} - {p['title']}")

def generate_by_id(pid):
    mapping = {
        "SAFE-RCE": (get_rce_by_id, RCEGenerator),
        "SAFE-LFI": (get_lfi_by_id, LFIGenerator),
    }

    for getter, gen in [
        (get_xss_by_id, None),
        (get_sqli_by_id, None),
        (get_rce_by_id, RCEGenerator),
        (get_lfi_by_id, LFIGenerator),
        (get_ssti_by_id, SSTIGenerator),
        (get_redirect_by_id, RedirectGenerator),
        (get_csrf_by_id, CSRFGenerator),
        (get_upload_by_id, UploadBypassGenerator),
    ]:
        p = getter(pid)
        if p:
            if gen:
                print(gen(p["payload"]).generate())
            else:
                print(p["payload"])
            return
    print("Payload ID not found.")

if args.action == "list":
    list_payloads(args.type)

elif args.action == "generate":
    if args.id:
        generate_by_id(args.id)
