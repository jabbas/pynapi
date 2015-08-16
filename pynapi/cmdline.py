import os
from pynapi import pyNapi
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

# TODO configuration
# TODO logging

MOVIE_EXTENSIONS = (".avi", ".mkv", ".mp4")

def cmdline():
    p = ArgumentParser(
        description="subtitles downloader",
        formatter_class=ArgumentDefaultsHelpFormatter
    )

    p.add_argument('path', metavar='PATH', type=str, nargs="+",
                   help="file (directory containing files) that subtitles will be downloaded for")

    p.add_argument('-l', '--language',  metavar="LANG", default='pl',       help="language of the subtitles")
    p.add_argument('-e', '--encoding',  metavar="ENC",  default='utf-8',    help="encoding of the subtitles")
    p.add_argument('-x', '--extension', metavar="EXT",  default="txt",      help="subtitles filename extension")

    # TODO explicitly select services

    args = p.parse_args()

    napi = pyNapi(
            language = args.language,
            encoding = args.encoding
    )

    file_list = []
    for path in args.path:
        if os.path.isdir(path):
            for root, dirs, files in os.walk(path):
                for filename in files:
                    file_path = os.path.join(root, filename)
                    if file_path.endswith(MOVIE_EXTENSIONS):
                        file_list.append(file_path)
        else:
            if path.endswith(MOVIE_EXTENSIONS):
                file_list.append(path)

    for file_path in file_list:
        subs = napi.get_subs(file_path)
        sub_path = "%s.%s" % (os.path.splitext(file_path)[0], args.extension)

        if subs:
            print "Found subtitles for '%s'" % file_path
            with open(sub_path, 'wb') as sub:
                sub.write(subs)
