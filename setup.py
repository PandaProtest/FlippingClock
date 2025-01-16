from setuptools import setup, find_packages

setup(
    name="flipping_clock",  # Package name
    version="1.0.0",  # Package version
    description="A full-screen clock with flipping animations for Linux.",  # Short description
    long_description=open("README.md").read(),  # Detailed description (from README)
    long_description_content_type="text/markdown",  # Specify markdown format for long description
    author="pandaprotest",  # Your name
    author_email="your.email@example.com",  # Your email
    url="https://github.com/yourusername/flipping_clock",  # Project URL (GitHub or others)
    packages=find_packages(),  # Automatically find and include all packages
    include_package_data=True,  # Include non-code files specified in MANIFEST.in
    install_requires=[
        "pygame>=2.1.0"  # Specify dependencies
    ],
    entry_points={
        "console_scripts": [
            "flipping-clock = flipping_clock.main:start_clock"  # CLI command to run the app
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX :: Linux",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.6",  # Minimum Python version
)
