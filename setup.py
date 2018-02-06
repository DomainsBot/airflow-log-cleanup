from setuptools import setup


def load_requirements(req_path):
    with open(req_path, 'r', encoding='utf-8') as req_file:
        return [req for req in req_file if not req.startswith('#')]

setup(
    name='airflow_log_cleanup',
    version='0.0.1',
    description='Remove old airflow logs to prevent infinite growth',
    classifiers=[
        'License :: MIT',
        'Programming Language :: Python :: 3',
        'Operating System :: POSIX :: Linux',
        'Topic :: Internet'
    ],
    keywords='airflow, maintenance, logs, cleanup',
    url='https://github.com/DomainsBot/airflow-log-cleanup',
    author='DomainsBot',
    zip_safe=False,
    packages=['airflow_log_cleanup'],
    install_requires=load_requirements('requirements.txt')
)
