

def add_site_to_block(path, site, redirect):
    with open(path, 'r+') as file:
        content = file.read()
        if site in content:
            pass
        else:
            file.write(redirect + ' ' + site + '\n')



def delete_site_from_block(path, site, redirect):
    with open(path, 'r+') as file:
        content = file.readlines()
        file.seek(0)
        for line in content:
            if site not in line:
                file.write(line)
            file.truncate()
