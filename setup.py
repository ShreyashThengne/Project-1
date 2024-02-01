from setuptools import setup, find_packages

def get_requirements(path):
    requ = []
    HYPHEN_E_DOT = '-e .'
    with open(path) as f:
        packages = f.readlines()
        requ = [r.replace('\n', '') for r in packages]

        if HYPHEN_E_DOT in requ:
            requ.remove(HYPHEN_E_DOT)

setup(
    name='project1',
    version = '0.0.1',
    author = 'Shreyash',
    author_email='shreyashthengne@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)