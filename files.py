from csv import DictWriter

import requests


insights_api_url =\
    'https://api.access.redhat.com/r/insights/v1/static/uploader.json'
report_file_name = 'scanned_files.csv'


def get_api_response(api_url):
    print(f'Fetching data from {api_url}.')
    api_response = requests.get(insights_api_url)
    return api_response.json()


def write_files_report(api_response, file_name):
    print(f'Writing report to {file_name}.')
    api_files_list = api_response['files']
    with open(file_name, 'w') as outputfile:
        field_names = ['symbolic_name', 'file']
        writer = DictWriter(
            outputfile, fieldnames=field_names, extrasaction='ignore'
        )
        writer.writerow(
            {'symbolic_name': 'Symbolic Name', 'file': 'File Name'}
        )
        writer.writerows(api_files_list)


def main():
    print('Starting reporting.')
    api_response = get_api_response(insights_api_url)
    write_files_report(api_response, report_file_name)
    print('Done.')


if __name__ == '__main__':
    main()