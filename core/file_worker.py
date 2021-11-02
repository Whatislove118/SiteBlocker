import re




def _search_block_rules(content, pattern=None):
    result = []
    if pattern is None:
        pattern = r'\d{,3}\.\d{,3}\.\d{,3}\.\d{,3}\s[w]{3}\.[A-Za-z]+\.[A-Za-z]+'
    for line in content:
        rule = re.match(pattern, line)
        if rule is not None:
            rule = re.search(r'[w]{3}\.[A-Za-z]+\.[A-Za-z]+', rule.group(0))
            result.append(rule.group(0))
    print('\n'.join(result))


def list_blocked_sites(path, *args):
    with open(path, 'r+') as file:
        content = file.readlines()
        _search_block_rules(content)
        


def add_site_to_block(path, sites, redirect):
    if len(sites) == 0:
        return
    with open(path, 'r+') as file:
        content = file.read()
        for site in sites:
            if site in content:
                pass
            else:
                file.write(redirect + ' ' + site + '\n')


def delete_site_from_block(path, sites, *args):
    if len(sites) == 0:
        return
    with open(path, 'r+') as file:
        content = file.readlines()
        file.seek(0)
        for line in content:
            if not any(site in line for site in sites):
                file.write(line)
            file.truncate()
