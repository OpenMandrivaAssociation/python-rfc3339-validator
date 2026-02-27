Name:		python-rfc3339-validator
Version:	0.1.4
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/r/rfc3339_validator/rfc3339_validator-%{version}.tar.gz
Summary:	A pure python RFC3339 validator
URL:		https://pypi.org/project/rfc3339_validator/
License:	MIT license
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
A pure python RFC3339 validator

%files
%{py_sitedir}/rfc3339_validator.py
%{py_sitedir}/rfc3339_validator-*.*-info
