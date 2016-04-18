from __future__ import print_function, absolute_import
import os, sys
import argparse
import json
from jinja2 import Environment

def render_template(env, input_file):
    if input_file == '-':
        return env.from_string(sys.stdin.read()).render()
    else:
        with open(input_file, 'r') as tfd:
            return env.from_string(tfd.read()).render()

def build_environment(args):
    extensions = ['jinja2.ext.do',
                  'jinja2.ext.loopcontrols',
                  'jinja2.ext.with_',
                  'jinja2.ext.autoescape']
    env = Environment(extensions=extensions)
    env.filters['jsonify'] = json.dumps
    return env

def main(arguments=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='input_file')
    parser.add_argument('-o', '--output-file',
                        metavar='output_file', help='output file')

    args = parser.parse_args(arguments)
    env = build_environment(args)
    content = render_template(env, args.input_file)

    if args.output_file:
        with open(args.output_file, 'w') as output_fd:
            print(content, file=output_fd)
    else:
        print(content)

if __name__ == '__main__':
    main()
