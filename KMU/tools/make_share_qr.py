"""Create a QR for the actual public repository. Not required by the notebook."""
from pathlib import Path
from urllib.parse import urlparse
import argparse, json, re

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--repo-url',required=True,help='Actual https://github.com/OWNER/REPOSITORY URL')
parser.add_argument('--folder',default='',help='Optional school folder on main, for example KMU')
args=parser.parse_args()
url=args.repo_url.rstrip('/')
parsed=urlparse(url)
parts=[part for part in parsed.path.split('/') if part]
if parsed.scheme!='https' or parsed.netloc!='github.com' or len(parts)!=2 or parsed.query or parsed.fragment:
    parser.error('Use the actual https://github.com/OWNER/REPOSITORY URL, without a query or fragment.')
if args.folder and not re.fullmatch(r'[A-Za-z0-9_-]+',args.folder):
    parser.error('Use a single school folder name, for example KMU.')
target=url+'/tree/main/'+args.folder if args.folder else url
try:
    import qrcode
    import qrcode.image.svg
except ImportError as exc:
    raise SystemExit('First install the sharing-only dependency: python -m pip install "qrcode[pil]>=8,<9"') from exc

out=Path(__file__).resolve().parents[1]/'share'
out.mkdir(exist_ok=True)
qr=qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M,box_size=12,border=4)
qr.add_data(target);qr.make(fit=True)
qr.make_image(fill_color='black',back_color='white').save(out/'github_qr.png')
qr.make_image(image_factory=qrcode.image.svg.SvgPathImage).save(out/'github_qr.svg')
(out/'links.json').write_text(json.dumps({'repository':url,'demo':target,'hub':'https://hub.quandela.com/',
    'web_ide':'https://cloud.quandela.com/webide'},indent=2)+'\n',encoding='utf8')
print('QR target:',target)
print('Saved PNG, SVG and links.json to',out)
