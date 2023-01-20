from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in master_data/__init__.py
from master_data import __version__ as version

setup(
	name="master_data",
	version=version,
	description="Master Data",
	author="Frappe Technologies Pvt. Ltd.",
	author_email="hello@frappe.io",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires,
)
