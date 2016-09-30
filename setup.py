from setuptools import setup,find_packages

setup(
    name = "telegram",
    version = "0.1",
    packages = find_packages(),
    author = "Nicolas Limage",
    author_email = 'github@xephon.org',
    description = "simple telegram lib and cli",
    url = "https://github.com/nlm/telegram",
    license = "GPL",
    keywords = "telegram",
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
            'telegram = telegram.__main__:main',
        ],
    },
)
