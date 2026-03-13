#
# Conditional build:
%bcond_with	tests	# unit tests (not included in sdist)

Summary:	AWS SAM Translator - library to transform SAM templates into AWS CloudFormation templates
Summary(pl.UTF-8):	AWS SAM Translator - biblioteka do tłumaczenia szablonów SAM do szablonów AWS CloudFormation
Name:		python3-aws-sam-translator
Version:	1.107.0
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/aws-sam-translator/
Source0:	https://files.pythonhosted.org/packages/source/a/aws-sam-translator/aws_sam_translator-%{version}.tar.gz
# Source0-md5:	472498445f203d35cb90d6325a0e9d3e
URL:		https://pypi.org/project/aws-sam-translator/
BuildRequires:	python3-modules >= 1:3.8
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-PyYAML >= 6.0
BuildRequires:	python3-PyYAML < 7
BuildRequires:	python3-boto3 >= 1.34.0
BuildRequires:	python3-boto3 < 2
BuildRequires:	python3-dateparser >= 1.1
BuildRequires:	python3-dateparser < 2
BuildRequires:	python3-jsonschema >= 4.23
BuildRequires:	python3-jsonschema < 5
BuildRequires:	python3-parameterized >= 0.7.4
BuildRequires:	python3-parameterized < 1
BuildRequires:	python3-pydantic >= 2.12.5
BuildRequires:	python3-pydantic < 2.13
BuildRequires:	python3-pytest >= 6.2
BuildRequires:	python3-pytest-cov >= 2.10
BuildRequires:	python3-pytest-cov < 5
BuildRequires:	python3-pytest-env >= 0.6
BuildRequires:	python3-pytest-env < 1
BuildRequires:	python3-pytest-rerunfailures >= 9.1
BuildRequires:	python3-pytest-rerunfailures < 12
BuildRequires:	python3-pytest-xdist >= 2.5
BuildRequires:	python3-pytest-xdist < 4
BuildRequires:	python3-tenacity >= 9.0
BuildRequires:	python3-tenacity < 10
BuildRequires:	python3-typing_extensions >= 4.4
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The AWS Serverless Application Model (SAM) is an open-source framework
for building serverless applications. It provides shorthand syntax to
express functions, APIs, databases, and event source mappings. With
just a few lines of configuration, you can define the application you
want and model it.

%description -l pl.UTF-8
AWS Serverless Application Model (SAM) to mający otwarte źródła
szkielet do budowania bezserwerowych aplikacji. Udostępnia skrótową
składnię do wyrażania funkcji, API, baz danych i odwzorowań źródeł
zdarzeń. Przy użyciu tylko kilku linii konfiguracji można zdefiniować
pożądaną aplikację i ją zamodelować.

%prep
%setup -q -n aws_sam_translator-%{version}

%build
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NOTICE README.md THIRD_PARTY_LICENSES
%{py3_sitescriptdir}/samtranslator
%{py3_sitescriptdir}/aws_sam_translator-%{version}-py*.egg-info
