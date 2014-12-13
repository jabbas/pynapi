import sys, os
from pynapi import pyNapi, list_services
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

# TODO configuration
# TODO logging

def cmdline():
    p = ArgumentParser(
        description="subtitles downloader",
        formatter_class=ArgumentDefaultsHelpFormatter
    )

    p.add_argument('files', metavar='FILE', type=str, nargs="+", help="file that subtitles will be downloaded for")

    p.add_argument('-l', '--language',  metavar="LANG", default='pl',       help="language of the subtitles")
    p.add_argument('-e', '--encoding',  metavar="ENC",  default='utf-8',    help="encoding of the subtitles")
    p.add_argument('-x', '--extension', metavar="EXT",  default="txt",      help="subtitles filename extension")

    # TODO explicitly select services

    args = p.parse_args()

    napi = pyNapi(
            language = args.language,
            encoding = args.encoding
    )

    for path in args.files:
        subs = napi.get_subs(path)
        sub_path = "%s.%s" % (os.path.splitext(path)[0], args.extension)

        with open(sub_path, 'wb') as sub:
            sub.write(subs)



