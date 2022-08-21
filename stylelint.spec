%global debug_package %{nil}

# macro to filter unwanted provides from Node.js binary native modules
%nodejs_default_filter

Name: stylelint
Epoch: 100
Version: 14.11.0
Release: 1%{?dist}
BuildArch: noarch
Summary: A mighty, modern CSS linter
License: MIT
URL: https://github.com/stylelint/dart-stylelint/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: nodejs-packaging
Requires: nodejs >= 12.20.0

%description
A mighty, modern linter that helps you avoid errors and enforce
conventions in your styles.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{nodejs_sitelib}
cp -rfT node_modules %{buildroot}%{nodejs_sitelib}
pushd %{buildroot}%{_bindir} && \
    ln -fs %{nodejs_sitelib}/stylelint/bin/stylelint.js stylelint && \
    popd
chmod a+x %{buildroot}%{nodejs_sitelib}/stylelint/bin/stylelint.js
fdupes -qnrps %{buildroot}%{nodejs_sitelib}

%check

%files
%license LICENSE
%dir %{nodejs_sitelib}
%{_bindir}/*
%{nodejs_sitelib}/*

%changelog
