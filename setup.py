from setuptools import setup

setup(
    name='DiscordPyAuxiliaryLib',
    version='1.0.0',
    packages=['DiscordPyAuxiliaryLib'],
    install_requires=[
        'discord.py>=1.7.3',
        # Add other dependencies here
    ],
    author='hashimotok',
    author_email='contact@hashimotok.dev',
    url='https://github.com/Monster2408/DiscordPyAuxiliaryLib',
    download_url='https://github.com/Monster2408/DiscordPyAuxiliaryLib',
    python_requires=">=3.10.6",
    description='A library to assist with Discord.py development',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Operating System :: OS Independent',
    ],
    keywords='discord.py auxiliary library',
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'discord-py-auxiliary-lib=DiscordPyAuxiliaryLib.__main__:main',
        ],
    },
    project_urls={
        'Documentation': 'https://discord-py-auxiliary-lib.readthedocs.io/',
        'Source': 'https://github.com/Monster2408/DiscordPyAuxiliaryLib',
        'Tracker': 'https://github.com/Monster2408/DiscordPyAuxiliaryLib/issues',
    },
    license='MIT',
    license_files=('LICENSE',),
    package_data={
        'DiscordPyAuxiliaryLib': ['data/*.json', 'data/*.yaml'],
    },
    scripts=['scripts/discord_py_auxiliary_script.py'],
)