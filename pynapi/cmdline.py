import os, sys
from pynapi import pyNapi, __version__
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

# TODO configuration in separate file
# TODO logging

MOVIE_EXTENSIONS = (".avi", ".mkv", ".mp4")

def cmdline():
    p = ArgumentParser(
        description="subtitles downloader",
        formatter_class=ArgumentDefaultsHelpFormatter
    )

    p.add_argument('path', metavar='PATH', type=str, nargs="+",
                   help="file (directory containing files) that subtitles will be downloaded for")

    p.add_argument('-l', '--language', metavar="LANG", default='pl',
                    help="language of the subtitles")
    p.add_argument('-e', '--encoding',  metavar="ENC", default='utf-8',
                    help="encoding of the subtitles")
    p.add_argument('-x', '--extension', metavar="EXT", default="txt",
                    help="subtitles filename extension")

    g = p.add_argument_group('additional commands')

    g.add_argument('-f', '--force', action="store_true",
                    help="force download subtitles even if they already exist")
    g.add_argument('-d', '--debug', action="store_true",
                    help="debug mode")

    g.add_argument('-v', '--version', action="version", version='%%(prog)s (version %s)' % __version__)

    # TODO explicitly select services

    args = p.parse_args()

    try:
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
            sub_path = "%s.%s" % (os.path.splitext(file_path)[0], args.extension)
            if os.path.exists(sub_path) and not args.force:
                continue
            subs = napi.get_subs(file_path)

            if subs:
                print "Found subtitles for '%s'" % file_path
                with open(sub_path, 'wb') as sub:
                    sub.write(subs)
    except Exception as e:
        if args.debug:
            raise e
        else:
            print e.message
            sys.exit(1)
