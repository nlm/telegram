from setuptools import setup,find_packages

setup(
    name = "pushover",
    version = "0.2",
    packages = ['pushover'],
    author = "Nicolas Limage",
    author_email = 'github@xephon.org',
    description = "simple pushover lib and cli",
    url = "https://github.com/nlm/pushover",
    license = "GPL",
    keywords = "pushover",
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    install_requires = [
        'requests',
    ],
    entry_points = {
        'console_scripts': [
            'pushover = pushover.__main__:main',
        ],
    },
)
