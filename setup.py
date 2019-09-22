# vim:fileencoding=utf-8:noet:tabstop=4:softtabstop=4:shiftwidth=4:expandtab:
import pathlib
from setuptools import setup

setup(
    name             = 'powerline-kubernetes',
    description      = 'A Powerline segment to show Kubernetes context',
    long_description = (pathlib.Path(__file__).parent / "README.md").read_text(),
    long_description_content_type="text/markdown",
    version          = '1.1.0',
    keywords         = 'powerline kubernetes context',
    license          = 'MIT',
    author           = 'kiemilcz',
    author_email     = 'stanislaw.dev@gmail.com',
    url              = 'https://github.com/kiemlicz/powerline-kubernetes',
    packages         = ['powerline_kubernetes'],
    install_requires = ['powerline-status', 'kubernetes'],
    classifiers      = [
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Terminals'
    ]
)
