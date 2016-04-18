from setuptools import setup,find_packages

setup(
    name = "jinjacli",
    version = "0.1",
    packages = ['jinjacli'],
    author = "Nicolas Limage",
    author_email = 'github@xephon.org',
    description = "jinja command-line interface",
    license = "GPL",
    keywords = "jinja template command-line",
    url = "https://github.com/nlm/jinjacli",
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    install_requires = [
        'Jinja2',
    ],
    entry_points = {
        'console_scripts': [
            'jinja = jinjacli.__main__:main',
        ],
    },
)
