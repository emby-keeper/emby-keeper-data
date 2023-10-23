from pathlib import Path

patterns = ['{spec}', '{spec}@latest']

if __name__ == '__main__':
    specs = {}
    basedir = Path(__file__).parent.parent
    data = basedir / 'data'
    for f in data.iterdir():
        try:
            spec, version = f.stem.split('@')
        except ValueError:
            continue
        spec_ext = (spec, f.suffix)
        if spec_ext in specs:
            specs[spec_ext].append(version)
        else:
            specs[spec_ext] = [version]
    versionm = basedir / 'version'
    with open(versionm, 'w+') as f:
        for (spec, ext), vs in specs.items():
            latest_version = sorted(vs, reverse=True)[0]
            for p in patterns:
                pattern = p.format(spec=spec)
                f.write(f'{pattern}{ext} = {spec}@{latest_version}{ext}\n')
