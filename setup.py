from setuptools import setup, find_packages

setup(
    name="wae-viral-sdk",
    version="1.0.0",
    author="WAE Media",
    author_email="contact@wildanimalencounter.com",
    description="Official Python SDK for WAE Viral Prediction Engine",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/omaralhrm/wae-viral-sdk",
    project_urls={
        "Documentation": "https://ai.wildanimalencounter.com/docs",
        "API Demo": "https://huggingface.co/spaces/OmarWAEMedia/WAE-Viral-Score-Demo",
        "Bug Tracker": "https://github.com/omaralhrm/wae-viral-sdk/issues",
    },
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.28.0",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="viral prediction ai wildlife content social-media",
)
