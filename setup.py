from setuptools import setup, find_packages

setup(
    name='jupyterhub-singleuser',
    version='0.7.2',
    description='Single-user server for running JupyterNotebooks with JupyterHub',
    url='https://github.com/yuvipanda/jupyterhub-singleuser',
    author='Yuvi Panda',
    author_email='yuvipanda@gmail.com',
    license='3 Clause BSD',
    packages=find_packages(),
    scripts=['scripts/jupyterhub-singleuser'],
    install_requires=[
        'traitlets>=4.1',
        'tornado>=4.1',
        'jinja2',
        'notebook>=4.0',
        'requests'
    ]
)
