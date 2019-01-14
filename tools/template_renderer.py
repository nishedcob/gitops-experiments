
import os
import argparse

import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', nargs=1, action='store', help='Path to config.yaml')
    parser.add_argument('-t', '--template', nargs=1, action='store', help='Path to template file')
    output_group = parser.add_argument_group('Output')
    output_group.add_argument('-o', '--output', nargs=1, action='store', help='Path to output file')
    output_group.add_argument('-s', '--stdout', action='store_true', help='Print to Standard Out')
    args = parser.parse_args()

    config_path = args.config[0]

    config = yaml.safe_load(open(config_path).read())

    jinja_env = Environment(
        loader=FileSystemLoader(os.getcwd()),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template_path = args.template[0]

    template = jinja_env.get_template(template_path)

    if args.stdout or args.output is None:
        print(template.render(**config))
    else:
        output_path = args.output[0]
        with open(output_path, 'w') as output_file:
            output_file.write(template.render(**config))
