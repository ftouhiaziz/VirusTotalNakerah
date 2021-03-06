from __future__ import print_function

import argparse
import os
import sys

try:
    import configparser
except ImportError:
    import ConfigParser as configparser

try:
    import simplejson as json
except ImportError:
    import json

import requests
from virus_total_apis import PrivateApi as VTPrivateAPI


def error(*args):
    """
    Prints an error message to stderr and terminates.
    Args:
        args: Variable-length arguments to print in the error message
    """
    print('ERROR:', *args, file=sys.stderr)
    sys.exit(1)


def parse_args():
    """
    Parse the command-line arguments.
    Returns:
        The parsed command-line arguments
    """
    default_conf_file = os.path.join(os.path.expanduser('~'), '.vtapi')

    # Construct the main parser
    parser = argparse.ArgumentParser(description='Interact with the '
                                                 'VirusTotal API.')
    parser.add_argument('-c', '--config', action='store',
                        default=default_conf_file,
                        help='Path to the configuration file')
    subparsers = parser.add_subparsers(dest='command')
    # URL scan subparser
    url_scan_parser = subparsers.add_parser('url-scan',
                                            help='Submit URL(s) to be scanned')
    url_scan_parser.add_argument('url', nargs='+', help='URL(s) (up to 25)')

    # URL report subparser
    url_report_parser = subparsers.add_parser('url-report',
                                              help='Get URL scan results')
    url_report_parser.add_argument('url', nargs='+', help='URL(s) (up to 25)')

    # IP report subparser
    ip_report_parser = subparsers.add_parser('ip-report',
                                             help='Get information about an '
                                                  'IP address')
    ip_report_parser.add_argument('ip', action='store', help='An IPv4 address')

    # Domain report subparser
    domain_report_parser = subparsers.add_parser('domain-report',
                                                 help='Get information about '
                                                      'a domain')
    domain_report_parser.add_argument('domain', action='store',
                                      help='A domain name')

    return parser.parse_args()

def pretty_print_json(json_data, output=sys.stdout):
    """
    Pretty-print JSON data.
    Args:
        json_data: The JSON data to pretty-print
        output: A file-like object (stream) to pretty-print the JSON data to
    """
    print(json.dumps(json_data, sort_keys=True, indent=4), file=output)


def check_num_args(args):
    """
    Checks the number of arguments does not exceed the maximum allowed by the
    VirusTotal private API.
    Args:
        hash_list: A list of arguments
    """
    if len(args) > 25:
        error('The VT Private API only allows a maximum of 25 arguments to '
              'be specified in a single query')

def url_scan(virus_total, url_list):
    """
    Submit a list of URLs to scan.
    Args:
        virus_total: VirusTotal API object
        url_list: A list of URLs to scan
    """
    check_num_args(url_list)
    response = virus_total.scan_url('\n'.join(url_list))
    pretty_print_json(response)


def url_report(virus_total, url_list):
    """
    Retrieves a scan report for a given URL.
    Args:
        virus_total: VirusTotal API object
        hash_list: A list of URLs to retrieve scan reports for
    """
    check_num_args(url_list)
    response = virus_total.get_url_report('\n'.join(url_list))
    pretty_print_json(response)


def ip_report(virus_total, ip_address):
    """
    Retrieves a scan report for a given IP address.
    Args:
        virus_total: VirusTotal API object
        ip_address: IPv4 address
    """
    response = virus_total.get_ip_report(ip_address)
    pretty_print_json(response)


def domain_report(virus_total, domain_name):
    """
    Retrieves a scan report for a given domain name.
    Args:
        virus_total: VirusTotal API object
        domain_name: Domain name
    """
    response = virus_total.get_domain_report(domain_name)
    pretty_print_json(response)


def main():
    """
    The main function.
    """
    args = parse_args()
    api_key ="c876807b8af1baf06e40a583cd2e61a62e99f9b46d3e355128bdb190be271951"
    command = args.command
    virus_total = VTPrivateAPI(api_key)


    if command == 'url-scan':
        url_scan(virus_total, args.url)
    elif command == 'url-report':
        url_report(virus_total, args.url)
    elif command == 'ip-report':
        ip_report(virus_total, args.ip)
    elif command == 'domain-report':
        domain_report(virus_total, args.domain)


if __name__ == '__main__':
    main()
